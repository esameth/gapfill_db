#!/usr/bin/python


# import required packages
import pymysql
import cgi
import cgitb
cgitb.enable()

print("Content-type: text/html\n")
print("<html><head>")
handler=open("./css/style.css")
print("<style>")
for style in handler:
	print (style)
handler.close()
print("</style>")

#print("<link rel='stylesheet' type='Text/css' href='https://drive.google.com/file/d/1dFjr-z6zSCIBUYYXz2nJBlqmIQm33Ytb'>")
def trim_link(var):
    var=str(var)
    var2=var.split(":")
    var2.pop(0)
    var=":".join(var2)
    return (var)

print("	<title>Final Semester Project</title>")
print("	</head>")
	
print("	<body>")
 
print('''
		<div id="main" >
			<div id="mainheader" class="maindiv">
				<ul id="nav" class="navitem">
					<li><a href="./homepage.py"><label>Home</label></a></li>
					<li><a href="./do_fba.py"><label>Run FBA</label></a></li>-->
					<li><a href="how_to_do.py"><label>How To</label></a></li>
					<li><a href="frequently_asked.py"> <label>FAQ </label></a></li>
				</ul>
				
				<form action="" method="post" id="searchform" class="navitem">
				<input type="text" name="search" value=""/>
				<input type="submit" value="search" id="searchbtn">
				</form>
			
			</div>
			<div id="mainmid" class="maindiv">
				<h2>MMNSG Database</h2>
				<hr></hr>''')
				
print('''	<div id="midh1search">

			
				</div>
				<hr></hr> 
        ''')
print("<div id='result'>")

form=cgi.FieldStorage()


if(form.getvalue("media_id")):
	media_id=form.getvalue("media_id")
#records=cursor.fetchall()
	queryz="""SELECT compound, description, name FROM Media WHERE Media_ID = %s """ 
	connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
	
	with connection.cursor() as cursor:
		cursor.execute(queryz,(media_id))
		results=cursor.fetchall()
		if(results):
			print("<h1>%s</h1>" % results[0][1])
			#print("<p></p>")#just for sapce                                   
			for row in results:
				print("<div class='medium_boxes'>")
				print("<p><strong>compound name:</strong> %s</p>"%(row[2]))
				print("<p><strong>compound shortname:</strong> %s</p>"%(row[0]))
				print("</div>")#just 
		else:
			print("Query failed")                                 
			print("<p class='search_message_paragraph'>Will check up soon<p>")
            
	cursor.close()
	connection.close()
 
##elif(explore=="Metabolite"):

print("<p></p>")
print("</div>") 
  

print("</div>")       
        
        
        
print('''	<div id="midh2search">
					<div  id="viewmetabolites" class="navlink">
						<a class="clickme" href="homepage.py"><label>To Home</label></a>
					
					</div>
					<div id="viewmodel" class="navlink">
					<a class="clickme" href="search_page.py"><label>To Search Page</label></a>
					</div>
					<div id="viewreactions" class="navlink">
					<a class="clickme" href="frequently_asked.py"><label>To Help Page</label></a>
					</div>
				</div>
				
				
			</div> ''')
print('''<div id="mainfooter_fba" class="maindiv">
			<p>Boston University &copy; 2021</p>
			</div>
		</div> ''')
   
print("</body>")
print("</html>")


