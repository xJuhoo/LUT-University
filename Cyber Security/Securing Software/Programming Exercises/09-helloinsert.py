# create_test_db.py
import sqlite3
	import os
	 
	# Creates agents.sqlite
	# TMC has issues with binary files, so we will go around by creating it locally from the text dump.
	 
	db = \
	"""
	PRAGMA foreign_keys=OFF;
	BEGIN TRANSACTION;
	CREATE TABLE Agent (
	    id varchar(9) PRIMARY KEY,
	    name varchar(200)
	);
	INSERT INTO Agent VALUES('Secret','Clank');
	INSERT INTO Agent VALUES('Gecko','Gex');
	INSERT INTO Agent VALUES('Robocod','James Pond');
	INSERT INTO Agent VALUES('Fox','Sasha Nein');
	INSERT INTO Agent VALUES('Riddle','Voldemort');
	COMMIT;
	"""
	 
	if os.path.exists('agents.sqlite'):
		print('agents.sqlite already exists')
	else:
		conn = sqlite3.connect('agents.sqlite')
		conn.cursor().executescript(db)
		conn.commit()



# hellodatabase.py
#!/usr/bin/env python3
	import sys
	import sqlite3
	 
	 
	def add_agent(conn, aid, name):
		c = conn.cursor()
		c.execute('INSERT INTO Agent VALUES (?, ?)', (aid, name))
		conn.commit()
	 
	def delete_agent(conn, aid):
		c = conn.cursor()
		c.execute('DELETE FROM Agent WHERE id = ?', (aid,))
		conn.commit()
	 
	def read_database(conn):
		agents = []
	 
		c = conn.cursor()
		c.execute('SELECT id, name FROM Agent ORDER BY id ASC')
		agents = c.fetchall()
		print(agents)
	 
		return agents
	 
	 
	def main(argv):
		name = sys.argv[1]
		conn = sqlite3.connect(name)
		while True:
			agents = read_database(conn)
			print('\nActive agents:\n')
			for agent in agents:
				print(agent[0], agent[1])
			print()
			command = input('What would you like to do: [a]dd, [r]emove, or [q]uit? ')
	 
			if command[0].startswith('a'):
				aid = input('id? ')
				name = input('name? ')
				add_agent(conn, aid, name)
				pass
			elif command[0].startswith('r'):
				aid = input('id? ')
				delete_agent(conn, aid)
				pass
			elif command[0].startswith('q'):
				break
		
	 
	# This makes sure the main function is not called immediatedly
	# when TMC imports this module
	if __name__ == "__main__": 
		if len(sys.argv) != 2:
			print('usage: python %s database' % sys.argv[0])
		else:
			main(sys.argv)
