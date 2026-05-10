import sqlite3

# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make sure we start with a fresh database by removing old tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Prompt for file name (default to tracks.csv)
fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'tracks/tracks.csv'

# Open the CSV file
fh = open(fname)

# Loop through every line in the file
for line in fh:
    line = line.strip()
    pieces = line.split(',')
    
    # Skip lines that don't have enough data
    if len(pieces) < 7 : continue

    # Parse the CSV line based on the standard format:
    # Name, Artist, Album, Count, Rating, Length, Genre
    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    # 1. Insert Artist
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES ( ? )', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', ( artist, ) )
    artist_id = cur.fetchone()[0]

    # 2. Insert Genre
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES ( ? )', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', ( genre, ) )
    genre_id = cur.fetchone()[0]

    # 3. Insert Album (linking it to the Artist)
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', ( album, ) )
    album_id = cur.fetchone()[0]

    # 4. Insert Track (linking it to Album and Genre)
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

# Commit changes to the database
conn.commit()
print("Database 'trackdb.sqlite' generated successfully.")
cur.close()