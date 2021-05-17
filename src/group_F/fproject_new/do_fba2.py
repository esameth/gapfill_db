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

print("<link rel='stylesheet' type='Text/css' href='https://drive.google.com/file/d/1dFjr-z6zSCIBUYYXz2nJBlqmIQm33Ytb'>")


print("	<title>Final Semester Project</title>")
print("	</head>")
	
print("	<body>")
 
print('''<div id="main_fba" >''')
print('''	<div id="mainheader" class="maindiv">
				<ul id="nav" class="navitem">
					<li><a href="./homepage.py"><label>Home</label></a></li>
					<li><a href="search_page.py"><label>Search</label></a></li>
					<li><a href="how_to_do.py"><label>How To</label></a></li>
					<li><a href="frequently_asked.py"> <label>FAQ </label></a></li>
				</ul>			
			</div>''')
print('''<div id="mainmid" class="maindiv" >''')

print('''				<h2>MMNSG Database</h2>
				<hr></hr>
				
				<div id="midfba1" class="mainfba_hori_div">
            <form action="./do_fba.py"  method="post" id="run_fba_form" >
               <label class="form_label_class">Refseq Accession</label><br>
               <p><input type="text" name="accession_number" id="accession_number" placeholder="Input Refseq Accession Here" /></p>
               
                <label class="form_label_class"> Choose a Media</label>
                <fieldset class="fieldset_analysis">
					
                <legend>Step 1: Choose Media</legend><br>
      					
      	               
      					<img class="fbaicon" src="https://bl3302files.storage.live.com/y4mSjoGST_1u0kNfStbH1q5DQJuZ6k51PSkC6wvofGeJasTlaJE25O1v3FVkfsQiYbL0Fk-FopgDAfmD89CuEoWUBLqUC04ejS6KIcW6aJ8o-Bsgc27EcROT5nP951Yo-glM614y1-IGqRG7wlfH4-7yNi-kXyC68nIyrH4a7hKDIHakuonq8GEuGUF318f3gWV?width=138&height=141&cropmode=none" alt="choose media alt" /><br>
      					
                
       				  <form name="mediafilter" action="" method="">
      						<label>Name</label><input name="mfilter" type="radio" value="" checked/>
      						<label>ID</label><input name="mfilter" type="radio" value=""/>
      					</form> <br>
                <select name="media">					
      						<option value="" placeholder="choose a media"> Choose a media</option>
      						<option value="">Media 1</option>
      						<option value="">Media 2</option>
      						<option value="">Media 3</option>
      					
      					</select>
      				</fieldset> 
               
               
            
            
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


