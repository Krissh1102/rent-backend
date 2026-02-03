from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import User, Auth, Verification, IDType
from ..serializers import user_to_dict

user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.route("", methods=["POST"])
def create_user():
    data = request.json

    user = User()

    auth = Auth(
        email=data["email"],
        phone=data.get("phone")
    )

    verification = Verification(
        id_type=IDType[data["idType"]] if data.get("idType") else None,
        college_name=data.get("collegeName"),
        graduation_year=data.get("graduationYear"),
        work_place=data.get("workPlace")
    )

    user.auth = auth
    user.verification = verification

    db.session.add(user)
    db.session.commit()

    return jsonify(user_to_dict(user)), 201
