from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime

from database import Base


class Customer(Base):

    __tablename__ = "customers"

    id = Column(String, primary_key=True)

    name = Column(String, nullable=False)

    email = Column(String, nullable=False)

    risk_score = Column(Float, default=0.1)


class Order(Base):

    __tablename__ = "orders"

    id = Column(String, primary_key=True)

    customer_id = Column(String, nullable=False)

    amount = Column(Float, nullable=False)

    payment_status = Column(String, nullable=False)

    delivery_status = Column(String, nullable=False)


class Dispute(Base):

    __tablename__ = "disputes"

    id = Column(Integer, primary_key=True)

    customer_id = Column(String)

    order_id = Column(String)

    message = Column(Text)

    category = Column(String)

    intent = Column(String)

    sentiment = Column(String)

    urgency = Column(String)

    confidence = Column(Float)

    status = Column(String)

    decision = Column(String)

    resolution = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)

    dispute_id = Column(Integer)

    action = Column(String)

    reason = Column(Text)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )