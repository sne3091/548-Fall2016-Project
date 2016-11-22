from bs4 import BeautifulSoup
from urllib.request import urlopen
import codecs
import json
import collections
import pprint
import requests
    
if __name__ == '__main__':
    links=[]
    with open("ebay_links final.txt","r") as inp:
        for line in inp:
            links.append(line.strip())
    #print(links)
    with open("ebay_extract_desc.json","w") as out: #output file
        out.write("[")    
        for l in links:
            #l=links[j]
            if not(l==links[0]):
                out.write(",\n")
            #print(l)
            page = requests.get(l,headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
            html=page.content
            soup=BeautifulSoup(html,'html.parser')
            #print(soup.prettify())
            #out.write(soup.prettify())
            
            t=soup.find('title').contents[0].strip() #extract title
            title=t.split("|")[0].strip()
            #print(title)
            r=soup.findAll('div',class_="ebay-star-rating") #extract rating
            if r==None:
                rating="No rating available"
            else:
                for i in r:
                    rating=i.get('aria-label')
                    if rating==None:
                        continue
                    else:
                        if rating.startswith("0.0"):
                            rating="No rating available"
            #print(rating)
            p=soup.find('span',id="prcIsum") #extract price
            if p==None:
                p1= soup.find('span',id="mm-saleDscPrc")
                price=p1.contents[0].strip()
            else:
                price=p.contents[0].strip()
            #print(price)
            image=soup.find('img',id="icImg").get('src') #extract image URL
            #print(image)
            
            d=soup.find('div', class_="itemAttr") #extract description
            description=d.text.replace("\n","").replace("\t","")
            #print(description)
            
            entity=collections.OrderedDict() #Creating the JSON object for each product
            entity["URL"]=l
            if title is not None:
                entity["Title"]=title
            if rating is not None:
                entity["Rating"]=rating  
            if price is not None:
                entity["Price"]=price
            if image is not None:
                entity["Image"]=image
            if description is not None:
                entity["Description"]=description
            out.write(json.dumps(entity))
            
        out.write("]")
            
