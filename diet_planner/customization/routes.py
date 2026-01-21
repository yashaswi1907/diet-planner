"""
Diet Plan Customization Routes
Endpoints for users to customize their diet plans
"""

from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from diet_planner.data_store import user_manager
from diet_planner.diet_plan_customizer import DietPlanCustomizer
from diet_planner.meal_suggestions import meal_suggestions

customization = Blueprint('customization', __name__, url_prefix='/customize')

@customization.route("/preferences", methods=["GET", "POST"])
def preferences():
    """View and manage diet preferences"""
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
    
    if request.method == "POST":
        # Update preferences
        macro_preset = request.form.get("macro_preset", "balanced")
        dietary_restrictions = request.form.getlist("dietary_restrictions")
        preferred_cuisines = request.form.getlist("preferred_cuisines")
        exclude_foods = request.form.get("exclude_foods", "").split(",")
        exclude_foods = [f.strip() for f in exclude_foods if f.strip()]
        
        # Optional: custom macros
        custom_macros = None
        if request.form.get("use_custom_macros"):
            try:
                carbs = int(request.form.get("custom_carbs", 50))
                protein = int(request.form.get("custom_protein", 30))
                fats = int(request.form.get("custom_fats", 20))
                
                if carbs + protein + fats == 100:
                    custom_macros = {
                        "carbs": carbs / 100,
                        "protein": protein / 100,
                        "fats": fats / 100
                    }
            except:
                pass
        
        prefs = {
            "macro_preset": macro_preset,
            "custom_macros": custom_macros,
            "dietary_restrictions": dietary_restrictions,
            "preferred_cuisines": preferred_cuisines or ["Indian", "Breakfast", "Protein"],
            "exclude_foods": exclude_foods
        }
        
        user_manager.update_diet_preferences(user_manager.current_user, prefs)
        return redirect(url_for("customization.preferences"))
    
    # GET - Show preferences
    current_prefs = user_manager.get_diet_preferences()
    
    macro_presets = {
        "balanced": "Balanced (50% Carbs, 30% Protein, 20% Fat)",
        "high_protein": "High Protein (40% Carbs, 40% Protein, 20% Fat)",
        "low_carb": "Low Carb (30% Carbs, 35% Protein, 35% Fat)",
        "keto": "Keto (5% Carbs, 30% Protein, 65% Fat)",
        "high_carb": "High Carb (60% Carbs, 25% Protein, 15% Fat)"
    }
    
    return render_template("customize_preferences.html", 
                         preferences=current_prefs,
                         macro_presets=macro_presets)


@customization.route("/generate", methods=["GET", "POST"])
def generate_custom_plan():
    """Generate a custom diet plan based on user preferences"""
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
    
    user_data = user_manager.get_user_data()
    profile = user_data['profile']
    
    if not profile.get('tdee'):
        return redirect(url_for('main.index'))
    
    if request.method == "POST":
        # Allow user to override macro preset
        macro_preset = request.form.get("macro_preset")
        
        customizer = DietPlanCustomizer()
        prefs = user_manager.get_diet_preferences()
        
        # Apply user preferences to customizer
        if macro_preset:
            customizer.set_macro_preset(macro_preset)
        else:
            customizer.user_preferences["macro_preset"] = prefs.get("macro_preset", "balanced")
        
        customizer.user_preferences["dietary_restrictions"] = prefs.get("dietary_restrictions", [])
        customizer.user_preferences["cuisines"] = prefs.get("preferred_cuisines", [])
        customizer.user_preferences["exclude_foods"] = prefs.get("exclude_foods", [])
        
        # Generate the plan
        tdee = profile.get('tdee', 2000)
        meal_dist = prefs.get("meal_distribution", {
            "breakfast": 0.25,
            "lunch": 0.35,
            "dinner": 0.35,
            "snacks": 0.05
        })
        
        custom_plan = customizer.generate_plan(tdee, meal_dist)
        
        # Update profile with new plan
        profile['diet_plan'] = custom_plan
        profile['customizer_settings'] = customizer.get_preferences()
        user_manager.update_profile(user_manager.current_user, profile)
        
        return redirect(url_for("main.index"))
    
    current_prefs = user_manager.get_diet_preferences()
    macro_presets = {
        "balanced": "Balanced (50% Carbs, 30% Protein, 20% Fat)",
        "high_protein": "High Protein (40% Carbs, 40% Protein, 20% Fat)",
        "low_carb": "Low Carb (30% Carbs, 35% Protein, 35% Fat)",
        "keto": "Keto (5% Carbs, 30% Protein, 65% Fat)",
        "high_carb": "High Carb (60% Carbs, 25% Protein, 15% Fat)"
    }
    
    return render_template("generate_custom_plan.html",
                         macro_presets=macro_presets,
                         current_preset=current_prefs.get("macro_preset", "balanced"),
                         profile=profile)


@customization.route("/api/macros", methods=["GET", "POST"])
def api_macros():
    """API endpoint for macro management"""
    if not user_manager.current_user:
        return jsonify({"error": "Not authenticated"}), 401
    
    if request.method == "GET":
        prefs = user_manager.get_diet_preferences()
        return jsonify(prefs)
    
    if request.method == "POST":
        data = request.get_json()
        
        # Validate and set macros
        if "carbs" in data and "protein" in data and "fats" in data:
            total = data["carbs"] + data["protein"] + data["fats"]
            if total == 100:
                customizer = DietPlanCustomizer()
                if customizer.set_custom_macros(data["carbs"], data["protein"], data["fats"]):
                    user_manager.update_diet_preferences(
                        user_manager.current_user,
                        {"custom_macros": customizer.user_preferences["custom_macros"]}
                    )
                    return jsonify({"success": True, "message": "Macros updated"})
        
        return jsonify({"error": "Invalid macro values"}), 400


@customization.route("/api/restrictions", methods=["GET", "POST"])
def api_restrictions():
    """API endpoint for dietary restrictions"""
    if not user_manager.current_user:
        return jsonify({"error": "Not authenticated"}), 401
    
    if request.method == "GET":
        prefs = user_manager.get_diet_preferences()
        return jsonify({"restrictions": prefs.get("dietary_restrictions", [])})
    
    if request.method == "POST":
        data = request.get_json()
        restriction = data.get("restriction")
        action = data.get("action", "add")  # add or remove
        
        prefs = user_manager.get_diet_preferences()
        restrictions = prefs.get("dietary_restrictions", [])
        
        if action == "add" and restriction not in restrictions:
            restrictions.append(restriction)
        elif action == "remove" and restriction in restrictions:
            restrictions.remove(restriction)
        
        user_manager.update_diet_preferences(
            user_manager.current_user,
            {"dietary_restrictions": restrictions}
        )
        
        return jsonify({"success": True, "restrictions": restrictions})


@customization.route("/api/meal-alternatives/<meal_name>", methods=["GET"])
def api_meal_alternatives(meal_name):
    """Get alternative meals for a given meal"""
    if not user_manager.current_user:
        return jsonify({"error": "Not authenticated"}), 401
    
    # Find the meal in the database
    from diet_planner.food_data import food_database
    current_meal = None
    for food in food_database:
        if food['name'].lower() == meal_name.lower():
            current_meal = food
            break
    
    if not current_meal:
        return jsonify({"error": "Meal not found"}), 404
    
    # Get alternatives
    alternatives = meal_suggestions.get_alternative_meals(current_meal, limit=5)
    healthier = meal_suggestions.get_healthier_alternatives(current_meal, limit=2)
    similar = meal_suggestions.get_similar_category_meals(current_meal, limit=3)
    
    return jsonify({
        "current_meal": current_meal,
        "alternatives": alternatives,
        "healthier_options": healthier,
        "similar_meals": similar
    })


@customization.route("/api/search-meals", methods=["GET"])
def api_search_meals():
    """Search for meals by query"""
    if not user_manager.current_user:
        return jsonify({"error": "Not authenticated"}), 401
    
    query = request.args.get("q", "")
    if not query or len(query) < 2:
        return jsonify({"error": "Query too short"}), 400
    
    results = meal_suggestions.search_meals(query, limit=10)
    return jsonify({"results": results})


@customization.route("/api/meals-by-calories", methods=["GET"])
def api_meals_by_calories():
    """Get meals within calorie range"""
    if not user_manager.current_user:
        return jsonify({"error": "Not authenticated"}), 401
    
    try:
        min_cal = int(request.args.get("min", 100))
        max_cal = int(request.args.get("max", 300))
    except:
        return jsonify({"error": "Invalid calorie values"}), 400
    
    meals = meal_suggestions.get_meals_by_calories(min_cal, max_cal, limit=10)
    return jsonify({"meals": meals})


@customization.route("/api/high-protein-meals", methods=["GET"])
def api_high_protein_meals():
    """Get high protein meal options"""
    if not user_manager.current_user:
        return jsonify({"error": "Not authenticated"}), 401
    
    try:
        min_protein = int(request.args.get("min", 20))
    except:
        min_protein = 20
    
    meals = meal_suggestions.get_meals_by_protein(min_protein, limit=10)
    return jsonify({"meals": meals})


@customization.route("/suggestions", methods=["GET"])
def suggestions():
    """View meal suggestions page"""
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
    
    user_data = user_manager.get_user_data()
    profile = user_data.get('profile', {})
    diet_plan = profile.get('diet_plan', {})
    
    # Get suggestions for current plan
    suggestions_data = None
    if diet_plan.get('meals'):
        meals = diet_plan['meals']
        try:
            suggestions_data = meal_suggestions.get_daily_suggestions(
                meals.get('breakfast', {}),
                meals.get('lunch', {}),
                meals.get('dinner', {}),
                meals.get('snacks', {}),
                profile.get('tdee', 2000)
            )
        except:
            suggestions_data = None
    
    return render_template("suggestions.html", 
                         diet_plan=diet_plan,
                         suggestions=suggestions_data,
                         profile=profile)

