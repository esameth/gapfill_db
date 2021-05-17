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
 
print('''
		<div id="faq_main" >
   				<h2 style="text-align:center">MMNSG Database</h2>
				<hr></hr>
			<div id="mainheader" class="faq_maindiv">
				<ul id="nav" class="navitem">
					<li><a href="./homepage.py"><label>Home</label></a></li>
					<li><a href="./do_fba.py"><label>Run FBA</label></a></li>
					<li><a href="how_to_do.py"><label>How To</label></a></li>
					<li><a href="do_fba.py"> <label>Run FBA </label></a></li>
				</ul>
				
				<form action="" method="post" id="searchform" class="navitem">
				<input type="text" name="search" value=""/>
				<input type="submit" value="search">
				</form>
			
			</div>
      	<hr></hr>
			<div id="faq_mainmid" class="faq_maindiv">
''')
				
print('''	<div id="faq_midh1search">

          <h2> What questions does this project aim to answer?</h2>
            <ul>
                  <li>How does a microorganism grow under different sources/conditions? </li>
                  <li>What is the flow of a given metabolite through the metabolic network? </li>
                  <li>How do growth rates of an organism compare across different conditions and/or media? </li>
                  <li>What are the metabolites and their fluxes in a given pathway? </li>
                  <li>What are the upper and lower bounds of a particular reaction?  </li>
            </ul>
				
					<h2>What is the work flow of this tool for performing dFBA?</h3>
			        <ul>
                 <li> User uploads/chooses a genome and growth media </li>
                 <li> We retrieve/create the gapfilled metabolic model </li>
                 <li> We give a dropdown menu of all the compounds that could be added to the gapfilled model </li>
                 <li> The user can select the compound or filter for one or more and specify concentrations </li>
                 <li> Dynamic Flux Balance Analysis will be performed and results (growth curves, metabolic networks) can be visualized </li>
             </ul>
             
         <h2> What predictions can you run with this platform?</h2>
             <ul> 
               <li> Whether an organism grows under different conditions </li>
               <li> The rate at which the organism grows </li>
               <li> The rate at which a metabolite is produced </li>
             </ul>
                 
             <h2> Can I explore the database without running dFBA analysis?</h2>
						 Yes! The website can be explored for retrieving information about analyses that have already been performed.
					  
             
             <h2> Further Development </h2>
             We plan to implement some missing functionalities due to package dependencies on the current server when the technical issues are resolved.
             If you plan to keep a close eye on development, follow our <a href="https://github.com/esameth/gapfill_db"> <label>github</label></a>. 
             </br>
				</div>
				<hr></hr> 
        ''')
print('''		<div id="midh2search">
					<div  id="viewmetabolites" class="navlink">
						<a class="clickme" href="homepage.py"><label>To Home</label></a>
					
					</div>
					<div id="viewmodel" class="navlink">
					<a class="clickme" href="search_page.py"><label>To Search Page</label></a>
					</div>
					<div id="viewreactions" class="navlink">
					<a class="clickme" href=""><label>To Help Page</label></a>
					</div>
				</div>
				
				
			</div> ''')
print('''<div id="mainfooter" class="maindiv">
			<p>Boston University &copy; 2020</p>
			</div>
		</div> ''')
   
print("</body>")
print("</html>")


