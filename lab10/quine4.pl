#!/usr/bin/perl
$b="\\";
$n="\n";
$q="\"";
$s="#!/usr/bin/perl%s$b="\\";%s\$n=%s\\n%s;%s\$q=%s\\%s%s;%s\$s=%s%s%s;%s printf \$s,\$n,\$q,\$q,\$n,\$q,\$q,\$q,\$n,\$q,\$s,\$q,\$n,\$n;%s";
 printf $s,$n,$q,$q,$n,$q,$q,$q,$n,$q,$s,$q,$n,$n;
