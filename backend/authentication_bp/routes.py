from flask import Blueprint, make_response, jsonify, session, request, redirect
from flask_jwt_extended import create_access_token
from urllib.parse import urlencode
from werkzeug.security import generate_password_hash, check_password_hash


from models.models import User
from initResources.db import db
from scripting.initialiseValues import jwt_time_period as jwt_period


# Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# =========================== ROUTES  ===========================


# Register route:
@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()
    email = data['email']
    password = data['password']
    hashed_password = generate_password_hash(password)
    
    if User.query.filter_by(email=email).first():
        return {
            'message':      "🚴‍♂️ User already exist",
            'description':  "An account with this email already exists. Enter unique credentials, or login to your account🫣"
        }, 409
    
    newUser = User(email=email, password=hashed_password)
    db.session.add(newUser)
    db.session.commit()
    return {
        'message': "✌️🥳 Registration successful.",
        'description': "✌️🥳 User registered successfully."
    }, 200


# Login route:
@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Check if user exists
    user = User.query.filter_by(email=email).first()
    if not user:
        return {
            'message': "🙅 User not found",
            'description': "User with these credentials not exist. Register yourself or re-login 😇"
        }, 404

    # Check password
    if check_password_hash(user.password, password):
        access_token = create_access_token(identity=str(user.id))
        session['jwt_token'] = access_token
        return {
            'message': "✌️🥳 Login Successfully",
            'description': "✌️🥳 User Login successfully.",
            'access_token': f"{access_token}",
        }, 200

    # Wrong password
    return {
        'message': "🔐 Invalid credentials",
        'description': '''You enter wrong password. Login again😇'''
    }, 401


# used for logging out the user
@auth_bp.route("/logout")
def logout():
    if not session:
        print(f"session already cleared.")
    session.clear()
    jwt_token = session.get("jwt_token", "No jwt_token found in session")
    print(f"\n\n\tSession is clear. {jwt_token}")
    return jsonify({"message": "Logged out successfully"}), 200



# used to send the JWT token to the frontend
@auth_bp.route("/token")
def send_token_to_frontend():
    jwt_token = session.get("jwt_token", "No-Token")
    if jwt_token == "No-Token":
        return jsonify({"message": "No-Token"}), 401
    return jsonify({"jwt_token": jwt_token}), 200


# use to fetch profile information
@auth_bp.route("/profile")
def profile():
    print(f"\n\n\tIn Profile route\n Name in session : {session.get('name', 'No name in session')}")
    if "name" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    # handling 's' in time period: 
    jwt_time_period = jwt_period 
    parts = jwt_time_period.split()  
    if parts[0] == "1":
        parts[1] = parts[1][:-1]
    jwt_time_period = " ".join(parts)

    return jsonify(
        {
            "email": session.get("email", "No email found in session"),
            "jwt_time_period": jwt_time_period,
        }
    )