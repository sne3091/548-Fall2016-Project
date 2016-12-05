import json
import csv
import re
from collections import OrderedDict

def getamazonebay():
    a1=[]
    e1=[]
    a1d=OrderedDict()
    e1d=OrderedDict()

    #read linked record lines for amazon and ebay
    with open("amazon-ebay.csv") as f:
        r = csv.DictReader(f)
        for i, line in enumerate(r):
            a1.append(int(line["amazon"]))
            e1.append(int(line["ebay"]))
    
    a1stays=a1[:]
    e1stays=e1[:]

    #get price_min for these linked records
    with open("amazon_clean.csv") as am:
        ra = csv.DictReader(am)
        for i,line in enumerate(ra):
            if i in a1:
                a1d[i]=float(line["price_min"])
    with open("ebay_clean.csv") as eb:
        re = csv.DictReader(eb)
        for i,line in enumerate(re):
            if i in e1:
                e1d[i]=float(line["price_min"])

    #compare the price_min between the two and keep only the ones with lower price else remove            
    for x,y in zip(a1,e1):
        if a1d[x]<e1d[y]:
            e1stays.remove(y)
        else:
            a1stays.remove(x)

    #final removed records list
    a1removed=list(set(a1)-set(a1stays))
    e1removed=list(set(e1)-set(e1stays))
    return a1removed,e1removed

if __name__ == '__main__':
    a,e=getamazonebay()
    print(a)
    print(e)
