import os
os.environ['DATABASE_URL'] = "postgresql://root:DlYe4QjalVn7AlS768RDSYLy8wA4Aehb@dpg-cok26rm3e1ms73blvc30-a.oregon-postgres.render.com/landingpage_evvt"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os
db = SQLAlchemy()
DB_NAME = "landingPage.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    #postgres://root:DlYe4QjalVn7AlS768RDSYLy8wA4Aehb@dpg-cok26rm3e1ms73blvc30-a.oregon-postgres.render.com/landingpage_evvt
    db.init_app(app)
    #set DATABASE_URL=#postgresql://root:DlYe4QjalVn7AlS768RDSYLy8wA4Aehb@dpg-cok26rm3e1ms73blvc30-a.oregon-postgres.render.com/landingpage_evvt
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')