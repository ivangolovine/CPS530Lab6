#!/usr/bin/python
print("Content-type: text/html\n\n")
import cgi

form=cgi.FieldStorage()
#Retrieves the form elements and makes them upper case
city=form.getvalue('Citname').upper()
province=form.getvalue('Pname').upper()
country=form.getvalue('Conname').upper()
population=form.getvalue('Pop')
imglink=form.getvalue('Pict')


print("<html><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><head></head>")
print("<body style=\"margin-left:auto;margin-right:auto;text-align:center;border:10px solid blue;width:80%;\">")
print("<div style=\"background-size: cover; height: 100%; width:100%; background-position: center;background-repeat: no-repeat;background-image: url('"+imglink+"');\">") #prints the image
print('<header style="width: fit-content;font-size:3em;color:#cc0000;display: inline-flex;background-color:powderblue;background-size:80%;">'+city+" "+country+'</header>') #printing title
print("<br>")
print('<p>'+"Province = "+province+'</p>')
print('<p>'+"Population = "+population+'</p>')
print("</div>")
print("</body></html>")
