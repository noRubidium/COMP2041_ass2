<html lang="en">
<head><title>Assignment 2 - Bitter</title>
<link href="../../2041.css" rel="stylesheet">
</head>
<body>
<div class="container">
<div class="page-header">
<h1>Assignment 2 - Bitter</h1>
</div>

<h2>Aims</h2>

<p>
This assignment aims to give you:
<ul>
<li> experience in constructing a CGI script and Perl/Python programming generally,
<li> practice in producing a complete CGI-based web site,
<li> and an introduction to the issues involved in programming for the web.
</ul>
<b>Note:</b> the material in the lecture notes will not be sufficient
by itself to allow you to complete this assignment.
You may need to search on-line documentation for CGI, Perl/Python etc.
Being able to search documentation efficiently for the information you need is a
<em>very</em> useful skill for any kind of computing work.

<h2>Introduction</h2>

Andrew has noticed students are often complaining about COMP[29]041.  Rather than address their
complaints and improve COMP2041, Andrew has decided he will make himself rich exploiting COMP[29]041 coding skills and then give up lecturing.
Andrew's plan is to have COMP[29]041 students create a social media platform called <i>Bitter</i> for complaints.
Andrew believes the absence of any similar existing social media platform means <i>Bitter</i> will become very popular and he will become rich
<p>
Users using <i>Bitter</i> send short messages called <b><i>bleats</i></b>.
Bleats can have at most maximum 142 characters.
<p>
<i>Bitter</i> users can indicate particular users they are interested in and whose bleats they wish to regularly see - this is termed <i>listening</i> to the user.
<p>
Your task is to produce a CGI script <code>bitter.cgi</code> which provides the core features of <i>Bitter</i>.
<p>
In other words your task is to implement a simple but fully functional social web site.
<p>
But don't panic, the assessment for this assignment (see below) will allow you to obtain
a reasonable mark if you successfully complete some basic features.

<h2>Data Sets</h2>

You have been provided with 4 synthetic datasets containing the details of <i>Bitter</i> users & their bleats:
<ul>
<li> <a href="dataset-small">small</a> (<a href="dataset-small.zip">zip</a>) - 4 users, 42 bleats
<li> <a href="dataset-medium">medium</a> (<a href="dataset-medium.zip">zip</a>) - 42 users, 1022 bleats
<li> <a href="dataset-large">large</a> (<a href="dataset-large.zip">zip</a>)  - 420 users,  10232 bleats
<li> <a href="dataset-large">huge</a> (<a href="dataset-huge.zip">zip</a>) - 1753 users, 131072 bleats
</ul>
<p>
I expect most people will work with <i>medium</i> or <i>large</i> datasets.
During debugging you may find the <i>small</i> dataset useful.
Students may wish to use the <i>huge</i> dataset to demonstrate subset 4 features.
<p>
The information for each user is in a separate directory named with their user name
For example in the <i>medium</i> dataset there is a <i>Bitter</i> user James Franco.
James has chosen the username <i>James41</i> so his information is in the directory:
<a href="dataset-medium/users/James41/"><code>dataset-medium/users/James41/</code></a>
<p>
Each  <i>Bitter</i> user's directory contains a file named <code>details.txt</code> containing
relevant information that the <i>Bitter</i> user has supplied.
<p>
For example <a href="dataset-medium/users/James41/details.txt"><code>dataset-medium/users/James41/details.txt</code></a>
contains James's details:
<p>
<pre class="program">
email: J.Franco@unsw.edu.au
home_latitude: -34.1041
username: James41
listens: JuliannaWoman78 CarmenTiger CrazyCarlos79 AwesomeVitali NerdyAnimal03 FunnyGeek53 PiotrMan68 SherylAngel JuanPabloMontoya BrainyStar69 PamelaAnderson
home_longitude: 150.8058
password: yankees
full_name: James Franco
home_suburb: St Helens Park
</pre>
<p>
Note James has supplied the suburb where he lives and the coordinates of his home address.
Notice also the usernames of the  <i>Bitter</i> users James listens to.
<p>
Most <i>Bitter</i> users will also have an image  present in the same directory named <code>profile.jpg</code>.
For example <a href="dataset-medium/users/James41/profile.jpg"><code>dataset-medium/users/James41/profile.jpg</code></a>
contains James's image.
<p>
<img src="http://www.cse.unsw.edu.au/~cs2041/assignments/bitter/dataset-medium/users/James41/profile.jpg">
<p>
Note some details may be missing for some <i>Bitter</i> users.
This is deliberate, it indicates the <i>Bitter</i> user has chosen not to supply this information
and your web site should handle this sensibly. Also images might not be present for all users.
Again your web site should handle this sensibly.
<p>
Also present in a <i>Bitter</i> users's directory will be a file named <code>bleats.txt</code> containing numbers which uniquely identify a bleat the <i>Bitter</i> user has sent.
<p>
For example <a href="dataset-medium/users/James41/bleats.txt"><code>dataset-medium/users/James41/bleats.txt</code></a> contains

<pre class="program">
2041906566
2041906785
2041907501
2041918917
2041919141
2041919353
2041919355
2041924552
....
</pre>

The bleats from all <i>Bitter</i> users can be found in the directory <a href="dataset-medium/bleats/"><code>dataset-medium/bleats/</code></a>
The first bleat James sent has identifying number 2041906566 so it will be found in
<a href="dataset-medium/bleats/2041906566"><code>dataset-medium/bleats/2041906566</code></a>

<pre class="program">
latitude: -33.9079
time: 1444180746
in_reply_to: 2041904922
longitude: 151.2263
bleat: @PamelaAnderson is in the bathroom and i have to pee!
username: James41
</pre>

Note the details include the time and location the bleat was sent.
The time is in seconds since Jan 1 1970.
Not all bleats will include location details.
<p>
Note James mentions another <i>Bitter</i> user <i>PamelaAnderson</i> using the <i>Bitter</i> convention of marking usernames in bleats with an <code><b>@</b></code> character.  Another <i>Bitter</i> convention is denoting keywords with a <code><b>#</b></code> character.
<p>
Note this bleat is a response to a previous bleat. Its unique identifying number is given in the <i>in_reply_to</i> field.
<p>
You are free to modify the data set and the data format in any way you choose.
Your code should still assume  details may be absent from  <i>Bitter</i> user details & locations absent from <i>bleats</i> because <i>Bitter</i> users choose not to supply them.
<p>
While you do not have to use this format to store data but I expect most students
will do so and unless you are very confident it is recommended you do so.
<p>
If you use another data format
you should import the large or huge dataset into this format and have it available
when you demo your web site so searches can be conducted using a familiar set of <i>Bitter</i> users.
<p>
Before choosing to use a database to store <i>Bitter</i> user data,
note it can be tricky getting full-fledged database systems such as mysql set up on CSE systems
and Andrew (& tutors) won't be able to offer any help.
If you do choose to use a database sqlite is recommended because its embedded,
and hence much simpler to setup, but again Andrew (& tutors) won't be able to help.

<h2>Subsets</h2>

To assist you tackling the assignments requirements have been broken into several levels in
approximate order of difficulty.  You do not have to follow this implementation order but
unless you are confident I'd recommend following this order.

You will receive marks for whatever features you have working or partially working
 (regardless of subset & order).

<h4>Display User Information &amp; Bleats (Level 0)</h4>

The starting-point script you've been given (see below) displays user information
in raw form and does not display their image or bleats.
<p>
Your web site should display user information
in nicely formatted HTML with appropriate accompanying text.  It should
display the user's image if there is one.
<p>
E-mail and password should not be displayed (e-mail, password).
<p>
The user's bleats should be display in reverse chronological order.

<h4>Interface (Level 0) </h4>

Your web site must generate nicely formatted convenient-to-use web pages
including appropriate navigation facilities and instructions for naive users.
Although this is not a graphic design exercise you should produce pages with a common
and somewhat distinctive look-and-feel. You may find CSS useful for this.
<p>
As part of your personal design you may change the name of the website to something
other than  Bitter but the primary CGI script has to be <code>bitter.cgi</code>.

<h4>Logging In & Out (Level 1)</h4>

Users should have to login to use Bitter.
<p>
Their password should be checked when they attempt to log in.
<p>
Users should also be able to logout.

<h4>Search for Users By Username or Full Name (Level 1)</h4>

Your web site should provide searching for a username or full name containing a
specified substring.  Search results should include the matching username
and their full name You should be able to click through to see full user details
and their recent bleats.


<h4>Sending Bleats (Level 1)</h4>

Users should be able to send bleats.  Bleats should be limited to 142 characters.

<h4>Displaying Relevant Bleats (Level 2)</h4>

When a user logs in they should see their recent bleats, any bleats that mention
them and any bleats from users they are <i>listening</i> to, all combined
in reverse-chronological order.

<h4>Listening/Unlistening to Users (Level 2)</h4>

A user should be able to start or stop listening to any other user at appropriate
points, including when viewing their profile or bleats.

<h4>Searching Bleats (Level 2)</h4>

It should be possible to search for bleats containing particular words or
hash-tagged strings.s.

<h4>Replying to Bleat(Level 2) </h4>

When viewing a bleat, it should be possible to click on a link and create a bleat responding to that bleat.

<h4>Pagination of Bleats & Search Results (Level 3)</h4>

When searching for users or bleats and when viewing bleats
the users be shown the first <i>n</i> (e.g n == 16) results.
They should be able then view the next  <i>n</i> and the next <i>n</i> and so on.

<h4>Bleat responses (Level 3) </h4>

When viewing a bleat, it should be possible to click on a link to see any
responses to the bleat & responses to them and so on.

<h4>User Account Creation (Level 3) </h4>

Your web site should allow users to create accounts with a
user name, password and e-mail address.
You should only accept a restricted syntax (certain characters) for this username
and of course check
that an account for this user name does not exist already.
It should  be compulsory that a valid e-mail-address is associated with an account but
the e-mail address need not be a UNSW address.
<p>
You should confirm e-mail address are valid and owned by the <i>Bitter</i> user creating the account by
e-mailing them a link necessary to complete account creation.
<p>
I expect (and recommend) most students to use the data format of the data set
you've been supplied.  If so for a new user you would need create
a directory named with their username and then add a appropriate <code>details.txt</code>
containing their details.

<h4>Profile Text (Level 3) </h4>

A <i>Bitter</i> user should be able to add to some text to their details , probably
describing their interests, which is displayed with their user details.

<pre class="program">
<i>
My interests are long walks on the beach and Python programming.
I plan to use what I've learnt COMP2041 to cure the world of all known diseases.
</i>
</pre>

It should be possible to use some simple (safe) HTML
tags, and only these tags, in this text.

The data set you've been given doesn't any include any examples of such text.
<p>
You can choose to store this text in the <code>details.txt</code> file or elsewhere,

<h4>Password Recovery (Level 3)</h4>

Users should be able to recover/change lost passwords via having an  e-mail sent to them.

<h4>Uploading &amp; Deleting  Images (Level 3)</h4>

In addition to their profile image users should also be allowed to add a background image.

A user should be able to upload/change/delete both background & profile images.

The lecture CGI examples include one for uploading a file.

<h4>Editing Infortmation (Level 3) </h4>

A user should be able to edit all the elements of their information.
including details, preferences & description.


<h4>Deleting Bleats (Level 3) </h4>

A <i>Bitter</i> user should also be able to delete any of their bleats.

<h4>Suspending/Deleting Bitter Account (Level 3) </h4>

A <i>Bitter</i> user not currently interested in Bitter  should be able to suspend their
account. A suspended account is not visible to other users.
<p>
A <i>Bitter</i> user should also be able to delete their account completely.

<h4>Notifications (Level 3) </h4>

A user should be able to indicate they wish to be  notified by e-mail
in one of these events:

<ul>
<li> their username is mentioned in a bleat
<li> someone replies to one of their bleets
<li> they gain a new listener
</ul>


<h4>Bleets Attachment (Level 3) </h4>

A user should be able to attach 1 or more (say upto 4) images (or perhaps videos)
to a bleat.  These should be appropriately displayed when the bleat is viewed.

<h4>Advanced Features (Level 4) </h4>

If you wish to obtain over 90% you should consider providing adding  features beyond those above.
marks will be available for extra features.

<h2>Getting Started</h2>

Here is the <a href="bitter.cgi.txt">source</a> to a <a href="bitter.cgi">Perl script</a>
with crude partial implementation of Level 0.
You may chooseto use this script as a starting point for your assignment.
<p>
The same Perl but using <code>cgi.pm</code> shortcuts is also <a href="bitter.cgipm.cgi.txt">available</a>.
You may choose to start with instead this version if you prefer this style of coding.
<p>
A  Python version of the same code is also <a href="bitter.py.cgi.txt">available</a>.
You may choose to start with this code if you prefer to the the assignment in Python.
<p>
However you start the assignment, make sure you name your script <code>bitter.cgi</code>.
<p>
All the above CGI scripts refer to a CSS file named <a href="bitter.css">bitter.css</a>.
It contains some simple CSS you can use as a starting point, but don't spend  much time on CSS - almost all
the marks are for coding!
<p>
You should use the  gitlab.cse.unsw.edu.au repository you've been using for the lab CGI exercises for
this assignment.  You can do this be using the commands below.
<p>
<pre class="command_line">
<kbd class="shell">cd</kbd>
<kbd class="shell">mkdir -p public_html/ass2</kbd>
<kbd class="shell">priv webonly public_html/ass2</kbd>
<kbd class="shell">cd public_html/ass2</kbd>
<kbd class="shell">cp -p /home/cs2041/public_html/assignments/bitter/bitter.c?? .</kbd>
<kbd class="shell">unzip /home/cs2041/public_html/assignments/bitter/dataset-medium.zip</kbd>
....
<kbd class="shell">chmod 755 bitter.cgi</kbd>
<kbd class="shell">chmod 644 bitter.css</kbd>
<kbd class="shell">git add bitter.cgi bitter.css</kbd>
<kbd class="shell">echo '/dataset*' >.gitignore</kbd>
<kbd class="shell">git commit -a -m "Andrew's code"</kbd>
<kbd class="shell">git push</kbd>
....
<kbd class="shell">firefox http://cgi.cse.unsw.edu.au/~z5555555/ass2/bitter.cgi</kbd>
<kbd class="shell">vi bitter.cgi</kbd>
<kbd class="shell">vi diary.txt</kbd>
<kbd class="shell">git add diary.txt</kbd>
<kbd class="shell">git commit -a -m 'added code for basic formatting'</kbd>
<kbd class="shell">git push</kbd>
....
<kbd class="shell">....</kbd>
<kbd class="shell">....</kbd>
<kbd class="shell">....</kbd>
<kbd class="shell">git commit -a -m 'tidied up assignment for submission'</kbd>
<kbd class="shell">give cs2041 ass2 bitter.cgi diary.txtr</kbd>
<kbd class="shell">git push</kbd>
....
</pre>
<p>

<h2>Assumptions/Clarifications</h2>

It is a requirement of the assignment that when you work the assignment for
more than a few minutes you push the work to <code>gitlab.cse,unsw.edu</code> (see above).
<p>
I expect almost all students will use Perl to complete this assignment
but you are permitted to use Python.
<p>
You may use Javascript for part of the assignment.
A high mark for the assignment can be obtained without Javascript.
<p>
You may use any Perl or Python package which is installed on CSE's system.
<p>
You may use general purpose, publicly available (open source) Javascript libraries (e.g. JQuery)
,CSS (e.g.Bootstrap) or HTML - much sure use of other people's work is clearly acknowledged and distinguished
from your own work.
<p>
You can not otherwise use code written by another person.
<p>
You may submit multiple CGI files but the primary file must be named bitter.cgi
You may submit other files used by your CGI script(s).
<p>
If you submit an executable named <code>init</code>, it will be run once before before your
assignment, is in the same directory as your assignment.  This is provide the possibility of set up
code for complex assignments.  I expect only a few student will need this.
<p>
Make sure you submit all files and in the appropriate hierarchy.
If for example you do URL rewriting in a <code>.htaccess</code> file (I'm
not expecting or recommending this), make sure you submit the .htaccess file.
<p>
Your CGI script must run on CSE's system. It will be run from a class account so you
must submit all necessary files and do not hard code absolute URLs or pathnames in your code.
In other words don't put embed URLs like <code>http://www.cse.unsw.edu.au/~z5555555/ass2/subdir/background.html</code> in your code.  Use relative  URLs like  <code>"subdir/background.html"</code>. Similarly don't put absolute pathnames such as <code>/home/z5555555/public_html/ass2/subdir/datafile"</code>. Use relative pathname such as <code>"subdir/datafile"</code>
<p>
We will use firefox(iceweasel) on CSE lab machines for the demo session. Your code should
be sufficiently portable to work on with that version of firefox  but you will be allowed to demo on Chrome
instead but again on a CSE lab machine.
<p>
You should avoid running external programs (via system, subprocess, back quotes or open).
where an equivalent operation could be performed simply in Perl/Python.
You may be penalized in the handmarking if you do so.
<p>
You are permitted to run an external program to send e-mail, although this
is possible from Perl &amp; Python.
<p>
You are only required to provide basic security - using a hidden field
to store user's password in plaintext is OK. More sophisticated security may qualify as an
extra feature for subset 4.
<p>
You should follow  discussion about the assignment in the
<a href="https://piazza.com/class/ic8qe8kuhbp1ex">course forum</a>.
All questions about the assignment should be posted there unless they concern your private circumstances.
This allows all students to see all answers to questions.

<h2>Diary</h2>
You must keep a record of your work on this assignment as you did for assignment in an ASCII file
The entries should include date, starting&amp;finishing time, and a brief (one or two line) description of
the work carried out.
For example:
<p>
<table class="table table-bordered">
<tr><th>Date<th>Start<th>Stop<th>Activity<th>Comments
<tr><td>29/10<td>16:00<td>17:30<td>coding<td>implemented creation of user accounts
<tr><td>30/10<td>20:00<td>10:30<td>debugging<td>found bug in handling of hair colours
</table>
<p>
Include these notes in the files you submit as an ASCII file named diary.txt.
<p>
Some students choose to store this information in git commit messages
and use a script to generate  <code>diary.txt</code> from <code>git log</code> before they submit.
You are welcome to do this.

<h2>Assessment</h2>

Assignment 2 will contribute 15 marks to your final COMP2041/9041 mark
<p>
20% of the marks for assignment 2 1 will come from hand marking by
your tutor.  These marks will be awarded on the basis of clarity,
commenting, elegance and style.  In other words, your tutor will assess how
easy it is for a human to read and understand your program.
<P>
80% of the marks for assignment 2 will come from a peer assessment session where
your submitted CGI script is tested against a specified set of operations and assessed
by fellow students.
You will be present to assist in determining what features are and are not
working, you will also be able to indicate any extra features you have implemented.
Details of the peer assessment sessions will be announced in week 13.
<P>
Here is an indicative marking scheme .
<P>
<table  class="table table-bordered table-striped">
<tr><td align=right>100%<td>Elegant Perl/Python with an excellent implementation of levels 0-3 and
some optional (level 4) features
<tr><td align=right>90+%<td>Very well written Perl/Python which implements levels 0-3 successfully
<tr><td align=right>85%<td>Well written Perl/Python which implements most of levels 0-3 successfully
<tr><td align=right>75+%<td>Readable Perl/Python which implements of levels 0-2 successfully
<tr><td align=right>65%<td>Reasonably readable code which implements level 0-1 successfully
<tr><td align=right>55%<td>Reasonably readable code which implements level 0 successfully
<tr><td align=right>45%<td>Major progress on the assignment with some things working/almost working
<tr><td align=right>-70%<td>Knowingly supplying  work to any other person which is subsequently submitted by another student.
<tr><td>0 FL for COMP2041/9041<td>Submitting any other person's work with their consent.  This includes joint work.
<tr><td>academic misconduct<td>Submitting another person's work without their consent.
</table>

<h2>Originality of Work</h2>

The work you submit must be your own work.  Submission of work partially or completely derived
from any other person or jointly written with any other person is not permitted.
The penalties for such an offence may include negative marks,
automatic failure of the course and possibly other academic discipline.
Assignment submissions will be examined both automatically and manually
for such submissions.
<p>
Relevant scholarship authorities will be informed if students holding scholarships
are involved in an incident of plagiarism or other misconduct.
<p>
Do not provide or show your assignment work to any other person - apart from the teaching staff
of COMP2041/9041.
If you knowingly provide or show your assignment work to another person for any
reason, and work derived from it is submitted you may be penalized, even
if the work was submitted without your knowledge or consent.  This may
apply even if your work is submitted by a third party unknown to you.
<p>
Note, you will not be penalized if your work is
taken without your consent or knowledge.

<h2>Submission</h2>

This assignment is  due at 23:59pm Sunday October 25
Submit the assignment using this <I>give</I> command:


<pre class="command_line">
<kbd class="shell">give cs2041 ass2 bitter.cgi bitter.css diary.txt [files.tar] [any-other-files]</kbd>
</pre>
<p>
If you have need to submit many other files, files in a sub-directory or a
directory hierarchy, submit them as a tar file named files.tar.  For example
if you have subdirectories named <i>css</i>, <i>js</i> and <i>images</i>, this
will submit all the files in them (including directories they contain).

<pre class="command_line">
<kbd class="shell">tar zcf files.tar css js images</kbd>
<kbd class="shell">give cs2041 ass2 bitter.cgi diary.txt files.tar</kbd>
</pre>

If your assignment is submitted after this date, each hour it is late reduces
the maximum mark it can achieve by 2%.
For example if an assignment worth 76% was submitted
5 hours late, the late submission would have no effect.
If the same assignment was submitted 30 hours late it would be awarded
40%, the maximum mark it can achieve at that time.
<P>

<ul>
<li><small>Thu Sep 27 23:00 Version 0.1 - initial release</small>
<li><small>Wed Oct 07 19:00 Version 0.2 - starting point code updates</small>
<li><small>Thu Oct 08 11:00 Version 0.3 - late penalty modified</small>
</ul>

<p>
</div>
<script src ="../../2041.js"></script>
</body>
</html>
