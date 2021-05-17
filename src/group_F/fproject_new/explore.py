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

print('''<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>''')
#print("<link rel='stylesheet' type='Text/css' href='https://drive.google.com/file/d/1dFjr-z6zSCIBUYYXz2nJBlqmIQm33Ytb'>")
#some function to help clean out link
'''def trim_link(var):
    var2 = str(var).split(';')
    #print("<p> %s </p>" % var2)
    var2.pop(0)
    var2=":".join(var2)
''' 

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
				<input type="submit" value="search">
				</form>
			
			</div>
			<div id="mainmid" class="maindiv">
				<h2>MMNSG Database</h2>
				<hr></hr>''')
form=cgi.FieldStorage()

explore=form.getvalue("explore")

if explore == "Metabolite":
  placeholder=str("Enter BiGG ID or Metabolite Name (Hint : glc__D_e or D-Glucose)")
if explore == "Model":
  placeholder=str("Enter Refseq Accession or Organism Name (Hint : GCF_000698265.1 or Pseudomonas simiae)")
if explore == "Reaction":
  placeholder=str("Enter BiGG ID or Reaction Name (Hint : BG_CELLB or Glucosidase)")
if explore == "Media":
  placeholder=str("Enter Media Name (Hint : LB)")

#placeholder=str("Search "+explore)
				
print('''	<div id="midh1search">
					<form action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_F/fproject_new/search_page.py" method="GET" id="mainsearchform" class="">
            <input name="searchcriteria" type="hidden" id="searchcriteria" value=%s />
						<input type="text" name="searchkeyword" id="searchkeyword" placeholder="%s" value=""/>
						<input type="submit" value="search" id="mainsearchbtn" />
            <div id="ajsearchdisplay"></div>
					</form>
			    <div id="ajsearchdisplay" value=""></div>
				</div>
				<hr></hr> 
        '''%(explore,placeholder))
print("<div id='result'>")

if(explore=="Reaction"):
	query = "SELECT * FROM Reaction;"
  
	print("<table id='search'>")
        print("<tr><th colspan='2'>Explore Reactions</th></tr>")
	print("<tr><th>BiGG ID</th><th>Name</th></tr>")
  
	connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
  
	with connection.cursor() as cursor:
		cursor.execute(query)
  
	records=cursor.fetchall()
  
	for row in records:
		row0=str(row[0]).strip()
		print("<tr><td><a target='_blank' href= 'search_page.py?searchcriteria=Reaction&searchkeyword=%s'> %s </a></td><td> %s</td></tr>" %(row0, row0, row[1])) 
    
	cursor.close()
	connection.close()
	print("</table>")
 
 
elif(explore=="Metabolite"):
	query = "SELECT * FROM Metabolite;"
  
	print("<table id='search'>")
	print("<tr><th colspan='2'>Metabolites</th></tr>")
	print("<tr><th>BiGG ID</th><th>Name</th></tr>")
  
	connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
  
	with connection.cursor() as cursor:
		cursor.execute(query)
  
	records=cursor.fetchall()
  
	for row in records:
		row0=str(row[0]).strip()
		print("<tr><td><a target='_blank' href= 'search_page.py?searchcriteria=Metabolite&searchkeyword=%s'> %s </a></td><td> %s </td></tr>" %(row0, row0, row[2])) 
    
	cursor.close()
	connection.close()
	print("</table>")
	 
elif(explore=="Media"):
	query = "SELECT DISTINCT medium, description FROM Media;"
  
	print("<table id='search'>")
	print("<tr><th colspan='2'>Media</th></tr>")
	print("<tr><th>Medium</th><th>Description</th></tr>")
  
	connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
  
	with connection.cursor() as cursor:
		cursor.execute(query)
  
	records=cursor.fetchall()
  
	for row in records:
		row0=str(row[0]).strip()
		print("<tr><td><a href='search_page.py?searchcriteria=Media&searchkeyword=%s'> <label>%s</label><td>%s</td></tr>" %(row0,row0,row[1]))
																																																																		
    
	cursor.close()
	connection.close()
	print("</table>")
	 
elif(explore=="Model"):
	query = "SELECT * FROM Genome g JOIN Metabolic_Model mm USING (RefSeq_Accession);"
	print("<table id='search_model'>")
	print("<tr><th colspan='4'>Model</th></tr>")
	print("<tr><th>RefSeq Accession</th><th>Species</th><th>Strain</th><th>XML File</th></tr>")
	connection = pymysql.connect(db="group_F", user="test", password="test", port=4253)
    
	with connection.cursor() as cursor:
		cursor.execute(query)
    
	records=cursor.fetchall()
   
	for row in records:
		refseq=str(row[0])
		species=str(row[1])
		strain=str(row[2])
		xml=str(row[4])
		xml=create_filepath(xml)
		print("<tr><p></p><td><a id='show_items' href= 'search_page.py?searchcriteria=Model&searchkeyword=%s'> %s </td><td>%s</td><td>%s</td><td><a onclick='download(%s,%s)' class='dlink' id='dmodel' href=%s download>Download</a></td><p></p></tr>" %(refseq,refseq, species,strain, refseq, refseq, xml))
	cursor.close()
	connection.close()
	print("</table>")
 

	
print("<p></p>")
print("</div>")       
        
        
        
print('''		<div id="midh2search">
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

print('''<div id="mainfooter" class="maindiv">
			<p>Boston University &copy; 2021</p>
			</div>
		</div> ''')


  
print("</body>")
print('''
<script type="text/javascript">
$(document).ready(function(){
  $('#searchkeyword').keyup(function(){
      var query = $(this).val();
      var explorez=%s;
        if(query != '')
        {
          $.ajax({
            url:"https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_F/fproject_new/ajx.py",
            method:"POST",
            dataType: 'json',
            data:{query:query, explorez:explorez},
            success:function(data)
            {
              $('#ajsearchdisplay').fadeIn();
              $('#ajsearchdisplay').html(data);
            }
          });
        }
        
      
  });
  $(document).on('click','li',function(){
              $('#searchkeyword').val(this).text());
              $('#searchkeyword').fadeOut();
  });
});
</script>''' %(explore))
#print(explore)
print("</html>")

