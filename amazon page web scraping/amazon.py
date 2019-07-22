import requests
from bs4 import BeautifulSoup
import argparse
import logging
import logging.handlers as handlers

#url = 'https://www.amazon.in/Waterfall-Storage-Additional-Exchange-Offers/dp/B07PSHLRJP/ref=sr_1_8?keywords=mobile&qid=1563347923&s=gateway&smid=A14CZOWI0VEHLG&sr=8-8'
#url = 'https://www.amazon.in/Moto-Plus-Indigo-Black-battery/dp/B077PWK5BT/ref=sr_1_10?keywords=mobile&qid=1563347923&s=gateway&sr=8-10'

logger = logging.getLogger('test')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
logHandler = handlers.TimedRotatingFileHandler('timed_app.log', when='M', interval=2)
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

parser = argparse.ArgumentParser(description='Get the url')
parser.add_argument('host',action='store', help='The user url gets stored in the host')
a=parser.parse_args()
url=a.host
#print (url)


response = requests.get(url)
b=response.text
soup = BeautifulSoup(b,'html.parser')
c=soup.title.string
d=c.split()
e=(''.join(c[0:11]))
#print(e)

f = soup.find('span',{'id':'priceblock_ourprice'})
if f is None:
    f = soup.find('span',{'id':'priceblock_dealprice'})
    for f in soup.find_all('span',{'class':"a-size-medium a-color-price priceBlockDealPriceString"}):
        g = f.string
    #print("e2 =",g)
    h=e+' '+g
   # print("check1:",h)
    logger.info(h)
    
else:
    for f in soup.find('span',{'class':"a-size-medium a-color-price priceBlockBuyingPriceString"}):
        i = f.string
    #print("e1 =",i)
    j= e+' '+i
    #print("check2:",j)
    logger.info(j)
    
