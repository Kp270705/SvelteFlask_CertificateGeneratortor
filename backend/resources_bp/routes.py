from flask import Blueprint, jsonify, request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    JWTManager
)
from initResources.jwt import jwt

resources_bp = Blueprint('resources', __name__, url_prefix='/resources')


# ✅ Error handler registration
def register_jwt_error_handlers():
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            "message": "⚠️ Token has expired. Please re-login.",
            "error": "token_expired"
        }), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(reason):
        return jsonify({
            "message": "💔 ❌ Invalid token. Please login again.",
            "error": "invalid_token"
        }), 422

    @jwt.unauthorized_loader
    def missing_token_callback(reason):
        return jsonify({
            "message": "Authorization token missing.",
            "error": "authorization_required"
        }), 401


@resources_bp.route('/protected')
@jwt_required()
def protectedRoute():
    current_user_id = get_jwt_identity()
    print(f"\nUser ID: {current_user_id}")
    return {
        "message": "✅ You accessed protected resource",
        "secret_id": f"{current_user_id}"

    }, 200

print("✅ Resources.protected loaded")