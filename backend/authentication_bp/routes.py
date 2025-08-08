from flask import Blueprint, make_response, jsonify, session, request, redirect, make_response
from flask_jwt_extended import create_access_token, jwt_required
from urllib.parse import urlencode
from werkzeug.security import generate_password_hash, check_password_hash


from flask_jwt_extended import jwt_required, get_jwt_identity
from models.models import db, User, UserDetails
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
            'message':      "🚴‍♂️ This user already exist",
            'description':  "An account with this email already exist. Enter unique credentials, or login to your account🫣"
        }, 409
    
    newUser = User(email=email, password=hashed_password)
    db.session.add(newUser)
    db.session.commit()
    return {
        'message': "🥳 Registration successful",
        'description': "🥳 User registered successfully."
    }, 200


# update user's data: 
@auth_bp.route('/update-profile', methods=['POST'])
@jwt_required()
def update_profile():
    print(f"\n\nIn updating user info...")
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"message": "User not found."}), 404

    data = request.get_json()
    user_details = UserDetails.query.filter_by(user_id=current_user_id).first()

    if not user_details:
        user_details = UserDetails(user_id=current_user_id)
        db.session.add(user_details)

    # Optional update of provided fields
    for field in ['userName', 'userHobbies', 'socialMediaLink']:
        if field in data:
            setattr(user_details, field, data[field])
    print(data["userName"])
    print(data["userHobbies"])
    print(data["socialMediaLink"])

    db.session.commit()

    return jsonify({
        "message": "✅ Profile updated",
        "details": {
            "userName": user_details.userName,
            "userHobbies": user_details.userHobbies,
            "socialMediaLink": user_details.socialMediaLink,
        }
    }), 200


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
        print(f"Logout and session already cleared.")
        return jsonify({"message": "Already logged out."}), 202
    session.clear()
    print(f"session cleared now.")
    return jsonify({"message": "Logged out successfully"}), 200



# used to send user profile data: 
@auth_bp.route('/get-profile')
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    details = user.details

    return jsonify({
        "userEmail": user.email,
        "profile": {
            "userName": details.userName if details else "Jese Leos",
            "userHobbies": details.userHobbies if details else "@jeseleos",
            "socialMediaLink": details.socialMediaLink if details else "Open-source contributor.",
        }
    }), 200

# =========================================================



