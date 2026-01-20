from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Secret key for session management (required for some potential future features)
    app.config['SECRET_KEY'] = 'dev_key_for_diet_planner'

    from diet_planner.main.routes import main
    from diet_planner.features.routes import features
    from diet_planner.auth.routes import auth
    from diet_planner.customization.routes import customization

    app.register_blueprint(main)
    app.register_blueprint(features)
    app.register_blueprint(auth)
    app.register_blueprint(customization)

    return app
