import json
import csv
import re
from collections import OrderedDict


def getwalmartebay():
    w1=[]
    e1=[]
    w1d=OrderedDict()
    e1d=OrderedDict()

    #read linked record lines for walmart and ebay
    with open("walmart-ebay.csv") as f:
        r = csv.DictReader(f)
        for i, line in enumerate(r):
            w1.append(int(line["walmart"]))
            e1.append(int(line["ebay"]))
    
    w1stays=w1[:]
    e1stays=e1[:]

    #get price_min for these linked records
    with open("walmart_clean.csv") as wm:
        ra = csv.DictReader(wm)
        for i,line in enumerate(ra):
            if i in w1:
                w1d[i]=float(line["price_min"])
    with open("ebay_clean.csv") as eb:
        re = csv.DictReader(eb)
        with open("test.txt","w") as out:
            for i,line in enumerate(re):
                if i in e1:
                    e1d[i]=float(line["price_min"])

    #compare the price_min between the two and keep only the ones with lower price else remove
    for x,y in zip(w1,e1):
        if w1d[x]<e1d[y]:
            e1stays.remove(y)
        else:
            w1stays.remove(x)

    #final removed records list
    w1removed=list(set(w1)-set(w1stays))
    e1removed=list(set(e1)-set(e1stays))
    return w1removed,e1removed

if __name__ == '__main__':
    w,e=getwalmartebay()
    print(w)
    print(e)
            
