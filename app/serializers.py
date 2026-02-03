def user_to_dict(user):
    return {
        "id": str(user.id),
        "auth": {
            "email": user.auth.email,
            "phone": user.auth.phone,
            "isPhoneVerified": user.auth.is_phone_verified,
            "lastLogin": user.auth.last_login
        },
        "verification": {
            "isVerified": user.verification.is_verified if user.verification else False,
            "idType": user.verification.id_type.value if user.verification and user.verification.id_type else None,
            "collegeName": user.verification.college_name if user.verification else None,
            "graduationYear": user.verification.graduation_year if user.verification else None,
            "workPlace": user.verification.work_place if user.verification else None,
            "verificationScore": user.verification.verification_score if user.verification else 0
        }
    }
