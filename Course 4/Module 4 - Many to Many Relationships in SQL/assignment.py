import json
import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Set up the tables
# Note: We added the 'role' column to the Member table definition
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Prompt for file name
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# Open and load the JSON data
# Format is a list of lists: [ ["Name", "Course", role_int], ... ]
try:
    str_data = open(fname).read()
    json_data = json.loads(str_data)
except:
    print("File not found or invalid JSON")
    quit()

for entry in json_data:
    # The JSON data has 3 parts: Name, Course Title, Role
    name = entry[0]
    title = entry[1]
    role = entry[2] # <--- This is the key modification required for the assignment

    # 1. Insert/Get User ID
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES ( ? )', (name, ))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    # 2. Insert/Get Course ID
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES ( ? )', (title, ))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    # 3. Insert Member with Role
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        (user_id, course_id, role))

# Commit changes to the database
conn.commit()

print("Database populated successfully.")

# --- AUTOMATIC ANSWER GENERATION ---
# The code below runs the exact query asked in the assignment to generate the answer key.

sql_query = '''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
'''

cur.execute(sql_query)
result = cur.fetchone()

print("\n--- RESULT ---")
if result:
    print("Enter this code into the assignment box:")
    print(result[0])
else:
    print("Could not generate result. Check your JSON file.")

cur.close()