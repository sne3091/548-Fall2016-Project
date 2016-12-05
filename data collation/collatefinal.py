import json
import csv
import re
from collections import OrderedDict
from walmartebay import*
from amazonebay import *
from amazonwalmart import*

#get removed records from amazon, ebay, walmart (removed due to higher price among linked records)
a1,w1=getamazonwalmart()
a2,e1=getamazonebay()
w2,e2=getwalmartebay()

#get final set of removed records
a=set(a1+a2)
e=set(e1+e2)
w=set(w1+w2)

#write records from amazon, ebay, walmart product files except the removed ones
with open("amazon_clean.csv",'r') as am:
    re = csv.DictReader(am)
    with open("gifts.csv",'w',newline='') as out:
        dw= csv.DictWriter(out, delimiter=',', fieldnames=re.fieldnames)
        dw.writerow(dict((fn,fn) for fn in re.fieldnames))
        am.close()
        with open("amazon_clean.csv",'r') as am:
            re = csv.DictReader(am)
            for i,line in enumerate(re):
                if i in a: #removed hence continue
                    continue;
                dw.writerow(line)
        with open("ebay_clean.csv",'r') as eb:
            re = csv.DictReader(eb)
            for i,line in enumerate(re):
                if i in e: #removed hence continue
                    continue;
                dw.writerow(line)
        with open("walmart_clean.csv",'r') as wm:
            re = csv.DictReader(wm)
            for i,line in enumerate(re):
                if i in w: #removed hence continue
                    continue;
                dw.writerow(line)
                        
