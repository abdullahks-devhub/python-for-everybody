import sqlite3

# Connect to the database (this will create the file 'emaildb.sqlite')
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Reset the table to ensure a clean run
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Ask for the file name
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

# Loop through the file
for line in fh:
    # Find lines that start with 'From: '
    if not line.startswith('From: '): continue
    
    # Extract the email address
    pieces = line.split()
    email = pieces[1]
    
    # Extract the organization (domain) from the email
    # We split the email string by the '@' character and take the second part
    parts = email.split('@')
    org = parts[1]
    
    # Database logic to update counts
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        # If the org isn't in the DB yet, insert it with count 1
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        # If it is in the DB, add 1 to the existing count
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

# Commit the changes to the database
conn.commit()

# Verify the result by printing the top 10
# The assignment hint says the top count should be 536
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
print("Counts:")
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()