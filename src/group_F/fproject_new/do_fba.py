#!/usr/local/Python-3.7/bin/python

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

print("<link rel='stylesheet' type='Text/css' href='https://drive.google.com/file/d/1dFjr-z6zSCIBUYYXz2nJBlqmIQm33Ytb'>")


print("	<title>Final Semester Project</title>")
print("	</head>")
	
print("	<body>") 
print('''<div id="main_fba" >''')
print('''	<div id="mainheader" class="maindiv">
				<ul id="nav" class="navitem">
					<li><a href="./homepage.py"><label>Home</label></a></li>
					<li><a href="./search_page.py"><label>Search</label></a></li>
					<li><a href="./how_to_do.py"><label>How To</label></a></li>
					<li><a href="./frequently_asked.py"> <label>FAQ </label></a></li>
				</ul>			
			</div>''')
print('''<div id="mainmid" class="maindiv" >''')

print('''				<h2>MMNSG Database</h2>
				<hr></hr>
				
				<div id="midfba1" class="mainfba_hori_div">
            <form action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_F/fproject_new/do_fba_s2.py"  method="post" id="run_fba_form" >
            
            <br>
            <label class="form_label_class" >Step 1: Choose Organism</label> <br></br>
                  
                   <select name="select_refseq" id="select_refseq">
                     <option value="">Choose Species</option>
                   ''')
query = "SELECT * FROM Genome;"
  
connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
  
with connection.cursor() as cursor:
	cursor.execute(query)
  
	records=cursor.fetchall()
	
	
for row in records:
	refseq=str(row[0])
	species=str(row[1])
	strain=str(row[2])
	#print("<p>refseq</p>")
	print("<option value=%s > %s %s </option>"%(refseq, species, strain))

cursor.close()
connection.close()

print("</select>")
print("<input type='text' id='input_genome' name='input_genome' class='input_item_x' Placeholder='Input your RefSeq here' />")
print('''                     
               
                <p><label class="form_label_class">Step 2: Choose a Media</label></br>
                <fieldset class="fieldset_analysis">
                
      					<img class="fbaicon" src="https://bl3302files.storage.live.com/y4mSjoGST_1u0kNfStbH1q5DQJuZ6k51PSkC6wvofGeJasTlaJE25O1v3FVkfsQiYbL0Fk-FopgDAfmD89CuEoWUBLqUC04ejS6KIcW6aJ8o-Bsgc27EcROT5nP951Yo-glM614y1-IGqRG7wlfH4-7yNi-kXyC68nIyrH4a7hKDIHakuonq8GEuGUF318f3gWV?width=138&height=141&cropmode=none" alt="choose media alt" /><br><br>
      					
                
                <select name="media">					
      						<option value="" > Choose a medium</option>
''')


connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
    
query2 = "SELECT DISTINCT Media_ID, Medium FROM Media;"
  
with connection.cursor() as cursor2:
	cursor2.execute(query2)
  
	#media_records=cursor.fetchone()

#using the cursor as iterator
for m in cursor2:
	media=str(m[1])
	medium_id=str(m[0])
	#print(refseq)
	#print("<p> %s %s </p>" % (medium_id, media))
	print("<option value=%s > %s </option>"%(medium_id, media))
cursor2.close()
connection.close()

print("</select>")

print('''
      				</fieldset> </p>                                   
            <input type='submit' id="fba_request_btn" name="fba_request_btn" value="Next"/>
            </form>''')
        
      
print("</div>")

print('''
				<p><hr></hr></p>
        
				<div id="midfba2"  class="mainfba_hori_div">
					<div  id="viewmetabolites" class="viewoptions">
						<a href="./explore.py" target="_blank"><a class="clickme" href="./explore.py?explore=Metabolite" target="_blank"><label>Explore Metabolites</label></a></a>
					
					</div>
					<div id="viewmodel" class="viewoptions">
					<a href="./explore.py" target="_blank"><a class="clickme" href="./explore.py?explore=Model" target="_blank"><label>Explore Models</label></a></a>
					</div>
					<div id="viewreactions" class="viewoptions">
					<a href="./explore.py" target="_blank"><a class="clickme" href="./explore.py?explore=Reaction" target="_blank"><label>Explore Reactions</label></a></a>
					</div>
				</div>


				</div>
				
			</div> ''')
print('''<div id="mainfooter_fba" class="maindiv">
			<p>Boston University &copy; 2020</p>
			</div>''')
      
print("</div>")
   
print("</body>")
print("</html>")

