import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create Connexion app instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get underlying Flask app instance
app = connex_app.app

sqlite_url = "sqlite:///" + os.path.join(basedir, "people.db")

# Configure SQLAlchemy
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
