#!/usr/bin/ruby -w

require 'cgi'
cgi = CGI.new

print "Content-type: text/html\n\n"
#Used the cgi to retrieve the variables from the form and assigned to non-constant variables
city = cgi['Citname']
province = cgi['Pname']
country = cgi['Conname']
population = cgi['Pop']
imglink = cgi['Pict']

puts "<html><head>"
puts "<title>Lab 6</title>"
puts "</head>"
#Use the image url to create the background for the website alongside inline css style
puts "<body style = \"text-align:center;background-size: cover;background-position: center;height:100%;background-image: url('"+imglink+"');\">"
#Use capitalize() to make the first character upper case
puts "<p style=\"color: blue; font-size: 40px; white-space: nowrap;\"> "+city.capitalize()+", "+country.capitalize()+"</p>"
puts "<div style=\"height: auto;width: 200px;margin: 10px auto;background: rgba(76, 175, 80, 0.5);padding: 1px; \">"
puts "<p style=\"color: red; font-size: 14px;\"> "+"Province = "+province.capitalize()+"</p>"
puts "<p style=\"color: red; font-size: 14px;\"> "+"Population = "+population+"</p>"
puts "</div>"
puts "</body>"
puts "</html>"