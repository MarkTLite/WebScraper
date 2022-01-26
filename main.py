
import app


def get_details_dict(emails,company_name):     
    data_dict = {}
    for email in emails:           
        if company_name.lower() in str(email).lower():
            data_dict["company_name"] = company_name
            data_dict["email_address"] = email                    
            break
                
    return(data_dict) 

def write_to_file(data_dict):
    output_file = open('output.txt', mode= 'a', encoding='utf-8')
    output_file.write(data_dict['company_name']+" : "+ data_dict['email_address']+'\n')
    output_file.close()

def main(): 
    try:
        file = open("companies.txt", mode='r', encoding='utf-8')
        for eachline in file:
            company_name = eachline.strip()
            print(f"-> Extracting details for: {company_name}")
            # Get google search results response content
            response = app.get_google_urls(company_name) 
            # Extract company page urls from the search results response
            company_urls = app.choose_needed_urls(response,company_name)
            # Extract company homepage URL from the company page urls        
            homepage = app.choose_company_homepage(company_urls,company_name)
            #Get urs on company home page        
            fb_response = app.get_response(homepage)        
            print("\nHomePage Response status_code: ", fb_response.status_code)
            a1_tags = app.get_a_tags(fb_response.content)    
            # Get Company About page  
            about_link = app.get_company_about(a1_tags,homepage)
            print(about_link) 
            #Get required data from about page                  
            emails = app.get_emails(about_link)
            data_dict = get_details_dict(emails,company_name)   
            #Write the resuts to an output fie
            print(emails)
            write_to_file(data_dict)

    finally:
        file.close() 
        print("file closed")

#main()
x='<a class="jkjk" href="http://example.com/" id="link1">Lorem Ipsum Dolo</a>'
print('<a' and '</a>' in x)