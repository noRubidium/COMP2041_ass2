#!/usr/bin/perl -w

print "Username: ";
$username = <STDIN>;
chomp $username;
print "password: ";
$password = <STDIN>;
chomp $password;

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
}

