import urllib
from bs4 import BeautifulSoup
'''from pdfparser import getTables'''
from StringIO import StringIO
def download_data():
	base_url = "http://www.munlima.gob.pe/"
	service_url = "gobierno-abierto-municipal/transparencia/mml/informacion-de-contrataciones/"
	#Param extra

	#Dictionary of elements 
	#items = {
	#	"gasto_publicidad":"gastos-de-publicidad/gastos-de-publicidad",
	#
	#}
	report_url = "gastos-de-publicidad/gastos-de-publicidad"
	#Name
	name = "gasto_publicidad"
	#
	download_url = base_url + service_url + report_url

	html = urllib.urlopen(download_url).read() #It may fail ., oh well 
	soup = BeautifulSoup(html)


	tabs = soup.find("div", {"class", "nn_tabs_content"}).findAll("div", {"class": "nn_tabs_item"})
	#
	output = {}
	#Getting variables
	for tab in tabs:
    		year = tab.find("h2", {"class", "nn_tabs_title"}).contents
	    	trimestres = tab.findAll("li")
    		year = str(year)
    		output[year] = []
    		links = []
    		for trimestre in trimestres:
        		links.append(base_url + trimestre.find("a")['href'])
    		print links
    		#print year
    		#now the magic
    		for link in links:
			print year
			print link
  #      		output[year].append(download_parse_pdf(link))
			#pass

def download_parse_pdf(url):
    contents = urllib.urlopen(url).read()
    #tables = getTables(StringIO(contents))    
    print tables

download_data()
