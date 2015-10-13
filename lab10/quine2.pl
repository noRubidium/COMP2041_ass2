#!/usr/bin/perl
$s="#!/usr/bin/perl\n$s=\'\%s\';\n$s=~s/\%s/$s/;\nprintf $s,$s;\n";
$s=~s/\%s/$s/;
printf $s,$s;
