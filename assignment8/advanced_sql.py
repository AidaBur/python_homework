import sqlite3
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

#TASK 1
print("Task 1: Total price of first 5 orders")

query1 = """
SELECT o.order_id,
       SUM(p.price * li.quantity) AS total_price
FROM orders o
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""

cursor.execute(query1)
for row in cursor.fetchall():
    print(row)

#TASK 2
print("\nTask 2: Average total price of each customer's orders")

query2 = """
SELECT c.customer_name,
       AVG(sub.total_price) AS average_total_price
FROM customers c
LEFT JOIN (
    SELECT o.customer_id AS customer_id_b,
           SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
) AS sub ON c.customer_id = sub.customer_id_b
GROUP BY c.customer_id;
"""

cursor.execute(query2)
for row in cursor.fetchall():
    print(row)


#TASK

print("\nTask 3: Creating new order for 'Perez and Sons'")

try:
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
    customer_id = cursor.fetchone()[0]

    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
    employee_id = cursor.fetchone()[0]

    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    product_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?, ?)
        RETURNING order_id;
    """, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    for product_id in product_ids:
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, ?);
        """, (order_id, product_id, 10))

    conn.commit()

    cursor.execute("""
        SELECT li.line_item_id, li.quantity, p.product_name
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        WHERE li.order_id = ?;
    """, (order_id,))
    print("Inserted line items:")
    for row in cursor.fetchall():
        print(row)

except Exception as e:
    conn.rollback()
    print("Error occurred during transaction:", e)


#TASK 4

print("\nTask 4: Employees with more than 5 orders")

query4 = """
SELECT e.employee_id,
       e.first_name,
       e.last_name,
       COUNT(o.order_id) AS order_count
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id
HAVING COUNT(o.order_id) > 5;
"""

cursor.execute(query4)
for row in cursor.fetchall():
    print(row)


conn.close()