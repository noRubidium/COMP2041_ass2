#!/usr/bin/perl -w
sub isPrime($){
	my $first = $_[0];
	$count=0;
	foreach $char (split("",$first)){
		if($char eq "1"){
			$count ++;
		}
	}
	if($count == 1 || $count == 2 ){
		return 0;
	}
	foreach $i (2..$count-1){
		if($count % $i == 0){
			return 1;
		}
	}
	return 0;
}


foreach $n (1..100) {
    $unary = 1 x $n;
    print "$n = $unary unary - ";
    if ($unary =~ &isPrime($unary)) {
        print "composite\n"
    } else {
        print "prime\n";
    }
}

