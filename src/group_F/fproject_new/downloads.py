#!/usr/bin/python

#import required packages
import os
import sys
import re
import numpy as np
import pandas as pd

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
					<li><a href="./do_fba.py"><label>Run FBA</label></a></li>
					<li><a href="how_to_do.py"><label>How To</label></a></li>
					<li><a href="frequently_asked.py"> <label>FAQ </label></a></li>
				</ul>			
			</div>''')
print('''<div id="mainmid" class="maindiv" >''')





print('''				<h2>MMNSG Database</h2>
				<hr></hr>
				
				<div id="midfba1" class="mainfba_hori_div">''')
query = "SELECT DISTINCT gm.XML, Fluxes, Concentration, Uptake, Growth, RefSeq_Accession,Species,medium,Strain FROM dFBA JOIN Gapfill_Model gm USING (GM_ID) JOIN Metabolic_Model USING(MM_ID) JOIN Genome USING(RefSeq_Accession) JOIN Media USING (Media_ID);"
print("<table id='download' width=100%>")
print("<tr class='dwtabh1'><th colspan='5'>FBA Data</th></tr>")
print("<tr class='dwtabh2'><th>RefSeq_Accession</th><th>Organism</th><th>Strain</th><th>Medium</th><th>Action</th></tr>")
connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
  
with connection.cursor() as cursor:
	cursor.execute(query)

records=cursor.fetchall()
 
for row in records:
	refseq=str(row[5])
	species=str(row[6])
	medium=str(row[7])
	strain=str(row[8])
	details=str(row[0])+'@'+str(row[1])+'@'+str(row[2])+'@'+str(row[3])+'@'+str(row[4])
	#print(refseq)
	print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><a class='dlink' target='_blank' href='download_item.py?details=%s')>Download</a></td></tr>" %(refseq,species,strain,medium,details))

cursor.close()
connection.close()
print("</table>")

print("<p></p>")
print("</div>")

        
      
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
			<p>Boston University &copy; 2021</p>
			</div>''')
      
print("</div>")
   
print("</body>")
print("</html>")

