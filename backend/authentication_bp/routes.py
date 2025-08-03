from flask import Blueprint, make_response, jsonify, session, request, redirect
from flask_jwt_extended import create_access_token
from urllib.parse import urlencode
from werkzeug.security import generate_password_hash, check_password_hash


from models.models import User
from initResources.db import db
from scripting.initialiseValues import jwt_time_period as jwt_period


# Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


# used for logging out the user
@auth_bp.route("/logout")
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200


# Login route:
@auth_bp.route("/login")
def login():
    print(f"\nIn User Login")
    data = request.get_json()
    email = data['email']
    password = data['password']
    user  = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=str(user.id))
        print(f"\nUser's name: {email}")
        print(f"User's password: {user.password}\n")
        print(f"Access token: {access_token}")
        
        return {
            'access_token': f"{access_token}",
        }, 200
    return {'message': "Invalid credentials"}, 401


# Register route:
@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()
    email = data['email']
    password = data['password']
    hashed_password = generate_password_hash(password)

    if not email or not password:
        return {'message': "Username or password missing"}, 400
    
    if User.query.filter_by(email=email).first():
        return {'message':"User already exists"}, 400
    
    newUser = User(email=email, password=hashed_password)
    db.session.add(newUser)
    db.session.commit()
    return {'message': "✌️🥳 User registered successfully."}, 201



# used to send the JWT token to the frontend
@auth_bp.route("/token")
def send_token_to_frontend():
    jwt_token = request.cookies.get("jwt_token")
    if not jwt_token:
        return jsonify({"msg": "No token"}), 401
    return jsonify({"jwt_token": jwt_token})



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