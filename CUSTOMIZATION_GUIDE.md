# Diet Planner - Customization Features Guide

## 🎯 New Features Added

Your diet planner app has been extended with comprehensive customization capabilities. Here's what's new:

---

## 📋 Features Overview

### 1. **Macro Customization**
- **Pre-built Presets:**
  - **Balanced**: 50% Carbs, 30% Protein, 20% Fat
  - **High Protein**: 40% Carbs, 40% Protein, 20% Fat
  - **Low Carb**: 30% Carbs, 35% Protein, 35% Fat
  - **Keto**: 5% Carbs, 30% Protein, 65% Fat
  - **High Carb**: 60% Carbs, 25% Protein, 15% Fat

- **Custom Macros**: Create your own macro split with any percentage combination (must total 100%)

### 2. **Dietary Restrictions**
- Vegetarian
- Vegan
- Gluten Free
- (Easily extensible for more restrictions)

### 3. **Cuisine Preferences**
- Indian
- Breakfast
- Protein
- Dairy
- Fruits
- Snacks

### 4. **Food Exclusions**
- Exclude specific foods you don't like
- Enter multiple foods separated by commas

### 5. **Meal Distribution**
- Customize the percentage of calories for each meal
- Default: Breakfast 25%, Lunch 35%, Dinner 35%, Snacks 5%

---

## 🚀 How to Use

### Step 1: Access Customization
1. Log in to your diet planner account
2. Go to **Customize Preferences** from the main menu
3. Or navigate to `/customize/preferences`

### Step 2: Set Your Preferences
1. **Select Macro Preset**: Choose from pre-built macro splits
2. **Or Use Custom Macros**: Toggle custom macros and enter your preferred percentages
3. **Dietary Restrictions**: Check any restrictions that apply to you
4. **Preferred Cuisines**: Select food categories you enjoy
5. **Exclude Foods**: List any foods you want to avoid
6. Click **Save Preferences**

### Step 3: Generate Custom Plan
1. Go to **Generate Custom Plan** or navigate to `/customize/generate`
2. Choose a macro distribution (or use your saved preference)
3. Click **Generate My Custom Plan**
4. Your new personalized diet plan will be created!

---

## 📂 New Files Added

### Backend Modules:
- `diet_planner/diet_plan_customizer.py` - Core customization logic
- `diet_planner/customization/routes.py` - API endpoints and routes
- `diet_planner/customization/__init__.py` - Module initialization

### Frontend Templates:
- `diet_planner/templates/customize_preferences.html` - Preferences management UI
- `diet_planner/templates/generate_custom_plan.html` - Plan generation UI

### Updated Files:
- `diet_planner/__init__.py` - Registered new customization blueprint
- `diet_planner/data_store.py` - Added diet preferences storage for users

---

## 🔧 API Endpoints

### REST API for Advanced Users

**Get Current Preferences:**
```
GET /customize/api/macros
```

**Update Macros:**
```
POST /customize/api/macros
Content-Type: application/json
{
  "carbs": 50,
  "protein": 30,
  "fats": 20
}
```

**Get Dietary Restrictions:**
```
GET /customize/api/restrictions
```

**Add/Remove Restriction:**
```
POST /customize/api/restrictions
Content-Type: application/json
{
  "restriction": "vegetarian",
  "action": "add"  // or "remove"
}
```

---

## 💡 Tips & Best Practices

1. **For Weight Loss**: Use "High Protein" or "Low Carb" preset to stay fuller longer
2. **For Muscle Gain**: Use "High Protein" preset with increased calories
3. **For Athletes**: Use "High Carb" preset to fuel workouts
4. **For Beginners**: Start with "Balanced" preset
5. **Customize as You Go**: Update preferences anytime to generate a new plan

---

## 🔍 How It Works

### Diet Plan Generation Algorithm:
1. Filters foods based on your dietary restrictions and preferences
2. Excludes foods on your exclusion list
3. Selects meals for each time slot that match your macro targets
4. Calculates total macros and calories for the plan
5. Saves the plan to your profile

### Smart Matching:
- Finds foods closest to your calorie targets for each meal
- Respects cuisine preferences
- Avoids allergenic foods
- Ensures variety by not repeating foods in one plan

---

## 📊 Example Use Cases

### Case 1: Vegetarian High-Protein Diet
- Macro Preset: High Protein
- Dietary Restriction: Vegetarian
- Cuisines: Indian, Breakfast, Dairy
- Generate Plan ➜ Get vegetarian-friendly, high-protein meals

### Case 2: Keto Diet with Allergies
- Macro Preset: Keto
- Exclude Foods: Oats, Bread, Rice
- Dietary Restriction: None
- Generate Plan ➜ Get low-carb meals without excluded items

### Case 3: Balanced with Specific Tastes
- Macro Preset: Balanced
- Custom Macros: 45% Carbs, 35% Protein, 20% Fats
- Preferred Cuisines: Indian, Protein
- Generate Plan ➜ Get customized Indian meals

---

## ⚙️ Customization Architecture

```
DietPlanCustomizer Class
├── MACRO_PRESETS (5 preset splits)
├── set_macro_preset() - Use built-in preset
├── set_custom_macros() - Create custom split
├── add_dietary_restriction() - Add restrictions
├── set_preferred_cuisines() - Set food preferences
├── exclude_food() - Blacklist foods
├── generate_plan() - Create customized plan
└── Helper Methods
    ├── _get_filtered_foods() - Filter by preferences
    └── _find_best_food() - Match calorie targets
```

---

## 🔐 Data Storage

All preferences are saved per user in the following structure:
```python
'diet_preferences': {
    'macro_preset': 'balanced',
    'custom_macros': None,  # or {carbs, protein, fats}
    'dietary_restrictions': [],
    'food_allergies': [],
    'preferred_cuisines': [],
    'exclude_foods': [],
    'meal_distribution': {breakfast, lunch, dinner, snacks}
}
```

---

## 🧪 Testing the Features

To test locally:
1. Start the app: `python run.py`
2. Register a new account
3. Fill in your profile (age, weight, activity level, etc.)
4. Go to Customize Preferences and set your preferences
5. Click Generate Custom Plan
6. View your personalized diet plan on the main dashboard

---

## 🚀 Future Enhancements

Possible additions to expand customization:
- Allergen tracking beyond basic restrictions
- Meal prep time preferences
- Budget-based food selection
- Seasonal food preferences
- Recipe complexity levels
- Integration with nutrition databases (USDA, etc.)
- Meal swapping/suggestions
- Macro tracking with real-time adjustments

---

## 📞 Support

For issues or questions about the customization features:
1. Check the logs for error messages
2. Review your preferences in the UI
3. Ensure all dietary restrictions are properly saved
4. Try regenerating the plan with different settings

---

**Happy Dieting! 🥗💪**
