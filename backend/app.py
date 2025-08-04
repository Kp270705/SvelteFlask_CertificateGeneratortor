
# import os
# from pathlib import Path
# from werkzeug.utils import secure_filename
# from flask import Flask, request, jsonify, send_file, session
from flask import Flask
from flask_cors import CORS
from datetime import timedelta
# import secrets

# importing files: 
# from PythonTasks.helper import formDataHelper
# from PythonTasks.Exceptions.handleExceptions import CertificateError
from scripting.genString import generate_random_string
from scripting.initialiseValues import jwt_time_period as jwt_period
from resources_bp.routes import register_jwt_error_handlers


# importing resources:
from initResources.db import db
from initResources.jwt import jwt


# importing blueprints:
from authentication_bp import auth_bp
from resources_bp import resources_bp
from home_bp import home_bp


# -----------------------------------------------------------------------------
# FLASK INIT
# -----------------------------------------------------------------------------


def create_app():
    pass

    app = Flask(__name__)
    app.secret_key = generate_random_string(32)
    app.config['JWT_SECRET_KEY'] = generate_random_string(32)

    jwt_time_period = jwt_period

    if "seconds" in jwt_time_period:
        app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=int(jwt_time_period.split()[0]))
    elif "minutes" in jwt_time_period:
        app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=int(jwt_time_period.split()[0]))
    elif "hours" in jwt_time_period:
        app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=int(jwt_time_period.split()[0]))
    elif "days" in jwt_time_period:
        app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=int(jwt_time_period.split()[0]))
    else:
        raise ValueError("Invalid JWT time period format. Use 'seconds', 'minutes', 'hours', or 'days'.")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    CORS(app,
     supports_credentials=True,
     origins=["http://localhost:5173"],
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "OPTIONS"])
    # CORS(app, supports_credentials=True)  # allow any origin (good for dev – tighten in prod)
    # CORS(app, resources={r"/api/*": {"origins": "https://your-svelte-domain.com"}}) # this is for production.
    
    

    # initialize db :
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # initialize jwt manager
    jwt.init_app(app)
    # register JWT error handlers
    register_jwt_error_handlers()


    # registering blueprints:

    app.register_blueprint(auth_bp)
    app.register_blueprint(resources_bp)
    app.register_blueprint(home_bp)
    return app

# -----------------------------------------------------------------------------
# ENTRY‑POINT
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app = create_app()
    # 0.0.0.0 so your Svelte dev server can reach it
    app.run(host="0.0.0.0", port=5000, debug=True)
