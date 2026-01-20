from flask import Blueprint, render_template, request, redirect, url_for
from diet_planner.data_store import user_manager
from diet_planner.food_data import get_diet_plan

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
        
    user_data = user_manager.get_user_data()
    profile = user_data['profile']
    food_log = user_data['diet_log']
    
    if request.method == "POST":
        # Handle Profile Creation
        age = int(request.form.get("age"))
        gender = request.form.get("gender")
        height = float(request.form.get("height"))
        weight = float(request.form.get("weight"))
        activity = request.form.get("activity")
        
        # New V2 Fields
        diet_pref = request.form.get("diet_pref", "non-veg")
        goal = request.form.get("goal", "maintain") # loss, gain, maintain

        # Calculate BMR (Mifflin-St Jeor Equation)
        if gender == "male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
            
        # Activity Multiplier
        activity_multipliers = {
            "sedentary": 1.2,
            "light": 1.375,
            "moderate": 1.55,
            "active": 1.725,
            "very_active": 1.9
        }
        
        tdee = bmr * activity_multipliers.get(activity, 1.2)
        
        # Goal Adjustment
        if goal == "loss":
            tdee -= 500
        elif goal == "gain":
            tdee += 500
            
        # Auto-generate Diet Plan
        generated_plan = get_diet_plan(tdee)
        
        # Macros Calculation (Simple Split: 50% C, 30% P, 20% F)
        macros = {
            "carbs": int((tdee * 0.50) / 4),
            "protein": int((tdee * 0.30) / 4),
            "fats": int((tdee * 0.20) / 9)
        }

        new_profile = {
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight,
            "activity": activity,
            "diet_pref": diet_pref,
            "goal": goal,
            "bmr": int(bmr),
            "tdee": int(tdee),
            "macros": macros,
            "diet_plan": generated_plan
        }
        
        user_manager.update_profile(user_manager.current_user, new_profile)
        return redirect(url_for("main.index"))

    # Calculate totals
    total_calories = sum(item['calories'] for item in food_log)
    remaining_calories = profile.get('tdee', 0) - total_calories if profile else 0
    
    water_count = user_data.get('water_log', {}).get('today', 0)
    
    fitness_log = user_data.get('fitness_log', [])
    steps_count = user_data.get('step_log', {}).get('today', 0)
    calories_burned = sum(item['calories_burned'] for item in fitness_log)
    
    # Steps rough estimate: 0.04 cal per step
    calories_burned += int(steps_count * 0.04)

    return render_template("index.html", profile=profile, food_log=food_log, 
                           total_calories=total_calories, remaining_calories=remaining_calories, 
                           water_count=water_count, user=user_manager.current_user,
                           fitness_log=fitness_log, steps_count=steps_count, calories_burned=calories_burned)

@main.route("/add_food", methods=["POST"])
def add_food():
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
        
    name = request.form.get("food_name")
    calories = int(request.form.get("calories"))
    meal_type = request.form.get("meal_type", "snack") # breakfast, lunch, dinner, snack
    
    # Simple macro lookup (mock) or estimate
    # In a real app we'd lookup 'name' in food_database
    # For now, let's just default to some values if not found or allow manual input eventually
    from diet_planner.food_data import food_database
    found_food = next((f for f in food_database if f['name'].lower() == name.lower()), None)
    
    macros = {"p": 0, "c": 0, "f": 0}
    if found_food:
        macros = {"p": found_food.get('p',0), "c": found_food.get('c',0), "f": found_food.get('f',0)}

    import uuid
    item_id = str(uuid.uuid4())[:8]
    
    item = {
        "id": item_id,
        "name": name, 
        "calories": calories,
        "meal_type": meal_type,
        "macros": macros
    }
    
    user_manager.get_user_data()['diet_log'].append(item)
    return redirect(url_for("main.index"))

@main.route("/add_water")
def add_water():
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
    
    user_data = user_manager.get_user_data()
    # Simple integer counter for today
    current = user_data.get('water_log', {}).get('today', 0)
    if 'water_log' not in user_data: user_data['water_log'] = {}
    
    user_data['water_log']['today'] = current + 1
    return redirect(url_for("main.index"))

@main.route("/add_exercise", methods=["POST"])
def add_exercise():
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
        
    name = request.form.get("exercise_name")
    category = request.form.get("category")
    duration = int(request.form.get("duration"))
    
    # Simple Calorie Burn Estimate (METs approx)
    # Cardio: 8, Strength: 5, Yoga: 3
    mets = {"cardio": 8, "strength": 5, "yoga": 3}
    user_weight = user_manager.get_user_data()['profile'].get('weight', 70)
    
    # Formula: Calories = MET * Weight(kg) * Time(hours)
    burned = int(mets.get(category, 5) * user_weight * (duration/60))

    import uuid
    item_id = str(uuid.uuid4())[:8]
    
    item = {
        "id": item_id,
        "name": name,
        "category": category,
        "duration": duration,
        "calories_burned": burned
    }
    
    user_manager.get_user_data()['fitness_log'].append(item)
    return redirect(url_for("main.index"))

@main.route("/add_steps", methods=["POST"])
def add_steps():
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
        
    steps = int(request.form.get("steps"))
    user_manager.get_user_data()['step_log']['today'] = steps
    return redirect(url_for("main.index"))

@main.route("/delete_food/<food_id>")
def delete_food(food_id):
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
        
    log = user_manager.get_user_data()['diet_log']
    # Filter in place or reassign
    user_manager.get_user_data()['diet_log'] = [item for item in log if item.get('id') != food_id]
    return redirect(url_for("main.index"))

@main.route("/edit_food/<food_id>", methods=["GET", "POST"])
def edit_food(food_id):
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))

    log = user_manager.get_user_data()['diet_log']
    item = next((i for i in log if i.get('id') == food_id), None)
    if not item:
        return redirect(url_for("main.index"))
        
    if request.method == "POST":
        item['name'] = request.form.get("food_name")
        item['calories'] = int(request.form.get("calories"))
        return redirect(url_for("main.index"))
        
    return render_template("edit_food.html", item=item)

@main.route("/reset")
def reset():
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
    user_manager.update_profile(user_manager.current_user, {})
    user_manager.get_user_data()['diet_log'] = []
    return redirect(url_for("main.index"))
