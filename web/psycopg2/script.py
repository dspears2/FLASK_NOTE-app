from website.models import User
import psycopg2


DB_HOST = 'postgresql://postgres@pg:5432/notes'
DB_NAME = 'notes'
DB_USER = 'postgres'
DB_PASS = ''

# Connect to your postgres DB
conn = psycopg2.connect(

    dbname=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASS, port=5432
)
conn.set_session(autocommit=True)

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute(
    """
    DROP TABLE IF EXISTS notes
    """
)

cur.execute("CREATE TABLE users(id SERIAL PRIMARY KEY,first_name TEXT NOT NULL,email TEXT NOT NULL UNIQUE,password TEXT NOT NULL,notes VARCHAR(10000))")

conn.commit()

cur.execute(
    """
    INSERT INTO veggies VALUES 
    (1, 'carrot', 'orange'),
    (2, 'onion', 'yellow'),
    (3, 'onion', 'red'),
    (4, 'zucchini', 'green'),
    (5, 'squash', 'yellow'),
    (6, 'pepper', 'red'),
    (7, 'pepper', 'green'),
    (8, 'pepper', 'orange'),
    (9, 'pepper', 'yellow'),
    (10, 'onion', 'white'),
    (11, 'green bean', 'green'),
    (12, 'jicama', 'tan'),
    (13, 'tomatillo', 'green'),
    (14, 'radicchio', 'purple'),
    (15, 'potato', 'brown')
    """
)

# Execute a query

cur.execute(
    """
    SELECT * FROM veggies
    """
)

# Retrieve query results

all_users = cur.fetchall()
print("All users", all_users, '\n')

cur.execute(
    """
    SELECT * FROM users
    """
)

cur.execute(
    """
    SELECT * FROM notes
    """
)

# This query selects a result set containing veggies records with only the color and name columns.
# The cursor method fetchall() is once again used to retrieve the result set.
# A for loop is then used to print out the pairs stored in each tuple.
# Save and run this file. You should see this new output, following the previous output:

all_notes = cur.fetchall()
for n in all_notes:
    print(n[0])


print('')  # new line

cur.execute(
    """
    SELECT color, name FROM veggies ORDER BY name, color
    """
)

"""Notice that this time in the SELECT query, we are using the ORDER BY clause to sort the result set by name, then color. 
Again, we use fetchall() to retrieve the result set as a list of tuples.
We iterate through the list using a for loop, combined with a Python function named enumerate() that allows us to access the index numbers of the list items as well as the values. 
We then print each tuple pair, numbered starting from 1. Since list indexes are zero-based, we add one to the index.
We also use Python's capitalize() function on each name and color.
Save and run this file. You should now see this additional output:"""

"""veggie_records = cur.fetchall()
for i, v in enumerate(veggie_records):
    print(str(i+1) + ".", v[0].capitalize(), v[1].capitalize())"""
