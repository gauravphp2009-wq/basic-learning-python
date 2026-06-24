from db_config import get_connection

conn = get_connection()

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
)
""")

conn.commit()

print("Table Created Successfully")

cur.close()
conn.close()