import sqlite3
# connect to a db in memory (wiped after program is exited)
# connect = sqlite3.connect(':customer:')

# saves db for future reference
connect = sqlite3.connect('customer.db')

# cursors tells a database what to do
c = connect.cursor()

# 5 Types of datatypes:
# 1. NULL (does/doesn't exist)
# 2. INTEGER (whole numbers)
# 3. REAL (decimals)
# 4. TEXT (Strings)
# 5. BLOB (stored as is - images, mp3 file, etc.)

# create a table
# ''' Creates a doc-string '''
c.execute('''CREATE TABLE IF NOT EXISTS customers (
        first_name text,
        last_name text,
        email text,
        age integer
    )''')

# insert single value
c.execute("INSERT INTO customers VALUES ('Rizwan', 'Hoque', 'imrizwanhoque@gmail.com', '19')")

# insert multiple values
customers = [
    ('Jeremy', 'Brown', 'jbrown@gmail.com', '28'),
    ('Dan', 'Bennisan', 'dwb@uga.edu', '20'), 
    ('Twuh', 'Sadaria', 'twuhDaGoat@uga.edu', '18')
]
# use '?' as the place-holder for the different values
c.executemany("INSERT INTO customers VALUES (?,?,?,?)", customers)

# query database
# 'rowid' is the default primary key
# c.execute("SELECT rowid, * FROM customers")

# helper function to print all items (formatted)
def print_fetch(prompt, items):
    print("\n", prompt)
    for item in items:
        print(f"{item[0]} {item[1]} \t({item[2]})")

# original records
c.execute("SELECT * FROM customers")
print_fetch("Current Records:", c.fetchall())

# update records
# update and delete records using rowid's
c.execute("""UPDATE customers SET first_name = "Rizzy"
            WHERE rowid = "1"
    """)
# delete records
c.execute("DELETE FROM customers WHERE rowid = 2")

c.execute("SELECT * FROM customers")
print_fetch("Updated Records:", c.fetchall())


# query specific item
c.execute("SELECT * FROM customers WHERE last_name = 'Hoque'")
print_fetch("Last Names with \"Hoque\":", c.fetchall())
c.execute("SELECT * FROM customers WHERE age < 20")
print_fetch("Ages < 20:", c.fetchall())
c.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com'")
print_fetch("Employees with gmails:", c.fetchall())

# order results
c.execute("SELECT * FROM customers ORDER BY last_name")
print_fetch("Order by last name:", c.fetchall())

# commit the connection 
connect.commit()

# close the connection
connect.close()
