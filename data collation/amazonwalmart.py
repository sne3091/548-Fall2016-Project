import json
import csv
import re
from collections import OrderedDict


def getamazonwalmart():
    a1=[]
    w1=[]
    a1d=OrderedDict()
    w1d=OrderedDict()

    #read linked record lines for amazon and walmart
    with open("amazon-walmart.csv") as f:
        r = csv.DictReader(f)
        for i, line in enumerate(r):
            a1.append(int(line["amazon"]))
            w1.append(int(line["walmart"]))
    
    a1stays=a1[:]
    w1stays=w1[:]

    #get price_min for these linked records
    with open("amazon_clean.csv") as am:
        ra = csv.DictReader(am)
        for i,line in enumerate(ra):
            if i in a1:
                a1d[i]=float(line["price_min"])
    with open("walmart_clean.csv") as wm:
        re = csv.DictReader(wm)
        with open("test.txt","w") as out:
            for i,line in enumerate(re):
                if i in w1:
                    w1d[i]=float(line["price_min"]

    #compare the price_min between the two and keep only the ones with lower price else remove                                 
    for x,y in zip(a1,w1):
        if a1d[x]<w1d[y]:
            w1stays.remove(y)
        else:
            a1stays.remove(x)
                                 
    #final removed records list                             
    a1removed=list(set(a1)-set(a1stays))
    w1removed=list(set(w1)-set(w1stays))
    return a1removed,w1removed

if __name__ == '__main__':
    a,w=getamazonwalmart()
    print(a)
    print(w)
            
