# Advanced Food Database with Macros
# Structure: { name, calories, protein, carbs, fats, category, healthy }

food_database = [
    # Indian Foods - Curries & Main Dishes
    {"name": "Paneer Butter Masala (1 cup)", "calories": 350, "p": 12, "c": 15, "f": 25, "category": "Indian", "healthy": False},
    {"name": "Dal Tadka (1 cup)", "calories": 180, "p": 12, "c": 25, "f": 4, "category": "Indian", "healthy": True},
    {"name": "Butter Chicken (1 cup)", "calories": 300, "p": 25, "c": 8, "f": 18, "category": "Indian", "healthy": False},
    {"name": "Chana Masala (1 cup)", "calories": 220, "p": 10, "c": 28, "f": 7, "category": "Indian", "healthy": True},
    {"name": "Rajma (1 cup)", "calories": 200, "p": 12, "c": 32, "f": 2, "category": "Indian", "healthy": True},
    {"name": "Chole Bhature", "calories": 400, "p": 14, "c": 60, "f": 12, "category": "Indian", "healthy": False},
    
    # Breads & Grains
    {"name": "Roti (1 piece)", "calories": 100, "p": 3, "c": 18, "f": 1, "category": "Indian", "healthy": True},
    {"name": "Rice (1 cup cooked)", "calories": 200, "p": 4, "c": 44, "f": 0.5, "category": "Indian", "healthy": True},
    {"name": "Biryani (1 cup)", "calories": 350, "p": 8, "c": 48, "f": 14, "category": "Indian", "healthy": False},
    {"name": "Brown Rice (1 cup)", "calories": 215, "p": 5, "c": 45, "f": 1.8, "category": "Breakfast", "healthy": True},
    {"name": "Whole Wheat Bread (2 slices)", "calories": 160, "p": 8, "c": 28, "f": 2, "category": "Breakfast", "healthy": True},
    
    # Proteins
    {"name": "Chicken Tikka (6 pcs)", "calories": 250, "p": 30, "c": 5, "f": 10, "category": "Protein", "healthy": True},
    {"name": "Grilled Chicken Breast", "calories": 165, "p": 31, "c": 0, "f": 3.6, "category": "Protein", "healthy": True},
    {"name": "Tandoori Chicken (1/2)", "calories": 220, "p": 35, "c": 2, "f": 7, "category": "Protein", "healthy": True},
    {"name": "Fish Curry (1 cup)", "calories": 180, "p": 25, "c": 4, "f": 8, "category": "Protein", "healthy": True},
    {"name": "Grilled Fish (150g)", "calories": 200, "p": 30, "c": 0, "f": 8, "category": "Protein", "healthy": True},
    {"name": "Mutton Curry (1 cup)", "calories": 280, "p": 28, "c": 6, "f": 15, "category": "Protein", "healthy": False},
    {"name": "Tofu (100g)", "calories": 76, "p": 8, "c": 2, "f": 5, "category": "Protein", "healthy": True},
    
    # Eggs
    {"name": "Eggs (2 boiled)", "calories": 155, "p": 13, "c": 1.1, "f": 11, "category": "Protein", "healthy": True},
    {"name": "Egg Omelet (3 eggs)", "calories": 280, "p": 18, "c": 2, "f": 22, "category": "Breakfast", "healthy": True},
    {"name": "Scrambled Eggs (2 eggs)", "calories": 180, "p": 12, "c": 1, "f": 14, "category": "Breakfast", "healthy": True},
    
    # South Indian
    {"name": "Dosa (Plain)", "calories": 133, "p": 3, "c": 23, "f": 3, "category": "South Indian", "healthy": True},
    {"name": "Masala Dosa", "calories": 200, "p": 5, "c": 32, "f": 6, "category": "South Indian", "healthy": True},
    {"name": "Idli (2 pcs)", "calories": 120, "p": 4, "c": 24, "f": 0.5, "category": "South Indian", "healthy": True},
    {"name": "Uttapam (1 pc)", "calories": 150, "p": 5, "c": 28, "f": 3, "category": "South Indian", "healthy": True},
    {"name": "Sambar (1 cup)", "calories": 80, "p": 4, "c": 12, "f": 2, "category": "South Indian", "healthy": True},
    
    # Breakfast Items
    {"name": "Oats (1 cup cooked)", "calories": 150, "p": 6, "c": 27, "f": 3, "category": "Breakfast", "healthy": True},
    {"name": "Cornflakes with Milk", "calories": 180, "p": 6, "c": 32, "f": 3, "category": "Breakfast", "healthy": True},
    {"name": "Paratha (1 piece)", "calories": 250, "p": 5, "c": 35, "f": 10, "category": "Breakfast", "healthy": False},
    {"name": "Aloo Paratha (1 pc)", "calories": 280, "p": 6, "c": 38, "f": 12, "category": "Breakfast", "healthy": False},
    {"name": "Poha (1 cup)", "calories": 110, "p": 2, "c": 24, "f": 1, "category": "Breakfast", "healthy": True},
    {"name": "Upma (1 cup)", "calories": 140, "p": 4, "c": 26, "f": 2, "category": "Breakfast", "healthy": True},
    
    # Fruits
    {"name": "Banana", "calories": 105, "p": 1.3, "c": 27, "f": 0.3, "category": "Fruit", "healthy": True},
    {"name": "Apple", "calories": 95, "p": 0.5, "c": 25, "f": 0.3, "category": "Fruit", "healthy": True},
    {"name": "Orange", "calories": 85, "p": 1.2, "c": 21, "f": 0.3, "category": "Fruit", "healthy": True},
    {"name": "Mango (1 medium)", "calories": 135, "p": 1, "c": 35, "f": 0.4, "category": "Fruit", "healthy": True},
    {"name": "Papaya (1 cup)", "calories": 55, "p": 0.9, "c": 14, "f": 0.2, "category": "Fruit", "healthy": True},
    {"name": "Strawberries (1 cup)", "calories": 49, "p": 1, "c": 12, "f": 0.5, "category": "Fruit", "healthy": True},
    {"name": "Guava", "calories": 68, "p": 2.6, "c": 14, "f": 1, "category": "Fruit", "healthy": True},
    
    # Vegetables
    {"name": "Carrot (1 medium)", "calories": 25, "p": 0.6, "c": 6, "f": 0.1, "category": "Vegetable", "healthy": True},
    {"name": "Broccoli (1 cup)", "calories": 55, "p": 3.7, "c": 11, "f": 0.6, "category": "Vegetable", "healthy": True},
    {"name": "Spinach (1 cup)", "calories": 7, "p": 0.9, "c": 1.1, "f": 0.1, "category": "Vegetable", "healthy": True},
    {"name": "Tomato (1 medium)", "calories": 22, "p": 1.1, "c": 5, "f": 0.2, "category": "Vegetable", "healthy": True},
    {"name": "Cucumber (1 cup)", "calories": 16, "p": 0.8, "c": 3.6, "f": 0.1, "category": "Vegetable", "healthy": True},
    
    # Dairy
    {"name": "Yogurt (1 cup)", "calories": 100, "p": 10, "c": 8, "f": 3, "category": "Dairy", "healthy": True},
    {"name": "Greek Yogurt (1 cup)", "calories": 130, "p": 20, "c": 9, "f": 0.5, "category": "Dairy", "healthy": True},
    {"name": "Paneer (100g)", "calories": 265, "p": 28, "c": 2, "f": 17, "category": "Dairy", "healthy": True},
    {"name": "Milk (1 cup)", "calories": 150, "p": 8, "c": 12, "f": 8, "category": "Dairy", "healthy": True},
    {"name": "Cheese (30g)", "calories": 120, "p": 7, "c": 1, "f": 10, "category": "Dairy", "healthy": False},
    
    # Snacks
    {"name": "Almonds (10 pcs)", "calories": 70, "p": 2.5, "c": 2.5, "f": 6, "category": "Snack", "healthy": True},
    {"name": "Peanuts (1 oz)", "calories": 160, "p": 7, "c": 5, "f": 14, "category": "Snack", "healthy": True},
    {"name": "Cashews (10 pcs)", "calories": 155, "p": 5, "c": 9, "f": 12, "category": "Snack", "healthy": True},
    {"name": "Samosa (1 pc)", "calories": 250, "p": 4, "c": 24, "f": 16, "category": "Snack", "healthy": False},
    {"name": "Namkeen Mix (30g)", "calories": 150, "p": 4, "c": 15, "f": 8, "category": "Snack", "healthy": False},
    {"name": "Roasted Chickpeas (1 cup)", "calories": 210, "p": 12, "c": 28, "f": 4, "category": "Snack", "healthy": True},
    
    # Beverages
    {"name": "Green Tea (1 cup)", "calories": 2, "p": 0, "c": 0, "f": 0, "category": "Beverage", "healthy": True},
    {"name": "Black Tea with Milk", "calories": 30, "p": 1, "c": 4, "f": 1, "category": "Beverage", "healthy": True},
    {"name": "Coffee with Milk", "calories": 50, "p": 2, "c": 5, "f": 2, "category": "Beverage", "healthy": True},
    {"name": "Protein Shake (1 cup)", "calories": 150, "p": 20, "c": 10, "f": 3, "category": "Beverage", "healthy": True},
]

def get_healthy_suggestion():
    import random
    healthy_foods = [f for f in food_database if f['healthy']]
    return random.choice(healthy_foods) if healthy_foods else None

def get_diet_plan(target_calories):
    # Same simple logic for now, could be enhanced with macros awareness
    plan = {
        "breakfast": [],
        "lunch": [],
        "dinner": [],
        "snacks": [],
        "total_calories": 0
    }
    
    targets = {
        "breakfast": target_calories * 0.2,
        "lunch": target_calories * 0.35,
        "dinner": target_calories * 0.35,
        "snacks": target_calories * 0.1
    }
    
    # Helper to find closest food match
    def find_food(calories_needed):
        # Sort by closeness to calories_needed
        candidates = sorted(food_database, key=lambda x: abs(x['calories'] - calories_needed))
        return candidates[0] if candidates else None

    # Breakfast
    b_item = find_food(targets['breakfast'])
    if b_item:
        plan['breakfast'].append(b_item)
        plan['total_calories'] += b_item['calories']
        
    # Lunch 
    l_item = find_food(targets['lunch'])
    if l_item: 
        plan['lunch'].append(l_item)
        plan['total_calories'] += l_item['calories']

    # Dinner
    d_item = find_food(targets['dinner'])
    if d_item:
        plan['dinner'].append(d_item)
        plan['total_calories'] += d_item['calories']
        
    # Snack
    s_item = find_food(targets['snacks'])
    if s_item:
        plan['snacks'].append(s_item)
        plan['total_calories'] += s_item['calories']
        
    return plan
