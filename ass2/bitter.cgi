#!/usr/bin/perl -w

# written by andrewt@cse.unsw.edu.au September 2015
# as a starting point for COMP2041/9041 assignment 2
# http://cgi.cse.unsw.edu.au/~cs2041/assignments/bitter/

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use Data::Dumper;  
use List::Util qw/min max/;
use POSIX qw(strftime);
use Class::struct;

struct(user =>{
    username => '$',
    full_name => '$',
    email => '$',
    listens => '@',
    home_longtitude => '$',
    home_altitude =>'$',
    home_suburb =>'$',
    password =>'$',
    bleats =>'@'
});
warningsToBrowser(1);
# print start of HTML ASAP to assist debugging if there is an error in the script
if(! defined param('username') && ! defined param('password')){
    
}
print page_header();
#
# some globals used through the script
$debug = 1;
$dataset_size = "medium"; 
$users_dir = "dataset-$dataset_size/users";
$bleats_dir = "dataset-$dataset_size/bleats";
$form_start=start_form;
$form_end = end_form."\n";
$html_base = "";
#print browse_screen();
print user_display();
print page_trailer();
exit 0; 

sub browse_screen {
    my $n = param('n') || 0;
    my @users = glob("$users_dir/*");
    $n = min(max($n, 0), $#users);
    param('n', $n + 1);
    my $user_to_show  = $users[$n];
    my $details_filename = "$user_to_show/details.txt";
    open my $p, "$details_filename" or die "can not open $details_filename: $!";
    $details = join '', <$p>;
    close $p;
    
    return p,
        start_form, "\n",
        pre($details),"\n",
        hidden('n', $n + 1),"\n",
        submit('Next user'),"\n",
        end_form, "\n",
        p, "\n";
}
sub list_user {
    my @users = glob("$users_dir/*");
    foreach my $user ()
}
#
# HTML placed at bottom of every screen
#
sub page_header {
    open F,"<",$html_base."header.html" or die "file open failed";
    my @header=<F>;
    close F;
    my $header = join("",@header);
    my $log_sub = "";
    if($logged_in == 1){
    	open F,"<",$html_base."loggedin.html" or die "file open failed";
    }else{
    	open F,"<",$html_base."notin.html" or die "file open failed";
    }
    my @string = <F>;
    close F;
    $log_sub = join("",@string);
    $header =~ s/\%\%user_login\%\%/$log_sub/g;
    return header,
        $header;
}

#
# HTML placed at bottom of every screen
# It includes all supplied parameter values as a HTML comment
# if global variable $debug is set
#
sub page_trailer {
    my $html = "";
    $html .= join("", map("<!-- $_=".param($_)." -->\n", param())) if $debug;
    open F,"<",$html_base."footer.html" or die "file open failed";
    my @footer=<F>;
    close F;
    $html .= join("",@footer);
    return $html;
}
sub user_display {
    my $n = param('n') || 0;
    my @users = glob("$users_dir/*");

    if(defined param("Prev_user")){
    	$n--;
    }elsif(defined param("Next_user")){
    	$n++;
    }
    $n = min(max($n, 0), $#users);
    param('n', $n);
    my $hidden = hidden('n', $n);
    
    #determin which user to show and open the corresponding file
    my $user_to_show  = $users[$n];
    my $details_filename = "$user_to_show/details.txt";
    open my $p, "$details_filename" or die "can not open $details_filename: $!";
    $details = join '', <$p>;
    close $p;
    #open user_display.html
    open F,"<",$html_base."user_display.html" or die "can't open user_display.html $!";
    my $user_display = join '', <F>;
    close F;
    (my $info_panel,my $listening) = info_panel($user_to_show,$details,$hidden);
    $user_display =~ s/\%\%info_panel\%\%/$info_panel/;


    #Add listening panel
    my $listen_Panel = "";
    foreach my $listen ($listening =~ /\S+/g){
    	$listen_Panel .=$form_start;
    	$listen_Panel .=hidden('user_ID', $listen);
    	$listen_Panel .=submit(-name =>'Prev_user', -class =>"list-group-item",-value=>$listen,-width=>"200px");
    	$listen_Panel .=$form_end;
    }
    $user_display =~ s/\%\%listening\%\%/$listen_Panel/g;
    #Add recent bleats
    my $bleats=bleat_display($user_to_show);
    $user_display =~ s/\%\%bleats_display\%\%/$bleats/g;
    return p,
        $user_display,
        p, "\n";
}

#display the bleat in the given panel
sub bleat_display{
	my $user_to_show=$_[0];
	my $bleats_file_list = "$user_to_show/bleats.txt";
	open F,"<",$bleats_file_list or die "Fail to open $bleats_file_list: $!";
	my $result = "";
	open G,"<",$html_base."single_bleat.html" or die "Fail to open single_bleat.html: $!";
	my $tmp = join "",<G>;
	close G;
	while(my $line = <F>){
		chomp $line;
		open G,"<","$bleats_dir/$line" or die "Fail to open $bleats_dir/$line.txt: $!";
		my @lines = <G>;
		my $tmpcp = $tmp;
		foreach my $l (@lines){
			if($l =~/([^\s:]+):[\s]*(.+)/){
				(my $flag,my $sub) = ($l =~/([^\s:]+):[\s]*(.+)/);
				my $str="";
				if($flag =~ /time/){
					$sub = strftime("%a %b %e %H:%M:%S %Y",localtime($sub));
				}
				$tmpcp =~ s/\%\%$flag\%\%/$sub/;
			}
		}
		$result.= $tmpcp;
		close G;
	}
	$result =~ s/\%\%[^\%\n]*\%\%[\s\t]*\n*//g;
	return $result;
}
#given personal detail return a full personal info panel & $listening
sub info_panel{
    (my $user_to_show,my $details,my $hidden)=@_;
    my $user_name = "";
    #derive username
    if($details =~ /username:[\s]*([^\n]*)\n/){
    	$user_name = $1;
    	$details =~ s/username:[\s]*([^\n]*)\n//;
    	$details =~ s/password:[\s]*([^\n]*)\n//;
    	$details =~ s/email:[\s]*([^\n]*)\n//;
    }
    #derive listening
    my $listening = "";
    if($details =~ /listens:[\s]*([^\n]*)\n/){
    	$listening = $1;
    	$details =~ s/listens:[\s]*([^\n]*)\n//;
    }
    
    #open user_display.html
    open F,"<",$html_base."info_panel.html" or die "can't open user_display.html $!";
    my $user_display = join '', <F>;
    close F;
    $user_display =~ s/\%\%user_name\%\%/$user_name/g;
    $user_display =~ s/\%\%user_detail\%\%/$details/g;
    
    #if picture exists change the default.jpg
    if (-e "$user_to_show/profile.jpg"){
    	$user_display =~ s/default\.jpg/$user_to_show\/profile\.jpg/;
    }
    
    #Add prev user and next user
    $user_display =~ s/\%\%form_start\%\%/$form_start\n/;
    my $submit = submit(-name =>'Prev_user', -class =>"btn btn-primary",-value=>"Prev User");
    $user_display =~ s/\%\%prev_user\%\%/$submit/;
    $submit = submit(-name =>'Next_user', -class =>"btn btn-primary",-value=>"Next User");
    $user_display =~ s/\%\%next_user\%\%/$submit/;
    
    $user_display =~ s/\%\%hidden_field\%\%/$hidden/g;
    return ($user_display,$listening);
}
