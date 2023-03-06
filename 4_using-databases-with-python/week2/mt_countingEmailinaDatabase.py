import sqlite3

connection = sqlite3.connect("email2db.sqlite")
cur = connection.cursor()


cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("""CREATE TABLE Counts (org TEXT, count INTEGER)""")

fileName = input("Enter file name: ")
if(len(fileName) < 1): fileName = "mbox.txt"

fileHandle = open("../../txt/" + fileName)

for line in fileHandle:
  if not line.startswith("From: "): continue
  pieces= line.split()
  email = pieces[1]
  org = email.split("@")[1]
  
  # Replace the ? with the tuple
  cur.execute("SELECT count FROM Counts WHERE org = ? ", (org,))

  # Get the first value
  row = cur.fetchone()

  if row is None:
    # Replace the ? with the tuple an set the count column with 1 for that new row
    cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))

  else:
    # Update the row: Update the count column for the row that already exist
    cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

  # https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html
  # It is recommended to commit every 10 records because this take time. In this case we are doing this for each record
  connection.commit()

sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
  print("row:", row)
  print("org", row[0], "count", row[1], "\n")

# Close connection
cur.close()