#!/usr/bin/python

#import required packages
import os
import sys
import re
import numpy as np
import pandas as pd
import requests

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
print('''<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>''')

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
print(''' 
<script>
def download(url,id):
		if(url is not None):
		split_urls=[str(i) for i in url.split("/")]
		split_urls.pop(0)
		split_urls.pop(0) 
		split_urls.pop(0)
		split_urls.pop(0)
		url2='/'.join(split_urls)
		url2="https://bioed.bu.edu/"+url2
	  url=url2
  <iframe id="my_iframe" style="display:none;"></iframe>
  <script>
  
  function Download(url) {
    document.getElementById(id).src = url;
  };

</script>

</script>


''')


print('''				<h2>MMNSG Database</h2>
				<hr></hr>
				
				<div id="midfba1" class="mainfba_hori_div">''')
print("<div id='resultdl'>")

form=cgi.FieldStorage()

if(form.getvalue("details")):
	download_details=form.getvalue("details")
	XML, flux, conc, uptake, growth = download_details.split('@')
	flux=create_filepath(flux)
	conc=create_filepath(conc)
	uptake=create_filepath(uptake)
	growth=create_filepath(growth)

  
	print("<div class='download_arena'>")
	print('''<h2> Downloads Ready! </h2>''')
  #download(url, filename)
	print('''<p><strong>Gapfill_Model:</strong> %s <a onclick='download(%s,%s)' class='dlink' id="dmodel" href=%s download>download model</a></p>'''%(XML,XML,'dmodel', XML ))
	print("<br>")
	print('''<p><strong>Metabolic Flux:</strong> %s <a onclick='download(%s,%s)' class='dlink' id="dflux" href=%s download>download flux</a></p>'''%(flux, flux,'dflux',flux))
	print("<br>")
	print('''<p><strong>Media Concentration:</strong> %s <a onclick='download(%s,%s)' class='dlink' id="dconc" href=%s download>download concentration</a></p>'''%(conc, conc, 'dconc',conc))
	print("<br>")
	print('''<p><strong>Reaction Bound:</strong> %s <a onclick='download(%s,%s)' class='dlink' id="duptake" href=%s download>download uptake</a></p>'''%(uptake, uptake, 'duptake',uptake))
	print("<br>")
	print('''<p><strong>Image:</strong> %s <a onclick='download(%s,%s)' class='dlink' id="dgrowth" href=%s download>download growth plot</a></p>'''%(growth, growth, 'dgrowth', growth))
	print("<br>")
	print("</div>")#just 
else:
	print("Missing information")                                 
            

	
##elif(explore=="Metabolite"):

print("<p></p>")
print("</div>") 
  

print("</div>")  

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
#print('''<script type="text/javascript">
#        $(document).ready(function () {
#            $(".m").click(function (e) {
#                e.preventDefault(); 
#                window.location.href = %s;
#            });
#        });
#</script>'''%(growth))

