from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text  # Import the text function

app = Flask(__name__)

# Manually set the database URL (Replace with your actual Supabase URL)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:dcruzaaa@db.ovluvsecqmqwtsiewwbz.supabase.co:5432/postgres"

db = SQLAlchemy(app)

try:
    with app.app_context():
        db.session.execute(text("SELECT 1"))  # Wrap the SQL string with text()
        print("✅ Database connection successful!")
except Exception as e:
    print("❌ Database connection failed:", str(e))
