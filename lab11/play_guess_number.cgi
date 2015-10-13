#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

$max_number_to_guess = 99;

print <<eof;
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
    <title>A Guessing Game Player</title>
    <link href="guess_number.css" rel="stylesheet">
</head>
<body>
eof

warningsToBrowser(1);
if(defined param("correct")){
	print <<eof;
	
	    <form method="POST" action="">
		<p>I win!!!!</p>
	       <input type="submit" value="Play Again">
	    </form>
	</body>
	</html>
eof
}else{
	if(defined param("higher")){
		$higher = param("high_limit");
		$lower = param("guess") +1;
		$guess = int(($higher + $lower) / 2);
	}elsif(defined param("lower")){
		$higher = param("guess") - 1;
		$lower = param("low_limit");
		$guess = int(($higher + $lower) / 2);
	}else{
		$higher = 100;
		$lower = 1;
		$guess = 50;
	}
	print <<eof;
	    <form method="POST" action="">
		<p>My guess is: $guess</p>
		<input type="submit" name="higher" value="Higher?">
		<input type="submit" name="correct" value="Correct?">
		<input type="submit" name="lower" value="Lower?">
		<input type="hidden" name="low_limit" value="$lower">
		<input type="hidden" name="high_limit" value="$higher">
		<input type="hidden" name="guess" value="$guess">
	    </form>
	</body>
	</html>
eof
}
