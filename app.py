import requests
import requests  
from bs4 import BeautifulSoup
import re



def get_response(url,co_query={}):
    response = requests.get(url,params=co_query)   
    return(response)

def choose_needed_urls(response,company_name):    
    a_tags = get_a_tags(response.content)
    company_urls = []
    for url in a_tags:
        my_dict = {
           "company": company_name,
           "company_url": url.get('href')
        }
        company_urls.append(my_dict)
    #print("\n",company_urls)
    return(company_urls)

def get_a_tags(html):
    soupObj = BeautifulSoup(html,'html.parser')
    a_tags = soupObj.find_all('a')   
    return a_tags

def get_google_urls(company_name):     
    co_query = {'q':company_name}    
    response = get_response('https://www.google.com/search?',co_query)        
    print("\nGoogle Search Response status_code: ",response.status_code)
    return(response)


def choose_company_homepage(company_urls,company_name):
    fb_urls = []
    for company in company_urls:
        expression = r'/'+company_name+r'\..*?/|/www\.'+company_name+r'\..*?/'            
        match = re.findall(expression, company['company_url'])
        print(match)
        if match:
            for lnk in match:                    
                fb_link = 'https:/'+lnk
                if fb_link not in fb_urls:
                    fb_urls.append(fb_link)
    print("\nfb_urls",fb_urls)
    homepage = fb_urls[0]
    return(homepage)

def get_company_about(a1_tags,homepage):
    for url in a1_tags:
        expression1 = r'about.*?/|contact.*?/'            
        match1 = re.findall(expression1, url.get('href'))
        print("match1: ",match1)
        about_link = ''
        if match1:                                   
            about_link = homepage + match1[0]
            return(about_link)

def get_emails(about_link):
    about_response = get_response(about_link)        
    print("\nAbout Response status_code: ",about_response.status_code)         
    expression2 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(expression2, about_response.text)
    return(emails)


