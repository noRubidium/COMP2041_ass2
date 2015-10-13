#!/usr/bin/perl
#This is written by Minjie Shen as a lab excercise
#Verifying the credit card number

foreach $number_set (@ARGV){
	validate($number_set);
}

sub validate{
	$number = $_[0];
	$var = $number;
	$var =~ s/[^0-9]//g;
	@num_set = split //,$var;
	if ($#num_set != 15){
		print $number." is invalid  - does not contain exactly 16 digits\n";
	}elsif(luhn_checksum(@num_set) % 10 == 0){
		#print luhn_checksum(@num_set);
		print $number." is valid\n";
	}else{
		
		print $number." is invalid\n";
	}
}
sub luhn_checksum{
	@num_set = @_;
	$checksum = 0;
	#print $#num_set;
	foreach $i (0..$#num_set){
		$factor = (1+ $i) % 2 + 1;
		$d = ($num_set[$i] * $factor);
		if($d > 9){
			$d -= 9;
		}
		$checksum += $d;
	}
	return $checksum;
}