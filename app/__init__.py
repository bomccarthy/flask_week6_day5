from flask import Flask
from config import Config
from flask_migrate import Migrate
from .models import db, User
from flask_login import LoginManager, login_manager

from .p_cards.routes import p_cards
from .auth.routes import auth

app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.config.from_object(Config)

# registering your blueprint
app.register_blueprint(auth)
app.register_blueprint(p_cards)

# initialize our database to work with our app
db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)

from . import routes
from . import models