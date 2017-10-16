from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup 
if __name__ == '__main__':
	
	pages = []
	for i in range(1,100):      
	    my_url = 'https://www.monster.se/jobb/sok/Data-IT_4?intcid=swoop_BrowseJobs_Data-IT&page={0}'.format(i)
	    pages.append(my_url)
	for my_url in pages:
		try:
			uClient = uReq(my_url)
			pageHtml = uClient.read()
			uClient.close()
			page_soup = soup(pageHtml,"html.parser")
			print page_soup.h1.text.strip()
			containers = page_soup.findAll("article",{"class":"js_result_row"})
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
	pages_stepstone = []
	for i in range(1,100):      
	    my_url_stepstone = 'https://www.stepstone.se/lediga-jobb-i-hela-sverige/data-it/sida{0}/'.format(i)
	    pages_stepstone.append(my_url_stepstone)
	for my_url_stepstone in pages_stepstone:
		try:
			uClient2 = uReq(my_url_stepstone)
			pageHtml2 = uClient2.read()
			uClient2.close()
			page_soup2 = soup(pageHtml2,"html.parser")
			containers2 = page_soup2.findAll("div",{"class":"description"})
			for container in containers2:
				companyName = container.span.a.text
				print companyName
				job_title = container.h5.a.text
				print job_title 
				location2 = container.findAll("span",{"class":"text-opaque"})
				print location2[1].text
				print my_url_stepstone
				print ('-------------------------------')
		except AttributeError:
			break
			

