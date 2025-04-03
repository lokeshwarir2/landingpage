import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize database instance
db = SQLAlchemy()
DB_NAME = "landingPage.db"

# Set PostgreSQL database URL as an environment variable
os.environ["DATABASE_URL"] = "postgresql://db_9wmx_user:9WDXxoAwSKsSNeiAe1dZ3rrp7UzbJHWD@dpg-cvnb1jngi27c738o7qd0-a.oregon-postgres.render.com/db_9wmx"

def create_app():
    app = Flask(__name__)

    # Set the app configuration
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'  # Change to a more secure key in production
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")  # Fetch from environment variable
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking to improve performance

    # Initialize database with Flask app
    db.init_app(app)

    # Import Blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import models to register them with SQLAlchemy
    from .models import User
    
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Set up Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


def create_database(app):
    """Create database file if it does not exist"""
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('✅ Created Database!')
