<html>
<head>
<title>hola mundo</title>
</head>
<body>
<p>
	Welcome, {{username}}!
	
	<ul>
		%for thing in things:
		<li>{{thing}}</li>
		%end
	</ul>
	
	<p>
	<form action='/favorite_sport' method='post'>
	Favorite sport: 
	<input name='sport'><br>
	<input type='submit'>
	</form>
	
</body>
</html>