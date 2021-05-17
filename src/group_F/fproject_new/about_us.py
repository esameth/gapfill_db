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
          <center> <h2>About Us</h2>
            <p>This project was undertaken under the guidance of:
							 <br></br><img src="https://media-exp1.licdn.com/dms/image/C4E03AQEi6nMMT0JH-Q/profile-displayphoto-shrink_200_200/0/1614865685784?e=1620864000&v=beta&t=nESHDEb2T7KoALk_9K4LpFOWPrlzNcaWS6N091snv-A" >
							 <br></br> <b>Daniel Segr&egrave;</b>
               </br>Director, BU Microbiome Initiative
               </br>Professor of Biology, 
               </br>Biomedical Engineering & Physics
               </br><a href="mailto:dsegre@bu.edu" > <label> dsegre@bu.edu </label> </a>
							 </p>
              
            <h3> This project was part of the ENG BF 768 database class (Spring 2021) at Boston University taught by Professor Gary Benson. </h3> </center>
              <h3>Team Members:</h3>
            <p> 
						  <b>Elysha Sameth</b>
              </br>	<b>Yashrajsinh Jadeja</b>
							</br>	<b>Sooyoun Lee</b>
							</br>	<b>Emmanuel Saake</b>										 							  
						</p>
             
             <h3> Purpose of the Database : </h3>
             <p>
             Flux Balance Analysis (FBA) is a mathematical approach for simulating metabolism in genome-scale reconstructions of metabolic networks. These network reconstructions contain all of the known metabolic reactions in an organism and the genes that encode various enzymes. Using these networks, the following predictions can be made: (1) whether an organism grows under different conditions, (2) the rate at which the organism grows, and (3) the rate at which a metabolite is produced. </p>
             
	            <p>Although there are databases such as BiGG that host curated genome-scale metabolic network reconstructions, there are currently no databases for storing gap-filled models and the results of dynamic FBA under various conditions. Our project aims to alleviate this issue and implement novel functionalities by:

<ul>
<li>Providing an interactive graphical interface for visualizing gap-filled metabolic networks</li>
<li>Resolving the static nature of existing databases by providing a dynamic database </li>
<li>Facilitating the troubleshooting of why an organism grows/does not grow given specific environmental conditions</li>
<li>Providing graphic visualizations of the simulated growth curves (biomass vs. time) and metabolic networks</li>
<li>Allowing for querying by organism, media, metabolite, pathway, and reaction</li>
</ul>
          </p>
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



