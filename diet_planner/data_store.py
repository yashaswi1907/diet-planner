import datetime

class UserManager:
    def __init__(self):
        # Structure: { username: { 'password': str, 'profile': dict, 'diet_log': [], 'fitness_log': [], 'water': 0, 'settings': {} } }
        self.users = {}
        self.current_user = None # Simple session tracking for single-process demo availability

    def create_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = {
            'password': password,
            'profile': {},
            'diet_log': [],
            'fitness_log': [],
            'water_log': {}, # { date_str: count }
            'step_log': {},  # { date_str: count }
            'settings': {
                'theme': 'light'
            },
            'diet_preferences': {
                'macro_preset': 'balanced',
                'custom_macros': None,
                'dietary_restrictions': [],
                'food_allergies': [],
                'preferred_cuisines': ['Indian', 'Breakfast', 'Protein', 'Dairy', 'Fruit', 'Snack'],
                'exclude_foods': [],
                'meal_distribution': {'breakfast': 0.25, 'lunch': 0.35, 'dinner': 0.35, 'snacks': 0.05}
            },
            'created_at': datetime.datetime.now()
        }
        return True

    def verify_user(self, username, password):
        user = self.users.get(username)
        if user and user['password'] == password:
            self.current_user = username
            return True
        return False

    def get_user_data(self, username=None):
        target_user = username if username else self.current_user
        return self.users.get(target_user)

    def logout(self):
        self.current_user = None

    # --- Profile Helpers ---
    def update_profile(self, username, profile_data):
        if username in self.users:
            self.users[username]['profile'] = profile_data
            return True
        return False
    
    def update_diet_preferences(self, username, preferences):
        """Update diet customization preferences for user"""
        if username in self.users:
            self.users[username]['diet_preferences'].update(preferences)
            return True
        return False
    
    def get_diet_preferences(self, username=None):
        """Get diet preferences for user"""
        target_user = username if username else self.current_user
        if target_user in self.users:
            return self.users[target_user]['diet_preferences']
        return None

# Global Instance
user_manager = UserManager()
