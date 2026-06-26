from db_config import get_connection

conn = get_connection()
cur = conn.cursor()

name = "Electronics"
slug = "electronics"

cur.execute(
    "SELECT id FROM categories WHERE slug = %s",
    (slug,)
)

category = cur.fetchone()

if category:
    print("Category already exists")
else:
    cur.execute(
        """
        INSERT INTO categories (name, slug)
        VALUES (%s, %s)
        """,
        (name, slug)
        
    )

    conn.commit()
    print("Category Added")

cur.execute("SELECT * FROM categories")

rows = cur.fetchall()

for row in rows:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Slug:", row[2])
    print("Status:", row[4])
    print("----------------")

cur.close()
conn.close()