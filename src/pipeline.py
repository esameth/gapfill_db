#!/usr/bin/python
import pymysql
import sys
import cgi
import cgitb
import re
import cobra
import os

from dfba import DfbaModel, ExchangeFlux, KineticVariable
from Bio import Entrez

cgitb.enable()

######## This is just a place-holder/example to be replaced
print('''<form name="OrgSearch" action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_F/gapfill.py" method="POST" >
	RefSeq Accession: <input type="text" id="refseq" name="refseq" value="" />
	Media: <select name="media" id="media">
            <option value="LB">Lysogeny broth</option>
            <option value="LB[-O2]">Lysogeny broth (anaerobic)</option>
            <option value="M9">M9 minimal medium</option>
            <option value="M9[-O2]">M9 minimal medium (anaerobic)</option>
            <option value="M9[glyc]">M9 minimal medium (glycerol)</option>
            <option value="RCH2">RCH2 (glucose)</option>
        </select>
	<input type="submit" value="Search" / >
	</form>''')

#### save all refseq ids as a list called allRef
rquery = "SELECT RefSeq_Accession FROM Genome;"
connection = pymysql.connect(... , port=4253)
cursor = connection.cursor()
cursor.execute(rquery)
allRef = cursor.fetchall()
cursor.close()
connection.close()

# get the form
form = cgi.FieldStorage()
refseq = form.getvalue("refseq")
media = form.getvalue("media")

if refseq:
    # Check if not in database already
    if refseq not in allRef:
        ######## Get organism name from RefSeq accession
        handle = Entrez.esearch(db='assembly', term=refseq)
        record = Entrez.read(handle)

        # Get Assembly Summary
        esummary_handle = Entrez.esummary(db='assembly', id=record['IdList'], report='full')
        esummary_record = Entrez.read(esummary_handle)

        # Organism and strain
        organism = esummary_record['DocumentSummarySet']['DocumentSummary'][0]['SpeciesName']
        try:
            strain = esummary_record['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0][
                'Sub_value']
        except:
            strain = ''

        # Create metabolic model (not gap-filled) for storage in the database
        # if the same model needs to be run with a different media
        os.system('carve --refseq %s --cobra -o %s.xml') % (refseq, refseq)

        # Create a gap-filled model
        os.system('gapfill %s.xml --cobra -g %s -i %s --mediadbmedia_db.tsv') % (refseq, media, media)

        # Add models and genome to database
        query = "INSERT INTO ..."

    # Get gap-filled model
    query = "SELECT GM_ID FROM Gapfill_Model WHERE ..."


####### See if want to search for a rxn/metabolite or perform dfba



