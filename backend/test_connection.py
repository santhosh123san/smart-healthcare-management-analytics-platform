from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/smart_healthcare_db"

try:
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    print("✅ Connected Successfully!")
    conn.close()
except Exception as e:
    print("❌ Error:")
    print(e)