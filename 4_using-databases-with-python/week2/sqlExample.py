import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open("../../txt/"+fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # Replace the ? with the tuple
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    # Get the first value
    row = cur.fetchone()
    if row is None:
        # Replace the ? with the tuple an set the count column with 1 for that new row
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        # Update the row: Update the count column for the row that already exist
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    # https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html
    # It is recommended to commit every 10 records because this take time. In this case we are doing this for each record
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the connection
cur.close()
