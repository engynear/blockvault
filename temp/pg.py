import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="blockvault",
    user="engynear",
    password="132wersdf"
)

cur = conn.cursor()

# cur.execute("""
# DROP TABLE models;
# """)
# conn.commit()

cur.execute("""
CREATE TABLE IF NOT EXISTS models (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    preview_path VARCHAR(255),
    type VARCHAR(50) NOT NULL,
    tags TEXT[]
);
""")
conn.commit()



cur.execute("""
INSERT INTO models (
    name,
    preview_path,
    type,
    tags
) VALUES (
    'Вибратор 3000',
    'models/1/preview',
    'Bedrock',
    '{"tag1", "tag2"}'
);
""")
conn.commit()

cur.execute("""
INSERT INTO models (
    name,
    preview_path,
    type,
    tags
) VALUES (
    'Буран',
    'models/2/preview',
    'Java',
    '{"vdnh", "Космос", "СССР", "КБ Энергия", "Буран", "Шаттл"}'
);
""")
conn.commit()

cur.execute("""
SELECT * FROM models;
""")
print(cur.fetchall())