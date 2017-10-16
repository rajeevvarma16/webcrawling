from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup 

def array_pages(url):
	print url
	pages = []
	for i in range(1,100):     
		my_url_allpages = url.format(i)
		pages.append(my_url_allpages)
	return pages

#my_url = 'https://www.monster.se/jobb/sok/Data-IT_4?intcid=swoop_BrowseJobs_Data-IT'
#opening up connection and grabbing the page
if __name__ == "__main__":
	'''
	my_url = 'https://www.monster.se/jobb/sok/Data-IT_4?intcid=swoop_BrowseJobs_Data-IT&page={0}'
	array_pages = array_pages(my_url)
	print array_pages


	for my_url in array_pages:
		try:
			uClient = uReq(my_url)
			pageHtml = uClient.read()
			print pageHtml
			uClient.close()
			#print pageHtml

			page_soup = soup(pageHtml,"html.parser")
			#print page_soup

			print page_soup.h1.text.strip()
			containers = page_soup.findAll("article",{"class":"js_result_row"})
			container = containers[0]
			for container in containers:
				job_title = container.findAll("div",{"class":"jobTitle"}) 
				print job_title[0].text.strip()
				company = container.findAll("div",{"class":"company"}) 
				print company[0].text.strip()
				location = container.findAll("div",{"class":"location"}) 
				print location[0].text.strip()
				print ('-------------------------------')
		except AttributeError:
			break
	'''
	my_url_step = 'https://www.stepstone.se/lediga-jobb-i-hela-sverige/data-it/sida{0}'
	array_pages_stepstone = array_pages(my_url_step)    
	for my_url_stepstone in array_pages_stepstone:
		try:
			uClient2 = uReq(my_url_stepstone)
			pageHtml2 = uClient2.read()
			#print pageHtml
			uClient2.close()
			#print pageHtml

			page_soup2 = soup(pageHtml2,"html.parser")
			#print page_soup

			#print page_soup.h1.text.strip()
			containers2 = page_soup2.findAll("div",{"class":"description"})
			#container = containers[0]
			for container in containers2:
				companyName = container.span.a.text
				print companyName
				
				job_title = container.h5.a.text
				print job_title 
				#print job_title[0].text.strip()
				#location = container.findAll("span",{"class":"subtitle"}) 
				#print company[0].text.strip()
				location2 = container.findAll("span",{"class":"text-opaque"})

				print location2[1].text
				print ('-------------------------------')

		except AttributeError:
			break
		