#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

print header, start_html('Login');
warningsToBrowser(1);

$username = param('username') || '';
$password = param('password') || '';

if ($username && $password) {
	if(-d "../accounts/$username"){
		open F,"<","../accounts/$username/password" or die;
		$cPassWord = <F>;
		chomp $cPassWord;
		if($cPassWord eq $password){
			print "$username authenticated.\n";
		}else{
			print "Incorrect password! \n";
		}
	    
	}else{
		print " Unknown username! \n";
	}
} else {
    print start_form, "\n";
    print "Username:\n", textfield('username'), "\n";
    print "Password:\n", textfield('password'), "\n";
    print submit(value => Login), "\n";
    print end_form, "\n";
}
print end_html;
exit(0);

