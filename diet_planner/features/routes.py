from flask import Blueprint, render_template, request, redirect, url_for
from diet_planner.data_store import user_manager
from diet_planner.food_data import get_healthy_suggestion, get_diet_plan, food_database
from diet_planner.workout_data import get_weekly_workout_plan

features = Blueprint('features', __name__, url_prefix='/features')

@features.route("/")
def dashboard():
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
    return render_template("features.html")

@features.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("message", "").lower()
    response = "I'm not sure about that. Try asking about 'protein' or 'tips'."
    
    if "hello" in user_message:
        response = "Hello! I'm your AI Diet Coach. How can I help you today?"
    elif "protein" in user_message:
        response = "High protein foods include Paneer, Chicken, Lentils, and Eggs."
    elif "weight loss" in user_message:
        response = "To lose weight, aim for a calorie deficit of 300-500 kcal and increase protein intake."
    elif "water" in user_message:
        response = "Staying hydrated is key! Aim for at least 8 glasses a day."
    elif "thank" in user_message:
        response = "You're welcome! Keep crushing your goals! 💪"
        
    return response

@features.route("/suggest")
def suggest():
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
    suggestion = get_healthy_suggestion()
    return render_template("features.html", suggestion=suggestion, mode="suggestion")

@features.route("/generate_plan")
def generate_plan():
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
    
    user_data = user_manager.get_user_data()
    target = user_data['profile'].get('tdee', 2000)
    plan = get_diet_plan(target)
    return render_template("features.html", plan=plan, mode="plan", target=target)

@features.route("/workout_plan")
def workout_plan():
    if not user_manager.current_user:
        return redirect(url_for('auth.login'))
        
    user_data = user_manager.get_user_data()
    activity = user_data['profile'].get('activity', 'moderate')
    plan = get_weekly_workout_plan(activity)
    return render_template("features.html", workout_plan=plan, mode="workout", activity=activity)

@features.route("/list_foods")
def list_foods():
    return render_template("features.html", all_foods=food_database, mode="list")
