from unittest import TestCase
import pytest
from app import *

#Class for testing get_response()
class TestResponses(TestCase):
    #Test get_response's status
    def test_get_response_status(self):        
        result = get_response('https://www.google.com')
        self.assertEqual(result.status_code, 200)

#Class for testing get_google_urls()
class TestGetGoogleUrls(TestCase):
    #testing response status
    def test_get_google_urls_status(self):   
        result = get_google_urls('https://www.google.com')
        self.assertEqual(result.status_code, 200)

#Class for testing choose_needed_urls()
""" class TestChooseNeededUrls(TestCase):
    #Test for returning proper urls
    def test_choose_needed_urls(self):
        company_name = "ucc"
        sample_res = requests.get(f"https://www.google.com/search?q={company_name}")
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
        for eachdict in choose_needed_urls(sample_res,company_name):
            print(eachdict)
            self.assertIsNotNone(re.match(regex, eachdict['company_url'])) """

class TestGet_A_tags(TestCase):
    #Check for presence of <a> tags 
     def test_get_a_tags(self):
        sample_html = """
            <html><head><title>Lorem Ipsum Dolor</title></head>
            <body>
            <a href="http://example.com/" class="jkjk" id="link1">Lorem Ipsum Dolo</a>,
            <p class="title"><b>Lorem Ipsum Dolor</b></p>
            <a href="http://example.com/" class="kkkr" id="link3">Lorem Ipsum Dolo</a>
            <p class="story">Lorem Ipsum Dolor; and Lorem Ipsum Dolor            
            <a href="http://example.com/" class="jkjk" id="link2">Lorem Ipsum Dolo</a> and            
            Lorem Ipsum DolLorem Ipsum DolLorem Ipsum Dol</p>            
            <p class="story">...</p>
        """
        links = get_a_tags(sample_html)
        for link in links:        
            self.assertTrue('<a' and '</a>' in str(link))
            
#
class TestChooseCompanyHomepage(TestCase):
    def test_choose_company_homepage(self):
        company_urls = [{'company': 'ucc', 'company_url': '/?sa=X&ved=0ahUKEwjrh8-w-s31AhWuTmwGHdkeDPcQOwgC'},
                        {'company': 'ucc', 'company_url': '/ucc.org/'}]
        company_name ='ucc'
        homepage = choose_company_homepage(company_urls,company_name)
        self.assertGreater(len(homepage),0)
        


class TestGetCompanyAbout(TestCase):
    def test_fb_about(self):
        sample_a1_tags = get_a_tags("""          
            <a href="http://example.com/about" class="jkjk" id="link1">Lorem Ipsum Dolo</a>            
            <a href="http://example.com/contact" class="kkkr" id="link3">Lorem Ipsum Dolo</a>""")
        homepage = 'http://facebook.com/'
        about_link = get_company_about(sample_a1_tags,homepage)
        self.assertTrue('about' or 'contact' in about_link)            

class TestGetEmails(TestCase):
     def test_get_emails(self):
        emails = get_emails('https://nbs.ug/about-us/')
        expression = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        for email in emails:     
            self.assertIsNotNone(re.match(expression, email))
       
#pytest runner
pytest.main()
     
 

    
    
