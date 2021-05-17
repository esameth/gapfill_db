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
					<li><a href="frequently_asked.py"> <label>FAQ </label></a></li>
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

          <h2>Project Overview</h2>
            <p>Flux balance analysis (FBA) is a mathematical approach for simulating metabolism in genome-scale reconstructions of metabolic networks. These network reconstructions contain all of the known metabolic reactions in an organism and the genes that encode various enzymes. Using these networks, the following predictions can be made: </p>
              
            <ol>
            
             <li> Whether an organism grows under different conditions, </li>
             <li> The rate at which the organism grows, and </li>
             <li>The rate at which a metabolite is produced </li>
              
            </ol>
            
            <p>However, FBA assumes a steady-state and linear contraints, which does not take into account growth kinetics or kinetic rate laws in an actual cell. Dynamic flux balance analysis (dFBA) is an extension of FBA that resolves this issue, and takes into account the changes of metabolite concentrations and reaction fluxes as a function of time due to biochemical and regulatory changes in the cell. </p>
              
            <h3> <b>NOTE : Information regarding how dFBA is performed and how the pipeline is executed can be found on our <a href="https://github.com/esameth/gapfill_db"> <label>github.</label></a> </b></h3> 
            
            <h3>This basic tutorial will be focusing on visualizing Pseudomonas simiae WCS417 growing on a RCH2 defined no-carbon media.</h3>

            <h2>Exploring Metabolites</h2>
            <ul>
            <li> Metabolites can be explored by clicking on the "Explore Metabolites" option on the home page.</li> This will allow you to retrieve information about the various metabolites present in the database.<br></br>
            <li>The search bar at the top can be also used to get information about a metabolite directly or the BiGG ID of a metabolite can be clicked to view more details.</li>
						</ul> <i>(Hint : Search for 'glc__D_e' in the search bar to explore how glucose is involved with Pseudomonas simiae growth)</i>
            <p> Doing so will navigate you to a new page with detailed information regarding the metabolite with links to external databases for reference.
            Information regarding the various organisms a metabolite is associated with and all the reactions it is a part of will also be displayed in a tabular format. </p>
						
            <h2>Exploring Models</h2>
            <ul>
            <li> Metabolic and Gap-filled metabolic models can be explored by clicking on the "Explore Models" option on the home page.</li> This will allow you to retrieve information about the various metabolic models present in the database.<br></br>
            <li>The search bar at the top can be also used to get information about a metabolic model directly or a specific model can be clicked to reveal all the gap-filled models associated with it.</li>
						</ul><i>(Hint : Search for 'GCF_000698265.1'	in the search bar to view growth curves for Pseudomonas simiae)</i>
            <p> Doing so will navigate you to a new page with detailed information regarding the models with growth curves embedded on the website. The plots can be hovered over the curves to get information on the concentration value at a given point in time. 
            There are also options available for downloading the respective 'SBML' models. </p>
            <i> (Hint++ : The 'View Contents of Model button' at top will lead you to the metabolic network visualizations with the different fluxes and metabolites highlighted)</i>
             
            <h2>Exploring Reactions</h2>
            <ul>
            <li> Reactions can be explored by clicking on the "Explore Reactions" option on the home page.</li> This will allow you to retrieve information about the various reactions present in the database.<br></br>
            <li>The search bar at the top can be also used to get information about a reaction directly or the BiGG ID of a reaction can be clicked to view more details.</li>
						</ul> <i>(Hint : Search for 'BG_CELLB' in the search bar to see how D-glucose is transported by the ABC system in Pseudomonas simiae)</i>
            <p> Doing so will navigate you to a new page with detailed information regarding the reaction like the reaction equation with links to external databases for reference.
            Information regarding the various organisms and metabolites a rection is associated with will also be displayed in a tabular format. </p> 
						            
					  <h2>Exploring Growth Media</h2>
            <ul>
            <li> Growth Media can be explored by clicking on the "Explore Media" option on the home page.</li> This will allow you to retrieve information about the various compounds present in the specific growth media.<br></br>
            <li>The search bar at the top can be also used to get information about a particular media directly.</li>
						</ul> <i>(Hint : Search for 'LB' in the search bar to see what compounds the Lysogeny Broth medium is composed of)</i>
            <p> Doing so will navigate you to a new page with options to select a specific media (aerobic/anaerobic).</p> <i>(Bonus hint : Click on 'Display Compounds' under Medium : LB to get all the compounds present in LB growth media)</i>     
            
            <h2>Congratulations for making it through the tutorial! Happy exploring!</h2>
            
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
print('''<div id="mainfooter_fba" class="maindiv">
			<p>Boston University &copy; 2021</p>
			</div>
		</div> ''')
   
print("</body>")
print("</html>")



