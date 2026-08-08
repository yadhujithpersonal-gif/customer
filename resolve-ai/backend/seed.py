from database import engine, SessionLocal, Base
from models import Customer, Order


Base.metadata.create_all(bind=engine)

db = SessionLocal()


customers = [

    Customer(
        id="CUS001",
        name="Rahul",
        email="rahul@example.com",
        risk_score=0.10
    ),

    Customer(
        id="CUS002",
        name="Ananya",
        email="ananya@example.com",
        risk_score=0.20
    ),

    Customer(
        id="CUS003",
        name="Arjun",
        email="arjun@example.com",
        risk_score=0.30
    ),

    Customer(
        id="CUS004",
        name="Priya",
        email="priya@example.com",
        risk_score=0.15
    )
]


orders = [

    Order(
        id="ORD1001",
        customer_id="CUS001",
        amount=1499,
        payment_status="duplicate",
        delivery_status="delivered"
    ),

    Order(
        id="ORD1002",
        customer_id="CUS002",
        amount=799,
        payment_status="successful",
        delivery_status="delayed"
    ),

    Order(
        id="ORD1003",
        customer_id="CUS003",
        amount=15999,
        payment_status="successful",
        delivery_status="delivered"
    ),

    Order(
        id="ORD1004",
        customer_id="CUS004",
        amount=2499,
        payment_status="successful",
        delivery_status="delivered"
    )
]


for customer in customers:

    if not db.query(Customer).filter(
        Customer.id == customer.id
    ).first():

        db.add(customer)


for order in orders:

    if not db.query(Order).filter(
        Order.id == order.id
    ).first():

        db.add(order)


db.commit()

db.close()

print("Database seeded successfully.")