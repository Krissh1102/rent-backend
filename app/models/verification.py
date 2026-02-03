import enum
from ..extensions import db

class IDType(enum.Enum):
    Aadhaar = "Aadhaar"
    Passport = "Passport"
    StudentID = "StudentID"


class Verification(db.Model):
    __tablename__ = "verification"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("users.id"),
        unique=True
    )

    is_verified = db.Column(db.Boolean, default=False)

    id_type = db.Column(
        db.Enum(IDType, name="id_type_enum"),
        nullable=True
    )

    college_name = db.Column(db.String(255))
    graduation_year = db.Column(db.Integer)

    work_place = db.Column(db.String(255), nullable=True)

    verification_score = db.Column(db.Integer, default=0)
