import uuid
from datetime import datetime, timezone
from ..extensions import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(
        db.UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        index=True
    )

    auth = db.relationship(
        "Auth",
        backref=db.backref("user", lazy="joined"),
        uselist=False,
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    verification = db.relationship(
        "Verification",
        backref=db.backref("user", lazy="joined"),
        uselist=False,
        cascade="all, delete-orphan",
        passive_deletes=True
    )
