#!/usr/bin/perl -w

# written by andrewt@cse.unsw.edu.au September 2015
# as a starting point for COMP2041/9041 assignment 2
# http://cgi.cse.unsw.edu.au/~cs2041/assignments/bitter/

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use Data::Dumper;  
use List::Util qw/min max/;
warningsToBrowser(1);

# print start of HTML ASAP to assist debugging if there is an error in the script
print page_header();

# some globals used through the script
$debug = 1;
$dataset_size = "medium"; 
$users_dir = "dataset-$dataset_size/users";

print browse_screen();
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

#
# HTML placed at bottom of every screen
#
sub page_header {
    return header,
        start_html("-title"=>"Bitter", -bgcolor=>"#FEDCBA"),
        center(h2(i("Bitter")));
}

#
# HTML placed at bottom of every screen
# It includes all supplied parameter values as a HTML comment
# if global variable $debug is set
#
sub page_trailer {
    my $html = "";
    $html .= join("", map("<!-- $_=".param($_)." -->\n", param())) if $debug;
    $html .= end_html;
    return $html;
}
