import sqlite3

# --- Functions to safely add data ---

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(cursor, name, publisher_name):
    cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
    result = cursor.fetchone()
    if result:
        publisher_id = result[0]
        try:
            cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        except sqlite3.IntegrityError:
            print(f"Magazine '{name}' already exists.")
    else:
        print(f"Publisher '{publisher_name}' not found.")

def add_subscriber(cursor, name, address):
    cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
    if cursor.fetchone():
        print(f"Subscriber '{name}' at '{address}' already exists.")
    else:
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))

def add_subscription(cursor, subscriber_name, magazine_name, expiration_date):
    cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", (subscriber_name,))
    sub_result = cursor.fetchone()
    cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
    mag_result = cursor.fetchone()

    if sub_result and mag_result:
        subscriber_id = sub_result[0]
        magazine_id = mag_result[0]

        cursor.execute(
            "SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
            (subscriber_id, magazine_id)
        )
        if cursor.fetchone():
            print(f"Subscription already exists: {subscriber_name} → {magazine_name}")
        else:
            cursor.execute(
                "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                (subscriber_id, magazine_id, expiration_date)
            )
    else:
        print("Subscriber or magazine not found.")


try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
        )
        """)

        print("Tables created successfully.")

        # Insert sample data
        add_publisher(cursor, "Penguin Books")
        add_publisher(cursor, "Marvel")
        add_publisher(cursor, "National Geographic")

        add_magazine(cursor, "Science Weekly", "Penguin Books")
        add_magazine(cursor, "Marvel Monthly", "Marvel")
        add_magazine(cursor, "Wild World", "National Geographic")

        add_subscriber(cursor, "Alice", "123 Main St")
        add_subscriber(cursor, "Bob", "456 Oak Ave")
        add_subscriber(cursor, "Charlie", "789 Pine Rd")

        add_subscription(cursor, "Alice", "Science Weekly", "2025-12-31")
        add_subscription(cursor, "Bob", "Marvel Monthly", "2025-11-30")
        add_subscription(cursor, "Charlie", "Wild World", "2025-10-10")

        conn.commit()
        print("Sample data inserted successfully.")
        print("Database created and connected successfully.")

        # SQL SELECT Queries
        print("\n All subscribers:")
        cursor.execute("SELECT * FROM subscribers")
        for row in cursor.fetchall():
            print(row)

        print("\n All magazines ordered by name:")
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        for row in cursor.fetchall():
            print(row)

        print("\n Magazines by publisher 'Penguin Books':")
        cursor.execute("""
            SELECT magazines.name 
            FROM magazines 
            JOIN publishers ON magazines.publisher_id = publishers.publisher_id 
            WHERE publishers.name = 'Penguin Books'
        """)
        for row in cursor.fetchall():
            print(row)

except Exception as e:
    print("An error occurred:", e)
