<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
    <!-- This returns the QueryString and sets the body color -->
    body{
        background-color: <%=Request.QueryString("Colour")%>;
        text-align: center;
        font-size: 16px;
    }
</style>
</head>
<body>
<h1>Part 1</h1>
<%
'cookie  variable declaration'
dim timeCookie
'response cookies sets the cookie expiration'
response.cookies("NumVisits").Expires=date+365
'request gets the numvisits cookie if it exits'
timeCookie=request.cookies("NumVisits")
'if the timeCookie has null variable then it goes into this case'
if timeCookie="" then
   'response sets the cookie visit time'
   response.cookies("NumVisits")=time()
   'this writes the greeting message for the first time visitor'
   response.write("First time visit")
else
    'otherwise it sets the new cookie to the current time and returns the previous cookie time'
   response.cookies("NumVisits")=time()
   response.write("Last visit was = " & timeCookie & "!")
end if
%>
</body>
</html>