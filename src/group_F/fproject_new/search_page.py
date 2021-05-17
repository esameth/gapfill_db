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
print('''<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>''')

def trim_link(var):
    var=str(var).split(";")
    return (var)

def create_filepath(url):
	if(url is not None):
		split_urls=[str(i) for i in url.split("/")]
		split_urls.pop(0)
		split_urls.pop(0) 
		split_urls.pop(0)
		split_urls.pop(0)
		url2='/'.join(split_urls)
		url2="https://bioed.bu.edu/"+url2
	return (url2)
print("	<title>Final Semester Project</title>")
print("	</head>")
	
print("	<body>")
 
print('''
		<div id="main" >
			<div id="mainheader" class="maindiv">
				<ul id="nav" class="navitem">
					<li><a href="./homepage.py"><label>Home</label></a></li>
					<!--<li><a href="./search_page.py"><label>Search</label></a></li>-->
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

if(form.getvalue("searchkeyword") and (form.getvalue("searchcriteria"))):
	keyword=form.getvalue("searchkeyword")
	table=form.getvalue("searchcriteria")
	hd1="ORGANISMS"
	hd2="REACTIONS"
	print("<form><label>Keyword:</label><input type='text' value=%s disabled><label>Where to Search:</label><input type='text' value=%s disabled>"%(keyword,table))
	print("<p></p>")
	if(table=='Metabolite'):

		query ="""SELECT * FROM Metabolite WHERE (Name regexp %s) OR (M_BIGG_ID = %s)"""
		connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
    
		with connection.cursor() as cursor:
			cursor.execute(query,(keyword,keyword))
    
			#records=cursor.fetchall()
			#print("<div id='searched_item'>") 
			for row in cursor:
				print("<p></p>") # For space
				print("<div id='searched_item'>")
				#print("<div class = 'boxed'>")
				db_links=trim_link(row[3])
				bigg_id=row[0]
				print ("<p><label><strong>Metabolite:</strong>  %s </label></p>" %(row[2]))
				print ("<p><label><strong>BiGG ID:</strong>  %s </label></p>" %(row[0]))
				print ("<p><label><strong>Universal ID:</strong>  %s </label></p>" %(row[1]))  
				if len(db_links[0]) == 0 or db_links[0] is None or db_links[0].lower() == 'none':
                                        print("<p><label><strong>There are no external links for this metabolite</strong></label></p>")
                                else:
                                        print("<p><label><strong>External Database Links:</strong></br>")
                                        for db in db_links:
						try:
                                                	name, link = db.split(':', 1)
							print("<a target='_blank' href=%s>  %s </a> &emsp;" % (link, name))
                                        	except:
							continue
					print("</label></p>")
                                print("</div>")			
    
				#records=cursor.fetchall()
				query2="""SELECT * FROM Contains_Metab JOIN Metabolic_Model USING (MM_ID) JOIN  Genome USING (RefSeq_Accession) 
				WHERE M_BiGG_ID = %s GROUP BY RefSeq_Accession""" 

				with connection.cursor() as cursor2:
					cursor2.execute(query2,(bigg_id))
					results=cursor2.fetchall()
					if(results):						
						print("<p></p>")
						print("<table id='search' class='searchtable'>")
						print("<tr><th colspan='3'>%s</th></tr>"%(hd1))
						print("<tr><th>RefSeq Accession</th><th>Species</th><th>Strain</th></tr>")                       
                       
						for row in results:
							################################
							# Genome information with links to all gapfilled models of that organism
							print("<tr><td><a target='_blank' href='search_page.py?searchcriteria=Model&searchkeyword=%s'> %s</a></td><td>%s</td><td>%s</td></tr>" %(row[0], row[0], row[4],  row[5])) 
					 
						print("</table>")
					else:
						print("<p class='search_message_paragraph'>There is no organism associated with this metabolite<p>")
				cursor2.close()
			
				query3="""SELECT * FROM Contains_React JOIN Reaction USING (R_BiGG_ID) WHERE M_BiGG_ID = %s GROUP BY R_BiGG_ID""" 

				with connection.cursor() as cursor3:
					cursor3.execute(query3,(bigg_id))
					results_rct=cursor3.fetchall()
					if(results_rct):		
						print("<p></p>")#just for space
						print("<p></p>")#just for space
						print("<table id='search' class='searchtable'>")
						print("<tr><th colspan='3'>%s</th></tr>"%("REACTIONS"))
						print("<tr><th>BiGG ID</th><th>Name</th><th>Equation</th></tr>")                       
                       				
						#########################3
						# Reaction information with links to reaction search info
						for row in results_rct:
							print("<tr><td><a target='_blank' href= 'search_page.py?searchcriteria=Reaction&searchkeyword=%s'> %s </a></td><td>%s</td><td>%s</td></tr>" %(row[0],row[0], row[3],  row[4])) 
						 
						print("</table>")
					else:
						print("<p class='search_message_paragraph'>There is no reaction associated with this metabolite<p>")
                        
                		cursor3.close()
				#print("</div>")
				print("<hr class='solid'>")
			print("</div>")
		cursor.close()
		connection.close()
                              
	elif(table=='Reaction'):

		query ="""SELECT * FROM Reaction WHERE (Name regexp %s) OR (R_BiGG_ID = %s)"""
		
		hd2="REACTION"
      
		connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
    
		with connection.cursor() as cursor:
			cursor.execute(query,(keyword,keyword))
    
			#records=cursor.fetchall()

        
			for row in cursor:
				r_bigg_id=row[0]
				db_links_r=trim_link(row[3])
			
				print("<p></p>")#just for sapce
				print("<div id='searched_item'>")
      
      
				print ("<p><label><strong>Reaction:</strong>  %s </label></p>" %(row[1]))
				print ("<p><label><strong>BiGG_ID:</strong>  %s </label></p>" %(row[0]))
				print ("<p><label><strong>Equation:</strong>  %s </label></p>" %(row[2]))  
				

				if len(db_links_r[0]) == 0 or db_links_r[0] is None or db_links_r[0].lower() == 'none':
                                        print("<p><label><strong>There are no external links for this reaction</strong></label></p>")
                                else:
					print("<p><label><strong>External Database Links:</strong></br>")
					for db in db_links_r:
						try:
							name, link = db.split(':', 1)
							print("<a target='_blank' href=%s>  %s </a> &emsp;" % (link, name))
						except:
							continue
                                        print("</label></p>")
				print("</div>")
        
    
				#records=cursor.fetchall()
				with connection.cursor() as cursor2:
					query2="""SELECT * FROM Contains_React JOIN Metabolic_Model USING (MM_ID) JOIN  Genome USING (RefSeq_Accession) 
				WHERE R_BiGG_ID = %s GROUP BY RefSeq_Accession""" 
					cursor2.execute(query2,(r_bigg_id))
					results=cursor2.fetchall()
					if(results):
						print("<p></p>")#just
						print("<table id='search' class='searchtable'>")
						print("<tr><th colspan='3'>%s</th></tr>"%(hd1))
						print("<tr><th>RefSeq Accession</th><th>Species</th><th>Strain</th></tr>")                       
                       
						for row in results:
						    
							print("<tr><td><a target='_blank' href= 'search_page.py?searchcriteria=Model&searchkeyword=%s'> %s </a></td><td>%s</td><td>%s</td></tr>" %(row[0], row[0], row[5],  row[6])) 
						 
						print("</table>")
					else:
						print("<p class='search_message_paragraph'>There is no organism associated with this Reaction<p>")
                    
				cursor2.close()
				query3="""SELECT * FROM Contains_React JOIN Metabolite USING (M_BiGG_ID) WHERE R_BiGG_ID = %s GROUP BY M_BiGG_ID""" 

				with connection.cursor() as cursor3:
					cursor3.execute(query3,(r_bigg_id))
					results_mt=cursor3.fetchall()
					if(results_mt):
							
						print("<p></p>")#just for sapce
						print("<p></p>")#just
						print("<table id='search' class='searchtable'>")
						print("<tr><th colspan='2'>%s</th></tr>"%("METABOLITES"))
						print("<tr><th>BiGG ID</th><th>Name</th></tr>")                       
                       
						for row in results_mt:
							print("<tr><td><a target='_blank' href= 'search_page.py?searchcriteria=Metabolite&searchkeyword=%s'> %s </a></td><td>%s</td></tr>" %(row[0],row[0], row[4])) 
						 
						print("</table>")
					else:
						print("<p class='search_message_paragraph'>There is no Metabolite in this DB associated with this Reaction<p>")
                        	cursor3.close()
				print("<hr class='solid'>")
			print("</div>")
		cursor.close()
		connection.close()
#********

	elif(table=='Media'):
		keyword1=keyword.upper()
		keyword2=keyword.lower()        

		query ="""SELECT DISTINCT Media_ID, medium FROM Media WHERE (medium regexp %s) OR (medium regexp %s)"""
		
		hd3="Media"
      
		connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
    
		with connection.cursor() as cursor:
			cursor.execute(query,(keyword1,keyword2))
    
			#records=cursor.fetchall()

        
			for row in cursor:
				media_id=row[0]
				
				print("<p></p>")#just for sapce
				print("<div id='searched_item'>")     
				print ("<p><label><strong>Medium:</strong>  %s </label></p>"%(row[1]))
				print ("<p><a  target='_blank' href='./media_c.py?media_id=%s' > Display Compounds </a></p>"%(media_id))
				
				print("</div>")
			print("<p></p>")
		

	elif(table=='Model'):
		keyword1=keyword.upper()
		keyword2=keyword.lower()        
		query ="""SELECT DISTINCT GM_ID, MM_ID, RefSeq_Accession, Species, Strain, medium, DFBA_ID, Growth FROM Genome g JOIN Metabolic_Model mm USING (RefSeq_Accession) JOIN Gapfill_Model gm USING (MM_ID) JOIN dFBA USING (GM_ID) JOIN Media USING (Media_ID) WHERE (RefSeq_Accession regexp %s) OR (Species regexp %s) OR (Strain regexp %s) OR (RefSeq_Accession regexp %s) OR (Species regexp %s) OR (Strain regexp %s)"""
		
		   
		connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
    
		with connection.cursor() as cursor:
			cursor.execute(query,(keyword1,keyword1,keyword1,keyword2,keyword2,keyword2))
    
			records=cursor.fetchall()

        
		for row in records:
			gm_id=row[0]
			mm_id=row[1]
			refseq=str(row[2])
			species=str(row[3])
			strain=str(row[4])
			medium=row[5]
			dfba_id=str(row[6])
			growth=str(row[7])
			
			query2 = """SELECT Metabolite, Concentration FROM Concentrations WHERE dFBA_ID = %s"""
			

			with connection.cursor() as cursor:
				cursor.execute(query2, (dfba_id))
				concentrations = cursor.fetchall()

	 		growth=create_filepath(growth)
		
			
			print("<div class='outputbox'>")
			print("<h3><center><a target='_blank' href= 'search_page.py?searchcriteria=Gapfill&searchkeyword=%s'>View Contents of Model</a></center></h3>" % dfba_id)
			print("<div class='outputbox_sub'>")     
			print ("<p><label><strong>RefSeq Accession:</strong>  %s </label></p>"%(refseq))
			print ("<p><label><strong>Species:</strong>  %s </label></p>"%(species))
			print ("<p><label><strong>Strain:</strong>  %s </label></p>"%(strain))
			print ("<p><label><strong>Medium:</strong>  %s </label></p>"%(medium))
			print ("<p><label><strong>Initial Conditions:</strong>")
			for conc in concentrations:
				print("%s: %s &emsp;"%(conc[0], conc[1]))
			print("</label></p>")
			print("</div>")
			print("<div class='outputbox_sub'>")
			print ("<a  target='_blank' href=%s ><iframe src=%s title='Growth rate and concentration plot from a dFBA associated with your searched model'></iframe></a>"%(growth,growth))
			print("</div>")
			print("</div>")
		print("<p></p>")
	
	
	####### Gapfilled models
	elif table == "Gapfill":
		dfba_id=keyword.upper()
		connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)

		# Get all info
		query = "SELECT DISTINCT Metabolic_Model.MM_ID, Metabolic_Model.XML as MM_XML, Gapfill_Model.XML as GM_XML, Medium, Fluxes, Concentration, Uptake, Growth, RefSeq_Accession FROM dFBA JOIN Gapfill_Model USING(GM_ID) JOIN Metabolic_Model USING(MM_ID) JOIN Media USING(Media_ID) WHERE dFBA_ID = %s"
		# Get all metabolites
		query1 = "SELECT M_BiGG_ID, Name FROM Contains_Metab JOIN Metabolite USING(M_BiGG_ID) WHERE MM_ID = %s" 
		# Get all reactions
		query2 = "SELECT R_BiGG_ID, Name FROM Contains_React JOIN Reaction USING(R_BiGG_ID) WHERE MM_ID = %s"
		# Get Escher info
		query3 = "SELECT * FROM Escher WHERE dFBA_ID = %s" 
		# Get Genome info
		query4 = "SELECT * FROM Genome WHERE RefSeq_Accession = %s"
		
		with connection.cursor() as cursor:
			cursor.execute(query, dfba_id)
			results = cursor.fetchall()[0]
			MM_ID, MM_XML, GM_XML, medium, flux, conc, uptake, growth, refseq = results[0], results[1], results[2], results[3], results[4], results[5], results[6], create_filepath(results[7]), results[8]
			cursor.execute(query1, MM_ID)
			metabolites = cursor.fetchall()
			cursor.execute(query2, MM_ID)
			reactions = cursor.fetchall()
			cursor.execute(query3, dfba_id)
			escher = cursor.fetchone()
			cursor.execute(query4, refseq)
			organism = cursor.fetchall()[0]
			species, strain = organism[1], organism[2]
		escher=create_filepath(escher[3])

		query = """SELECT Metabolite, Concentration FROM Concentrations WHERE dFBA_ID = %s"""
		with connection.cursor() as cursor:
			cursor.execute(query, (dfba_id))
			concentrations = cursor.fetchall()

		print("<div class='outputbox'>")
		print("<div class='outputbox_sub'>")
		print("<h2><center>Gap-filled Model for Accession %s</center></h2>" % (refseq))
		print ("<p><label><strong>Species:</strong>  %s </label></p>"%(species))
		print ("<p><label><strong>Strain:</strong>  %s </label></p>"%(strain))
		print ("<p><label><strong>Medium:</strong>  %s </label></p>"%(medium))
		print ("<p><label><strong>Initial Conditions:</strong>")
		for conc in concentrations:
			print("%s: %s &emsp;"%(conc[0], conc[1]))
		print("</label></p>")
		print("</div>")
		print("</div>")

		print("<div class='outputbox_sub'>")
		# Metabolite Scrolling Table
		print("<p><label><strong>Metabolites</strong></label></p>")
		print("<div style='overflow:scroll; height:500px;'><table id='search' class='searchtable'>")
		print("<p></p>")
		print("<tr><th>BiGG ID</th><th>Name</th></tr>")
		for row in metabolites:
			print("<tr><td><a target='_blank' href= 'search_page.py?searchcriteria=Metabolite&searchkeyword=%s'> %s </a></td><td>%s</td></tr>" %(row[0],row[0], row[1]))
		print("</table></div>")
		print("</table>")

		# Reaction Scrolling Table
		print("<p><label><strong>Reactions</strong></label></p>")
                print("<div style='overflow:scroll; height:500px;'><table id='search' class='searchtable'>")
                print("<p></p>")
                print("<tr><th>BiGG ID</th><th>Name</th></tr>")
                for row in reactions:
                        print("<tr><td><a target='_blank' href= 'search_page.py?searchcriteria=Reaction&searchkeyword=%s'> %s </a></td><td>%s</td></tr>" %(row[0],row[0], row[1]))
                print("</table></div>")
                print("</table>")


                print("<div class='outputbox'>")
		print("<p><label><strong>Growth rate and Initial Concentration Dynamics</strong></label></p>")
		print ("<a  target='_blank' href=%s ><iframe src=%s title='Growth rate and concentration plot from a dFBA associated with your searched model'></iframe></a>"%(growth,growth))
		print("</div>")
		#print("<div class='outputbox'>")
		
		print ("<div align='center'><a  target='_blank' href=%s ><iframe src=%s style='width:100vw; height:100vh' title='Network of the dFBA associated with your searched model'></iframe></a></div>" % (escher,escher))
	
else:
	print("No criteria value received");
 
##elif(explore=="Metabolite"):


print("</div>") 
  

print("</div>")       
        
        
        
print('''	<div id="midh2search">
					<div  id="viewmetabolites" class="navlink">
						<a class="clickme" href="homepage.py"><label>To Home</label></a>
					
					</div>
					<div id="viewmodel" class="navlink">
					<a class="clickme" href="./do_fba.py"><label>Run FBA Page</label></a>
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

