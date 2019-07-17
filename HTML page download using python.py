import os
import argparse
import time
import requests

'''argparse module is used to get the input url from the command line. The url is
stored in variable 'a''''

parser=argparse.ArgumentParser(description='Get the url')
parser.add_argument('host',action='store',help='The user url gets tagged to the host')
b=parser.parse_args()
a=b.host
#print(a) To check if the url is present in variable 'a'

'''req module is used to establish a connection with the given url
and write the html code in text format'''

response = requests.get(a) # print(response) displays the status code of connection
moment = time.strftime("%Y-%b-%d_____%H_%M_%S", time.localtime()) 
f = open('/home/jovyan/final/outputs/output' + moment + '.txt', 'w') #create a file with the filename as "output Month-Date-Year___Hours-Min-Sec.txt"
f.write(response.text) #can use response.content also inorder to get the html content in bytes. The write command writes the data into the output file created 
f.close()
