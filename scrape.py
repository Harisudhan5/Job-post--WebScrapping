from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

with open("companys.csv","r") as file:
    reader = csv.reader(file)
    data = list(reader)
    c = 0
    for ptrs in range(902):
        c_url = data[ptrs][0]
        ul = c_url

        reqs = Request(
            url=ul, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        webpage = urlopen(reqs)
        soup = BeautifulSoup(webpage,"html.parser")
        box = soup.find("div",class_="et_pb_column et_pb_column_2_5 et_pb_column_3 et_pb_css_mix_blend_mode_passthrough et-last-child")
        inner_box = box.find_all("div",class_="detail")
        list_container = []

        ran = inner_box[0].find_all("a")
        leaders = ""
        for ko in ran:
            if ko.text == "Leader":
                break
            leaders = str(ko.text.strip())+" & " + leaders
        if len(inner_box) == 12:
            print("1",leaders)
            employee_count = inner_box[1].a.text
            print("2",employee_count)
            funding_type = inner_box[2].a.text
            print("3",funding_type)
            location = inner_box[3].a.text
            print("4",location)
            foundedd = inner_box[4].text
            ind = foundedd.index(":")
            founded = foundedd[ind+1::].strip()
            print("5",founded)
            not_val = "Null"

            for i in range(0,len(inner_box)):
                if str(inner_box[i].label.text).strip() == "Software Type:":
                    software_type = inner_box[i].a.text
   
                elif str(inner_box[i].label.text).strip() == "Industry:":
                    industry_type = inner_box[i].a.text

                elif str(inner_box[i].label.text).strip() == "Category:":
                    cate = inner_box[i].a.text

                elif str(inner_box[i].label.text).strip() == "Size:":
                    size = inner_box[i].a.text
                else:
                    continue
            try:
                print("6",software_type)
            except:
                print("Null")
                software_type = not_val
            try:
                print(industry_type)
            except:
                industry_type = not_val
                print("Null")
            try:
                print(cate)
            except:
                cate = not_val
                print(cate)
            print("9",size)
            '''if str(inner_box[5].label.text).strip() == "Software Type:":
                software_type = inner_box[5].a.text
                print("6",software_type)
                id1 = 6 
            else:
                software_type = "Null"
                id1 = 5
            if str(inner_box[id1].label.text).strip() == "Industry:":
                industry_type = inner_box[id1].a.text
                print("7",industry_type)
                id2 = id1 +1
            else:
                industry_type = "Null"
                id2 = id1
                print("7",industry_type)
            if str(inner_box[id2].label.text).strip() == "Category":
                cate = inner_box[id2].a.text
                print("8",cate)
                id3 = id2 + 1
            else:
                cate = "Null"
                id3 = id2
                print("8",cate)'''
            '''if str(inner_box[id3].label.text).strip() == "Size":
                size = inner_box[id3].a.text
                print("9",size)
            else:
                size = "Null"
                print("9",size)'''
            website = inner_box[-3].a.text
            print("10",website)
            linkedin = inner_box[-2].a.text
            print("11",linkedin) 
            address = inner_box[-1].a.text
            print("12",address)
        else:
            print("1",leaders)
            employee_count = inner_box[1].a.text
            print("2",employee_count)
            funding_type = inner_box[2].a.text
            print("3",funding_type)
            location = inner_box[3].a.text
            print("4",location)
            foundedd = inner_box[4].text
            ind = foundedd.index(":")
            founded = foundedd[ind+1::].strip()
            print("5",founded)
            not_val = "Null"
          
            for i in range(0,len(inner_box)):
                if str(inner_box[i].label.text).strip() == "Software Type:":
                    software_type = inner_box[i].a.text
              
                elif str(inner_box[i].label.text).strip() == "Industry:":
                    industry_type = inner_box[i].a.text
                
                elif str(inner_box[i].label.text).strip() == "Category:":
                    cate = inner_box[i].a.text
                  
                elif str(inner_box[i].label.text).strip() == "Size:":
                    size = inner_box[i].a.text
                else:
                    continue
            try:
                print("6",software_type)
            except:
                print("Null")
                software_type = not_val
            try:
                print("7",industry_type)
            except:
                industry_type = not_val
            try:
                print("8",cate)
            except:
                cate = not_val
                print(cate)
            print("9",size)
            '''if str(inner_box[5].label.text).strip() == "Software Type:":
                software_type = inner_box[5].a.text
                print("6",software_type)
                id1 = 6
            else:
                software_type = "Null"
                id1 = 5
            if str(inner_box[id1].label.text).strip() == "Industry:":
                industry_type = inner_box[id1].a.text
                print("7",industry_type)
                id2 = id1 +1
            else:
                industry_type = "Null"
                id2 = id1
                print("7",industry_type)
            if str(inner_box[id2].label.text).strip() == "Category":
                cate = inner_box[id2].a.text
                print("8",cate)
                id3 = id2 +1
            else:
                cate = "Null"
                print("8",cate)
                id3 = id2'''
            

            """if str(inner_box[id3].label.text).strip() == "Size":
                size = inner_box[id3].a.text
                print("9",size)
            else:
                size = "Null"
                print("9",size)"""

            website = inner_box[-3].a.text
            
            print("10",website)
            linkedin = inner_box[-2].a.text
            print("11",linkedin) 
            address = inner_box[-1].a.text
            print("12",address)
        with open("company.csv") as f2:
            rdr = csv.reader(f2)
            for indux,valse in enumerate(rdr):
                if indux == ptrs:
                    c_name = valse[0]
        print(c_name)
            
        groupd = [
            [c_name,leaders,founded,employee_count,funding_type,industry_type,cate,software_type,size,website,linkedin,address]
        ]

        with open("greglist_data.csv","a") as f3:
           writ = csv.writer(f3)
           writ.writerows(groupd)
        

        c = c + 1
        print("----------> ",c)
            
