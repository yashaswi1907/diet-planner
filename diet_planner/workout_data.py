def get_weekly_workout_plan(activity_level):
    """
    Returns a dictionary with keys Sunday-Saturday containing workout descriptions
    based on the user's activity level.
    """
    # Normalize activity level string
    activity = activity_level.lower() if activity_level else "sedentary"

    # Define plans
    plans = {
        "sedentary": {
            "Sunday": "Rest & Light Stretching",
            "Monday": "20 min brisk walk",
            "Tuesday": "Rest",
            "Wednesday": "20 min brisk walk",
            "Thursday": "Rest",
            "Friday": "20 min brisk walk",
            "Saturday": "30 min light activity (gardening, cleaning, etc.)"
        },
        "light": {
            "Sunday": "Rest & Recovery",
            "Monday": "30 min Jog / Power Walk",
            "Tuesday": "20 min Bodyweight Exercises (Squats, Pushups)",
            "Wednesday": "30 min Jog / Power Walk",
            "Thursday": "Active Rest (Yoga/Stretching)",
            "Friday": "30 min Jog / Power Walk",
            "Saturday": "45 min Hike or Long Walk"
        },
        "moderate": {
            "Sunday": "Rest",
            "Monday": "45 min Cardio (Run/Cycle)",
            "Tuesday": "40 min Strength Training (Upper Body)",
            "Wednesday": "30 min HIIT Cardio",
            "Thursday": "40 min Strength Training (Lower Body)",
            "Friday": "45 min Cardio (Run/Cycle)",
            "Saturday": "60 min Active Hobby (Sports, Hiking, Swimming)"
        },
        "active": {
            "Sunday": "Active Recovery (Yoga/Light Swim)",
            "Monday": "60 min Cardio",
            "Tuesday": "60 min Strength Training (Push)",
            "Wednesday": "60 min Cardio + Core",
            "Thursday": "60 min Strength Training (Pull)",
            "Friday": "60 min HIIT",
            "Saturday": "60 min Strength Training (Legs)"
        },
        "very_active": {
            "Sunday": "Rest",
            "Monday": "AM: Cardio, PM: Strength (Chest/Tri)",
            "Tuesday": "AM: Cardio, PM: Strength (Back/Bi)",
            "Wednesday": "AM: Cardio, PM: Strength (Legs/Shoulders)",
            "Thursday": "60 min High Intensity Activity",
            "Friday": "Full Body Strength Circuit",
            "Saturday": "90+ min Endurance Activity"
        }
    }

    # Fallback to moderate if unknown
    return plans.get(activity, plans["moderate"])
