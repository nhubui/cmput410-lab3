#!/usr/bin/env python   
import cgi
form= cgi.FieldStorage()
val1=form.getvalue("birthdate")
val2=form.getvalue("hobby")
print "Content-type:text/html"
print
print "Your Birthday is :"
print val1 
print "<br/>"
print "Your Hoppy is :"
print val2
print """

<form method="post" action="test_form.py">
First name: <input type="text" name="name"><br>
Last name: <input type="text" name="family"><br>
<br/>
<input type="submit" value="Submit">
</form>"""
