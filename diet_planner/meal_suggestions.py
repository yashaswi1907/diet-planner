"""
Meal Suggestion Engine
Provides alternative meal suggestions and recommendations for diet plans
"""

from diet_planner.food_data import food_database
import random


class MealSuggestions:
    """Provides alternative meal suggestions and recommendations"""
    
    def __init__(self):
        self.food_db = food_database
    
    def get_alternative_meals(self, current_meal, calorie_range=50, limit=5):
        """
        Get alternative meals for a given meal
        
        Args:
            current_meal: Current meal dict with calories
            calorie_range: How many calories range to look for (default ±50)
            limit: Maximum number of suggestions
        
        Returns:
            List of alternative meal suggestions
        """
        target_calories = current_meal.get('calories', 200)
        min_cal = target_calories - calorie_range
        max_cal = target_calories + calorie_range
        
        alternatives = [
            f for f in self.food_db
            if min_cal <= f['calories'] <= max_cal
            and f['name'] != current_meal.get('name')
        ]
        
        # Shuffle and limit
        random.shuffle(alternatives)
        return alternatives[:limit]
    
    def get_healthier_alternatives(self, current_meal, limit=3):
        """Get healthier alternatives for a meal"""
        target_calories = current_meal.get('calories', 200)
        
        # Look for healthy foods in similar calorie range
        healthier = [
            f for f in self.food_db
            if f['healthy'] and
            abs(f['calories'] - target_calories) <= 80 and
            f['name'] != current_meal.get('name')
        ]
        
        # Sort by closest calorie match
        healthier.sort(key=lambda x: abs(x['calories'] - target_calories))
        return healthier[:limit]
    
    def get_similar_category_meals(self, current_meal, limit=4):
        """Get meals from same category"""
        category = current_meal.get('category', 'Breakfast')
        target_calories = current_meal.get('calories', 200)
        
        similar = [
            f for f in self.food_db
            if f['category'] == category and
            f['name'] != current_meal.get('name')
        ]
        
        # Sort by calorie proximity
        similar.sort(key=lambda x: abs(x['calories'] - target_calories))
        return similar[:limit]
    
    def get_protein_boosted_meals(self, current_meal, limit=3):
        """Get high-protein alternatives"""
        target_calories = current_meal.get('calories', 200)
        
        high_protein = [
            f for f in self.food_db
            if f['p'] >= 20 and  # High protein
            abs(f['calories'] - target_calories) <= 100 and
            f['name'] != current_meal.get('name')
        ]
        
        # Sort by protein content (descending)
        high_protein.sort(key=lambda x: x['p'], reverse=True)
        return high_protein[:limit]
    
    def get_low_carb_meals(self, current_meal, limit=3):
        """Get low-carb alternatives"""
        target_calories = current_meal.get('calories', 200)
        
        low_carb = [
            f for f in self.food_db
            if f['c'] <= 15 and  # Low carbs
            abs(f['calories'] - target_calories) <= 100 and
            f['name'] != current_meal.get('name')
        ]
        
        low_carb.sort(key=lambda x: x['c'])
        return low_carb[:limit]
    
    def get_combo_meal_suggestions(self, target_calories, macro_target):
        """
        Suggest food combinations for a meal to hit macro targets
        
        Args:
            target_calories: Total calories for the meal
            macro_target: Dict with target macros {carbs: %, protein: %, fats: %}
        
        Returns:
            List of meal combinations
        """
        combinations = []
        
        # Try different food combinations
        for i, main_food in enumerate(self.food_db[:20]):  # Sample main foods
            remaining_cal = target_calories - main_food['calories']
            if remaining_cal < 0:
                continue
            
            # Find a side dish to complement
            for side_food in self.food_db[20:40]:
                if abs((main_food['calories'] + side_food['calories']) - target_calories) < 50:
                    combo = {
                        'main': main_food,
                        'side': side_food,
                        'total_calories': main_food['calories'] + side_food['calories'],
                        'total_protein': main_food['p'] + side_food['p'],
                        'total_carbs': main_food['c'] + side_food['c'],
                        'total_fats': main_food['f'] + side_food['f']
                    }
                    combinations.append(combo)
            
            if len(combinations) >= 3:
                break
        
        return combinations
    
    def get_daily_suggestions(self, breakfast, lunch, dinner, snack, tdee):
        """
        Get suggestions for each meal along with the plan
        
        Returns:
            Dict with suggestions for each meal
        """
        suggestions = {
            'breakfast_alternatives': self.get_alternative_meals(breakfast, limit=3),
            'breakfast_healthier': self.get_healthier_alternatives(breakfast, limit=2),
            'lunch_alternatives': self.get_alternative_meals(lunch, limit=3),
            'lunch_high_protein': self.get_protein_boosted_meals(lunch, limit=2),
            'dinner_alternatives': self.get_alternative_meals(dinner, limit=3),
            'dinner_low_carb': self.get_low_carb_meals(dinner, limit=2),
            'snack_alternatives': self.get_alternative_meals(snack, limit=3),
        }
        
        return suggestions
    
    def get_random_healthy_meal(self):
        """Get a random healthy meal suggestion"""
        healthy_foods = [f for f in self.food_db if f['healthy']]
        return random.choice(healthy_foods) if healthy_foods else None
    
    def search_meals(self, query, limit=5):
        """Search for meals by name"""
        query_lower = query.lower()
        results = [
            f for f in self.food_db
            if query_lower in f['name'].lower()
        ]
        return results[:limit]
    
    def get_meals_by_calories(self, min_cal, max_cal, limit=5):
        """Get meals within a calorie range"""
        meals = [
            f for f in self.food_db
            if min_cal <= f['calories'] <= max_cal
        ]
        random.shuffle(meals)
        return meals[:limit]
    
    def get_meals_by_protein(self, min_protein, max_protein=None, limit=5):
        """Get meals by protein content"""
        if max_protein is None:
            max_protein = 100
        
        meals = [
            f for f in self.food_db
            if min_protein <= f['p'] <= max_protein
        ]
        
        meals.sort(key=lambda x: x['p'], reverse=True)
        return meals[:limit]


# Global instance
meal_suggestions = MealSuggestions()
