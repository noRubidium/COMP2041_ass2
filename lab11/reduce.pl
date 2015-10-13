#!/usr/bin/perl
sub reduce(&@){
	my ($sub,@list)=@_;
	$len = $#list;
	our $a = $list[0];
	foreach $i (0..$len -1){
		our $b = $list[$i+1];
		$a = &$sub;
	}
	return $a;
}

$sum = reduce { $a + $b } 1 .. 10;
$min = reduce { $a < $b ? $a : $b } 5..10;
$maxstr = reduce { $a gt $b ? $a : $b } 'aa'..'ee';
$concat = reduce { $a . $b } 'J'..'P';
$sep = '-';
$join = reduce { "$a$sep$b" }  'A'..'E';
print "$sum $min $maxstr $concat $join\n";
