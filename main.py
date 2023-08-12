from bs4 import BeautifulSoup
import requests

html_user = requests.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0").text
soup = BeautifulSoup(html_user,"lxml")

jobs = soup.find_all("div",class_ = "base-search-card__info")
cnt = 0
for job in jobs:
    cnt  = cnt + 1
    role_name_ = job.find("h3",class_ = "base-search-card__title").text.strip()
    company_name = job.find("h4",class_ = "base-search-card__subtitle").text.strip()
    loc_and_posted = job.find("div",class_ = "base-search-card__metadata")
    company_location = loc_and_posted.find("span",class_ = "job-search-card__location").text.strip()
    posted = loc_and_posted.time.text.replace("\n","").strip()
    dated = loc_and_posted.time["datetime"]
    
    print(f"------( {cnt} )-----------")
    print(f"""
    Company Name : {company_name}
    Role         : {role_name_}
    Location     : {company_location}
    Posted       : {posted}
    Date         : {dated}
        """)