#!/usr/bin/env python   
import cgi
form= cgi.FieldStorage()
val1=form.getvalue("name")
val2=form.getvalue("family")
print "Content-type:text/html"
print
print "Your name is: "
print val1, val2
print "<br/>"
print """

<form method="post" action="form.py">
birthdate: <input type="text" name="birthdate"><br>
main hobby: <input type="text" name="hobby"><br>
<br/>
<input type="submit" value="Submit">
</form>"""
