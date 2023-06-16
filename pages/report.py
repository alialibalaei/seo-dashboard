from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

class ReportSeo():
    url=""
    def analyze_seo(self):

        response = requests.get(self.url)
        dic={
            "title":"",
            "description":"",
            "h1":"",
            "h2":"",
            "h3":"",
            "h4":"",
            "h5":"",
            "h6":"",
            "robots":False,
            "sitemap":False,
            
            }
        soup = BeautifulSoup(response.content,"html.parser")
        if response.status_code==200:
            l=[]
            if  soup.find('title'):
                l.append(soup.find('title').text)
                if len(l[0])<=5:
                    l.append("bad")
                elif len(l[0])>=6 and len(l[0])<=15:
                    l.append("good")
                elif len(l[0])>15:
                    l.append("very good")            

            else:
                l.append("")
                l.append("")

            dic["title"]=l    
            
            
            
            l=[]
            if soup.findAll("meta", attrs={"name": "description"}):
                
                l.append(soup.find("meta", attrs={"name": "description"}).get("content"))
                if len(l[0])<=50:
                    l.append("bad")
                elif len(l[0])>=50 and len(l[0])<=100:
                    l.append("good")
                elif len(l[0])>100:
                    l.append("very good")            

            else:
                l.append("")
                l.append("")

            dic["description"]=l    
            
            
            
            
            l=[]
            if soup.find_all('h1'):
                for i in soup.find_all('h1'):
                    if len(i.text)<=5:
                        l.append([i.text,"bad"])
                    elif len(i.text)>=6 and len(i.text)<=15:
                        l.append([i.text,"good"])
                    elif len(i.text)>15:
                        l.append([i.text,"very good"])
                        
            dic["h1"]=l
            
            
            l=[]
            if soup.find_all('h2'):
                for i in soup.find_all('h2'):
                    if len(i.text)<=5:
                        l.append([i.text,"bad"])
                    elif len(i.text)>=6 and len(i.text)<=15:
                        l.append([i.text,"good"])
                    elif len(i.text)>15:
                        l.append([i.text,"very good"])  
                        
            dic["h2"]=l
            
            
            l=[]
            if soup.find_all('h3'):
                for i in soup.find_all('h3'):
                    if len(i.text)<=5:
                        l.append([i.text,"bad"])
                    elif len(i.text)>=6 and len(i.text)<=15:
                        l.append([i.text,"good"])
                    elif len(i.text)>15:
                        l.append([i.text,"very good"])  
                        
            dic["h3"]=l


            l=[]
            if soup.find_all('h4'):
                for i in soup.find_all('h4'):
                    if len(i.text)<=5:
                        l.append([i.text,"bad"])
                    elif len(i.text)>=6 and len(i.text)<=15:
                        l.append([i.text,"good"])
                    elif len(i.text)>15:
                        l.append([i.text,"very good"])  
                        
            dic["h4"]=l
            
            
            l=[]
            if soup.find_all('h5'):
                for i in soup.find_all('h5'):
                    if len(i.text)<=5:
                        l.append([i.text,"bad"])
                    elif len(i.text)>=6 and len(i.text)<=15:
                        l.append([i.text,"good"])
                    elif len(i.text)>15:
                        l.append([i.text,"very good"])  
                        
            dic["h5"]=l
            
            
            l=[]
            if soup.find_all('h6'):
                for i in soup.find_all('h6'):
                    if len(i.text)<=5:
                        l.append([i.text,"bad"])
                    elif len(i.text)>=6 and len(i.text)<=15:
                        l.append([i.text,"good"])
                    elif len(i.text)>15:
                        l.append([i.text,"very good"])  
                        
            dic["h6"]=l
            domain=urlparse(self.url).netloc
            robot = requests.get("https://"+domain+"/robots.txt")

            if robot.status_code==200:
                dic["robots"]=True
                if "Sitemap" in robot.text:
                    dic["sitemap"]=True
            
            return dic
        return False
# print(analyze_seo("https://blog.faradars.org/%d8%af%d8%b3%d8%aa%d9%88%d8%b1%d8%a7%d8%aa-%d9%84%db%8c%d9%86%d9%88%da%a9%d8%b3/")['description'])
