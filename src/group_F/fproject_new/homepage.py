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
 
print('''<div id="main" >''')
print('''			<div id="mainheader" class="maindiv">
				<ul id="nav" class="navitem">
					<li><a href="./about_us.py"><label>About Us</label></a></li>
					<!--<li><a href="search_page.py"><label>Search</label></a></li>-->
					<li><a href="how_to_do.py"><label>How To</label></a></li>
					<li><a href="frequently_asked.py"> <label>FAQ </label></a></li>
          <li><a href="downloads.py"> <label>Download</label></a></li>
				</ul>			
			</div>''')
print('''<div id="mainmid" class="maindiv" >''')

print('''				<h2>MMNSG Database</h2>
              <h3>Microbial Metabolic Networks and Simulated Growth Rates</h3>
				<hr></hr>
				
				<div id="midh1">
          <img src="https://bl3302files.storage.live.com/y4mR-P1SJbL_bVzhoIgkdImHQLg23Wkxc_mciHyirzv-MeMjlY9gn403GyWYAW3DqPGGKAe_ayYJ16DwkJtVuz-Dw_4c2ZY8s22QuFoGm8rjGe0fDiGkmuNS8nxjJ2ee6_nD7rC0D8kQqPoYoViJ9CZzxMKxLqqzXOtLEYtsE5EGFtHtJ89FeFyF48a3Jna2tkV?width=292&height=211&cropmode=none" > <br>
          <form name="fba_request" action="./do_fba.py" method="post">
						<input type='submit' id="fba_request_btn" name="fba_request_btn" value="DO FBA" />
					</form>
			''')
				
print('''</div>
				<hr></hr>
				<div id="midh2">
					<div  id="viewmetabolites" class="viewoptions">
						<a href="./explore.py?explore=Metabolite" target="_blank"><img src="https://bl3302files.storage.live.com/y4mMcEE076TkFRi_HNNqyrir3nT7_opX803su5oNcCIAHXOPnwNIMqhQiTc4s7BAiPAtSn7ljLFOWykUsAb1VETozyRMtaeCsjbJ0_X0jshX3grijw83_EHvofsgq9A0qTkpfRbVMWSGu8p79PXfILFoF-uhJOf1HfvNXjaAlxi195_DQf54W0vmUm4QOJxten3?width=277&height=182&cropmode=none"><br><a class="clickme" href="./explore.py?explore=Metabolite" target="_blank"><label>Explore Metabolites</label></a></a>
					
					</div>
					<div id="viewmodel" class="viewoptions">
					<a href="./explore.py?explore=Model" target="_blank"><img src="https://bl3302files.storage.live.com/y4mqtywm18imwserbW9QLiSon_YchEhEekQeLgf_KtQ15XjlGNZGYzHGiG5_ut1JZWrAcgTjFLJkxbymAs7NHbxaoquVU4AuuYvf3QjGjMOIBK375rsKg0dThIREqG7Qb8TBxTgwlixdzsKQn8til7f1MSAA7hZ8IcFy7Omk32eDJSHPUWrJyTxKHFYFZHBStXk?width=252&height=192&cropmode=none"><br><a class="clickme" href="./explore.py?explore=Model" target="_blank"><label>Explore Models</label></a></a>
					</div>
					<div id="viewreactions" class="viewoptions">
					<a href="./explore.py?explore=Reaction" target="_blank"><img src="https://bl3302files.storage.live.com/y4mTecq_rjCrEVu7im324UfmFrEN5G4ZkgNnXV8SWXakO8BelE1r1AI8L2n_qBqD4-LjLi8m3du9Ua9gzCF47SZHf5OAQfw5hrn1N7PDJ0o4gkdY9upSjZ8JDk8Mn4gGHlYnXdqmaJl8Uylsp5p09TLAT9E1dKqhvaS82ROxxbKUE2FuakZDV_SZ9CZj28CG5EA?width=277&height=181&cropmode=none"><br><a class="clickme" href="./explore.py?explore=Reaction" target="_blank"><label>Explore Reactions</label></a></a>
					</div>
                
					<div id="viewmedia" class="viewoptions">
					<a href="./explore.py?explore=Media" target="_blank"><img src="https://bl3302files.storage.live.com/y4mcX5xAoK8Bs5EedW-DdXGW_eqo0t2WeEL2YmeIb6w7z3BichOtN-630XTZFUqFsR_OM8sgasqPzi7KO02W8Wydw1dMCf_AHvCLQrGUtBpHqmZBEEdX8AyqYNMCXHFa-iZZE_dTGPEgbQs7mrzOgb5y7EnKMNEpjVGNY1RGhQIKxw_Z5X6nge1pMQgLBzk3nYm?width=279&height=181&cropmode=none"><br><a class="clickme" href="./explore.py?explore=Media" target="_blank"><label>Explore Media</label></a></a>
					</div>                
                
                
                
                
				</div>

				</div>
				
			</div> ''')
print('''<div id="mainfooter" class="maindiv">
			<p>Boston University &copy; 2021</p>
			</div>
		</div> ''')
   
print("</body>")
print("</html>")
