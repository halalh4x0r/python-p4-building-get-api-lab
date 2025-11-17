from models import db, Bakery, BakedGood
from app import app

with app.app_context():
    # Clear existing data
    BakedGood.query.delete()
    Bakery.query.delete()
    db.session.commit()

    # Create bakeries
    bakery1 = Bakery(name="Delightful donuts")
    bakery2 = Bakery(name="Incredible crullers")

    db.session.add_all([bakery1, bakery2])
    db.session.commit()

    # Create baked goods
    bg1 = BakedGood(name="Chocolate dipped donut", price=2.75, bakery_id=bakery1.id)
    bg2 = BakedGood(name="Apple-spice filled donut", price=3.5, bakery_id=bakery1.id)
    bg3 = BakedGood(name="Glazed honey cruller", price=3.25, bakery_id=bakery2.id)
    bg4 = BakedGood(name="Chocolate cruller", price=3.4, bakery_id=bakery2.id)

    db.session.add_all([bg1, bg2, bg3, bg4])
    db.session.commit()

    print("Database seeded successfully!")
