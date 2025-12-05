import psycopg2
import time

# Wait for PostgreSQL to start
time.sleep(5)

try:
    conn = psycopg2.connect(
        host="postgres-db",
        database="testdb",
        user="testuser",
        password="testpass"
    )

    cur = conn.cursor()

    # Create table
    cur.execute("CREATE TABLE IF NOT EXISTS students (id SERIAL PRIMARY KEY, name VARCHAR(50));")

    # Insert one row
    cur.execute("INSERT INTO students (name) VALUES ('Somu');")

    # Read row
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()

    # Print table header
    print("+----+--------+")
    print("| ID | Name   |")
    print("+----+--------+")

    # Print each row formatted
    for row in rows:
        print(f"| {row[0]:<2} | {row[1]:<6} |")

    print("+----+--------+")

    # Save changes
    conn.commit()

    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)
