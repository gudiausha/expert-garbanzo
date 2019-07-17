import os
import sys
import time
import requests

a = str(sys.argv[1])
response = requests.get(a) # print(response) displays the status code of connection
moment = time.strftime("%Y-%b-%d_____%H_%M_%S", time.localtime()) 
f = open('/home/jovyan/final/outputs/output' + moment + '.txt', 'w') #create a file with the filename as "output Month-Date-Year___Hours-Min-Sec.txt"
f.write(response.text) #can use response.content also inorder to get the html content in bytes. The write command writes the data into the output file created 
f.close()
