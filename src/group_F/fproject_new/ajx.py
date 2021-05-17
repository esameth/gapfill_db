#!/usr/bin/python


# import required packages
import pymysql
import cgi
import cgitb
cgitb.enable()

print("Content-type: text/html\n")
print("<html><head>")
print("	</head>")
	
print("	<body>")

form=cgi.FieldStorage()


if(form.getvalue("queryy") and form.getvalue("explorez")):
    keywordz=form.getvalue("query")
    explorez=form.getvalue("explore")
  
    connectionz = pymysql.connect(db="group_F", user="test", password="test", port=4253)
    ajresults=''
    queryz=''
    if(explorez=="Reaction"):
        queryz ="""SELECT * FROM Reaction WHERE (Name regexp %s) OR (R_BiGG_ID regexp %s)"""
    elif(explorez=="Metabolite"):
        queryz ="""SELECT * FROM Metabolite WHERE (Name regexp %s) OR (M_BIGG_ID regexp %s)"""
    elif(explorez=="Media"):
        queryz ="""SELECT DISTINCT Media_ID, medium FROM Media WHERE (medium regexp %s) OR (medium regexp %s)"""
    
    elif(explorez=="Model"):
        queryz ="""SELECT DISTINCT RefSeq_Accession, Species, Strain, medium, DFBA_ID, Growth FROM Genome g JOIN Metabolic_Model mm USING (RefSeq_Accession) JOIN Gapfill_Model gm USING (MM_ID) JOIN dFBA USING (GM_ID) JOIN Media USING (Media_ID) WHERE (RefSeq_Accession regexp %s) OR (Species regexp %s)"""

    ajresults="<ul class='ajdisplay'>"
    with connectionz.cursor() as cursorz:
        cursorz.execute(queryz,(keywordz,keywordz))
        if(cursorz.fetchall()):
            recordsz=cursorz.fetchall()
            for rowz in recordsz:
                rowz0=str(rowz[0]).strip()
                rowz1=str(rowz[1]).strip()
                ajresults=ajresults+"<li></li>%s<li>%s</li>"%(row0,row1)
        else:
            ajresults=ajresults+"<li>search item not in database</li>" 

        ajresults=ajresults+"</ul>"
        print(ajresults)
	cursorz.close()
	connectionz.close()
else:
	print("nothing")
print("</body>")
print("</html>")     
