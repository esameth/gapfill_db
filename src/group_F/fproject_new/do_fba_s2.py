#!/usr/local/Python-3.7/bin/python

import os
import site
import sys
import cobra
import cplex
import re
import numpy as np
import pandas as pd

from math import exp
from Bio import Entrez

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
					<!--<li><a href="./search_page.py"><label>Search</label></a></li>-->
					<li><a href="./how_to_do.py"><label>How To</label></a></li>
					<li><a href="./frequently_asked.py"> <label>FAQ </label></a></li>
				</ul>			
			</div>''')
print('''<div id="mainmid" class="maindiv" >''')



form=cgi.FieldStorage()

query = "SELECT RefSeq_Accession FROM Genome;"
connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
with connection.cursor() as cursor:
    cursor.execute(query)
_allRef = cursor.fetchall()
cursor.close()
connection.close()

allRef = []
for row in _allRef:
    allRef.append(row[0])

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

def _Entrez_read(handle, validate=True, escape=False):
    from Bio.Entrez import Parser
    handler = Entrez.Parser.DataHandler(validate, escape)
    handler.directory = '/var/www/cgi-bin/students_21/group_proj/group_F/handler'
    record = handler.read(handle)
    return record

def _get_model(refseq, medium):
    connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)

    query = "SELECT Gapfill_Model.XML FROM Genome JOIN Metabolic_Model USING(RefSeq_Accession) JOIN Gapfill_Model USING(MM_ID) JOIN Media USING(Media_ID) WHERE Refseq_Accession = '%s' AND Media_ID = %s;" % (
        refseq, medium)

    with connection.cursor() as cursor:
        cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0]

def _create_GM(genome, medium, media, MM_ID):
    # Create a gap-filled model
    os.system(
        'gapfill /var/www/html/images/students_21/group_proj/group_F/Metabolic_Model/%s.xml --cobra -m %s /var/www/html/images/students_21/group_proj/group_F/Gapfill_Model/%s_%s.xml --mediadb /var/www/html/images/students_21/group_proj/group_F/Media/media.tsv' % (
            genome, medium, genome, medium))

    # Add gapfilled model to database
    query = "INSERT INTO Gapfill_Model (XML, MM_ID, Media_ID) VALUES ('/var/www/html/images/students_21/group_proj/group_F/Gapfill_Model/%s_%s.xml', '%s', '%s')" % (
        genome, medium, str(MM_ID), str(media))
    connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
    with connection.cursor() as cursor:
        cursor.execute(query)
    
    connection.commit()
    cursor.close()
    connection.close()

def _get_MM_ID(genome):
    # Get MM_ID
    query = "SELECT MM_ID FROM Metabolic_Model WHERE RefSeq_Accession = '%s'" % genome
    connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
    with connection.cursor() as cursor:
        cursor.execute(query)
    MM_ID = cursor.fetchone()[0]
    return MM_ID

if form.getvalue("media"):
    media = form.getvalue("media")
    query = "SELECT medium FROM Media WHERE Media_ID = '%s'" % media
    connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
    with connection.cursor() as cursor:
        cursor.execute(query)
    medium = str(cursor.fetchone()[0])
    cursor.close()
    connection.close()


if form.getvalue("input_genome"):
    genome = form.getvalue("input_genome")

    if genome not in allRef:
        ######## Get organism name from RefSeq accession
        #Entrez.email = 'esameth1@bu.edu'
        # patched version of Entrez.read
        record = _Entrez_read(Entrez.esearch(db='assembly', term=genome))
        #print("<p> Handle: %s </p>" % record)
        # record = Entrez.read(result, validate=False)
        #print("<p> Record: %s </p>" % record)
        # Get Assembly Summary
        esummary_record = _Entrez_read(Entrez.esummary(db='assembly', id=record['IdList'], report='full'))
        organism = esummary_record['DocumentSummarySet']['DocumentSummary'][0]['SpeciesName']
        # esummary_handle = Entrez.esummary(db='assembly', id=record['IdList'], report='full')
        # esummary_record = Entrez.read(esummary_handle, validate=False)
        # Organism and strain
        #print("<p> ORGANISM: %s </p>" % organism)
        try:
            strain = esummary_record['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0][
                'Sub_value']
        except:
            strain = ''
        #print("<p> STRAIN : %s </p>" % strain)

        # Create metabolic model (not gap-filled) for storage in the database
        # if the same model needs to be run with a different media
        os.system(
            'carve --refseq %s --cobra -o /var/www/html/images/students_21/group_proj/group_F/Metabolic_Model/%s.xml' % (
            genome, genome))
        #print("<p> CARVE ME RAN </p>")

        # Add genome and metabolic model to database
        query = "INSERT INTO Genome (RefSeq_Accession, Species, Strain) VALUES ('%s','%s','%s')" % (genome, organism, strain)
        query2 = "INSERT INTO Metabolic_Model (XML, RefSeq_Accession) VALUES ('/var/www/html/images/students_21/group_proj/group_F/Metabolic_Model/%s.xml', '%s')" % (
        genome, genome)
        connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()
        cursor1.execute(query)
        cursor2.execute(query2)
        cursor1.close()
        cursor2.close()
        connection.commit()
        connection.close()

elif form.getvalue("select_refseq"):
    genome = form.getvalue("select_refseq")

MM_ID = _get_MM_ID(genome)
gapfill_model = _get_model(genome, media)
if gapfill_model is None:
     _create_GM(genome, medium, media, MM_ID)

gapfill_model = _get_model(genome, media)
#print("<p> %s, %s</p>" % (gapfill_model, create_filepath(gapfill_model)))
connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
with connection.cursor() as cursor:
	# Load the gap-filled model
	model = cobra.io.read_sbml_model(gapfill_model)

print('''				<h2>MMNSG Database</h2>
				<hr></hr>
				
				<div id="midfba1" class="mainfba_hori_div">
            <form action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_F/fproject_new/do_fba_s2.py"  method="post" id="run_fba_form" >
            
            <br>
            <label class="form_label_class" >Step 3: Choose exchange Metabolites</label> <br></br>
                  
                   <select name="select_metab" >
                     <option value="">Choose exchange metabolites</option>
                   ''')

#using the cursor as iterator
for ex in model.exchanges:
    for metab in ex.metabolites:
        metabolite=str(metab.id)
        print("<option value=%s > %s </option>"%(metabolite, metabolite))

print("</select>")
print('''                     
               
                <p><label class="form_label_class">Step 4: Enter Concentration</label></br>
                <fieldset class="fieldset_analysis">
                

      					
                
                <input type="text" name="choose_conc" id="choose_conc" placeholder="Type in your concentration here" />					
      						
''')



#print("</select>")
print('''
      				</fieldset> </p>             
               
            
              <input type='submit' id="fba_request_btn" name="fba_request_btn" value="Next" />
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

