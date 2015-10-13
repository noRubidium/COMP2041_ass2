#!/usr/bin/perl
#This is written by Minjie Shen as a lab excercise
#Verifying the credit card number
use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

	print header, start_html("Credit Card Validation"), "\n";
	warningsToBrowser(1);
	$credit_card = param("credit_card");
	print h2("Credit Card Validation");
if (defined param("Close")){
	print "Thank you for using the Credit Card Validator.\n";
}else{
	print "This page checks whether a potential credit card number satisfies the Luhn Formula.\n";
	print start_form;
	if (defined param("Reset")){
		print textfield({-name=>'credit_card'});
	}elsif (defined $credit_card) {
	    print validate($credit_card)."\n";
	    print textfield({-name=>'credit_card',-value=>$credit_card})."\n";
	}else{
		print textfield({-name=>'credit_card'});
	}
	print submit("Validate")."\n";
	print reset("Reset")."\n";
	print submit("Close")."\n";
	print end_form;
}
print end_html;
exit 0;


sub validate{
	$number = $_[0];
	$var = $number;
	$var =~ s/[^0-9]//g;
	@num_set = split //,$var;
	if ($#num_set != 15){
		return p(b(span({-style=>'color: red'},$number.' is invalid  - does not contain exactly 16 digits'))).'Try again:';
	}elsif(luhn_checksum(@num_set) % 10 == 0){
		#print luhn_checksum(@num_set);
		return $number." is valid\n".p;
	}else{
		return p(b(span({-style=>'color: red'},$number." is invalid\n")))."Try again:";
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
