from bs4 import BeautifulSoup
from urllib.request import urlopen
import codecs
import json
import collections
import pprint
import requests
    
if __name__ == '__main__':
    links=[]
    with open("amazon_links final.txt","r") as inp:
        for line in inp:
            links.append(line.strip())
    #print(links)
    with open("amazon_extract_desc.json","w") as out: #output file
        out.write("[")    
        for l in links:
            if not(l==links[0]):
                out.write(",\n")
            #print(l)
            page = requests.get(l,headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
            html=page.content
            soup=BeautifulSoup(html,'html.parser')
            #print(soup.prettify())
            
            title=soup.find('span',id='productTitle').contents[0].strip() #extract title
            #print(title)
            t=soup.find('span',id='priceblock_ourprice') #extract price
            if t==None:
                t1=soup.find('span',id='priceblock_saleprice')
                if t1==None:
                    t2=soup.find('span',class_='a-color-price')
                    price=t2.contents[0].strip()
                else:
                    price=t1.contents[0].strip()
            else:
                price=t.contents[0].strip()
            #print(price)
            i=soup.find('img',class_="a-dynamic-image miniATFImage") #extract image URL
            if i==None:
                i1=soup.find('div',class_="imgTagWrapper")
                if i1==None:
                   image="No image available"
                else:
                    img=i1.find('img')
                    image=img.get('src')    
            else:
                image=i.get('src')
            #print(image)
            r=soup.find('span',id='acrPopover') #extract rating
            if r==None:
                rating="No rating available"
            else:
                rating=r.get('title')
            #print(rating)
            
            d=soup.find('div',id="feature-bullets") #extract description
            des=d.findAll('span',class_="a-list-item")
            description=""
            for desc in des:
                description+=desc.text.strip()+". "
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

