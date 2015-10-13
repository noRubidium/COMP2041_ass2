#!/usr/bin/perl
$d="\$";
$b="\\";
$n="\n";
$q="\"";
$s="#!/usr/bin/perl%s\$b=%s%s%s%s;%s\$b=%s%s%s%s;%s\$n=%s%sn%s;%s\$q=%s%s%s%s;%s\$s=%s%s%s;%s printf \$s,\$n,\$q,\$b,\$b,\$q,\$n,\$q,\$b,\$q,\$n,\$q,\$q,\$b,\$q,\$n,\$q,\$s,\$q,\$n,\$n;%s";
 printf $s,$n,$q,$b,$b,$q,$n,$q,$b,$q,$n,$q,$q,$b,$q,$n,$q,$s,$q,$n,$n;
