"""
Advanced Diet Plan Customization Module
Allows users to customize macros, meal preferences, and dietary restrictions
"""

from diet_planner.food_data import food_database
import random

class DietPlanCustomizer:
    """Customizable diet plan generator"""
    
    # Macro presets (percentage split)
    MACRO_PRESETS = {
        "balanced": {"carbs": 0.50, "protein": 0.30, "fats": 0.20},
        "high_protein": {"carbs": 0.40, "protein": 0.40, "fats": 0.20},
        "low_carb": {"carbs": 0.30, "protein": 0.35, "fats": 0.35},
        "keto": {"carbs": 0.05, "protein": 0.30, "fats": 0.65},
        "high_carb": {"carbs": 0.60, "protein": 0.25, "fats": 0.15},
    }
    
    def __init__(self):
        self.user_preferences = {
            "macro_preset": "balanced",
            "custom_macros": None,
            "dietary_restrictions": [],  # vegetarian, vegan, gluten_free, etc
            "food_allergies": [],
            "cuisines": ["Indian", "Breakfast", "Protein", "Dairy", "Fruit", "Snack"],
            "exclude_foods": [],
            "meal_count": 4  # breakfast, lunch, dinner, snacks
        }
    
    def set_macro_preset(self, preset_name):
        """Set macro split using a preset"""
        if preset_name in self.MACRO_PRESETS:
            self.user_preferences["macro_preset"] = preset_name
            self.user_preferences["custom_macros"] = None
            return True
        return False
    
    def set_custom_macros(self, carbs_pct, protein_pct, fats_pct):
        """Set custom macro percentages (must sum to 100)"""
        total = carbs_pct + protein_pct + fats_pct
        if total != 100:
            return False
        
        self.user_preferences["custom_macros"] = {
            "carbs": carbs_pct / 100,
            "protein": protein_pct / 100,
            "fats": fats_pct / 100
        }
        return True
    
    def add_dietary_restriction(self, restriction):
        """Add dietary restriction (vegetarian, vegan, gluten_free, etc)"""
        if restriction not in self.user_preferences["dietary_restrictions"]:
            self.user_preferences["dietary_restrictions"].append(restriction)
        return True
    
    def remove_dietary_restriction(self, restriction):
        """Remove dietary restriction"""
        if restriction in self.user_preferences["dietary_restrictions"]:
            self.user_preferences["dietary_restrictions"].remove(restriction)
        return True
    
    def add_allergy(self, allergen):
        """Add food allergy"""
        if allergen not in self.user_preferences["food_allergies"]:
            self.user_preferences["food_allergies"].append(allergen)
        return True
    
    def set_preferred_cuisines(self, cuisines):
        """Set preferred food categories/cuisines"""
        self.user_preferences["cuisines"] = cuisines
        return True
    
    def exclude_food(self, food_name):
        """Add food to exclusion list"""
        if food_name not in self.user_preferences["exclude_foods"]:
            self.user_preferences["exclude_foods"].append(food_name)
        return True
    
    def _get_filtered_foods(self):
        """Get foods that match user preferences"""
        filtered = []
        
        for food in food_database:
            # Check category/cuisine preference
            if food.get('category') not in self.user_preferences["cuisines"]:
                continue
            
            # Check exclusions
            if food['name'] in self.user_preferences["exclude_foods"]:
                continue
            
            # Check dietary restrictions
            if self.user_preferences["dietary_restrictions"]:
                if "vegetarian" in self.user_preferences["dietary_restrictions"]:
                    if food.get('category') == "Protein" and "paneer" not in food['name'].lower() and "chicken" in food['name'].lower():
                        continue
                if "vegan" in self.user_preferences["dietary_restrictions"]:
                    if food.get('category') in ["Protein", "Dairy"] and "plant" not in food['name'].lower():
                        continue
            
            filtered.append(food)
        
        return filtered
    
    def _find_best_food(self, calories_target, filtered_foods, exclude_list=None):
        """Find food closest to calorie target"""
        if exclude_list is None:
            exclude_list = []
        
        candidates = [f for f in filtered_foods if f['name'] not in exclude_list]
        if not candidates:
            return None
        
        best = min(candidates, key=lambda x: abs(x['calories'] - calories_target))
        return best
    
    def generate_plan(self, daily_calories, meal_distribution=None):
        """
        Generate customized diet plan
        
        Args:
            daily_calories: Target daily calories
            meal_distribution: Dict with meal percentages {breakfast: 0.25, ...}
        
        Returns:
            dict with meal plan and macro info
        """
        if meal_distribution is None:
            meal_distribution = {
                "breakfast": 0.25,
                "lunch": 0.35,
                "dinner": 0.35,
                "snacks": 0.05
            }
        
        # Get macro split
        if self.user_preferences["custom_macros"]:
            macros = self.user_preferences["custom_macros"]
        else:
            macros = self.MACRO_PRESETS[self.user_preferences["macro_preset"]]
        
        # Calculate macro targets
        macro_targets = {
            "carbs": int((daily_calories * macros["carbs"]) / 4),
            "protein": int((daily_calories * macros["protein"]) / 4),
            "fats": int((daily_calories * macros["fats"]) / 9)
        }
        
        # Get filtered foods
        filtered_foods = self._get_filtered_foods()
        
        # Generate meals
        plan = {
            "meals": {},
            "total_calories": 0,
            "macros": macro_targets,
            "macro_split": {k: f"{int(v*100)}%" for k, v in macros.items()}
        }
        
        used_foods = []
        
        for meal_name, meal_pct in meal_distribution.items():
            meal_calories = int(daily_calories * meal_pct)
            food = self._find_best_food(meal_calories, filtered_foods, used_foods)
            
            if food:
                plan["meals"][meal_name] = food
                plan["total_calories"] += food['calories']
                used_foods.append(food['name'])
            else:
                plan["meals"][meal_name] = None
        
        return plan
    
    def get_preferences(self):
        """Get current user preferences"""
        return self.user_preferences
    
    def update_preferences(self, prefs_dict):
        """Update multiple preferences at once"""
        for key, value in prefs_dict.items():
            if key in self.user_preferences:
                self.user_preferences[key] = value
        return True


# Global customizer instance (can be extended to per-user)
plan_customizer = DietPlanCustomizer()
