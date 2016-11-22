from bs4 import BeautifulSoup
from urllib.request import urlopen
import codecs
import json
import collections
import pprint
import requests
    
if __name__ == '__main__':
    links=[]
    with open("walmart_links final.txt","r") as inp:
        for line in inp:
            links.append(line.strip())
    #print(links)
    with open("walmart_extract_desc.json","w") as out: #output file
        out.write("[")    
        for l in links:
            if not(l==links[0]):
                out.write(",\n")
            #print(l)
            page = requests.get(l,headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
            html=page.content
            soup=BeautifulSoup(html,'html.parser')
            #print(soup.prettify())
            out.write(soup.prettify())
            
            t=soup.find('title').contents[0].strip() #extract title
            title=t.split("-")[0].strip()
            #print(title)
            r=soup.find('div',class_="review-summary Grid") #extract rating
            if r==None:
                rating="No rating available"
            else:
                rev=r.find('p',class_="heading-e")
                rating=rev.contents[0].split("|")[1].strip()
            #print(rating)
            p=soup.find('div',class_="js-price-display Price Price--stylized Price--large hide-content display-inline-m price-display") #extract price
            price=p.text.strip()
            #print(price)
            i=soup.find('img',class_="product-image js-product-image js-product-primary-image") #extract image URL
            image=i.get('src').split("?")[0].strip()
            #print(image)
            
            d=soup.find('div', class_="about-item-preview-text js-about-item-preview-text") #extract description
            description=d.text.strip()
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

            
            
