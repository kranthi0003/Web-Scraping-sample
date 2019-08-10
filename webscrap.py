#author- Kranthi Kiran

import time 
import requests
from bs4 import BeautifulSoup
import notify2 
#requests.get is used to get the data from the server,inturn the server sends the html content of a particular webpage.
page1=requests.get('https://www.spoj.com/users/atiaditya3/') 
page2=requests.get('https://www.spoj.com/users/kamesh11/')
#Beautiful soup is used to parse the html content into a tree structure from where we can access html data.
soup1=BeautifulSoup(page1.content,'html.parser')
soup2=BeautifulSoup(page2.content,'html.parser')
#find returns the content with a particular class-name (or) id-name (or) tag-name in an html content.
name1=soup1.find(class_='dl-horizontal profile-info-data profile-info-data-stats')
name2=soup2.find(class_='dl-horizontal profile-info-data profile-info-data-stats')
#the content what I want is stored in <dd> tag,hence i'm finding all 'dd' tags.
details_adi=name1.find_all('dd')
details_kam=name2.find_all('dd')
#from here just manipulating strings and printing
str1=str(details_adi[0])
adi_correct=str1[4:len(str1)-5]
str2=str(details_adi[1])
adi_submissions=str2[4:len(str2)-5]
str3=str(details_kam[0])
kam_correct=str3[4:len(str3)-5]
str4=str(details_kam[1])
kam_submissions=str4[4:len(str4)-5]
#notify2 is python module which helps to send a notification to our device.
try:
    if notify2.init("adi"):
        string1="Correct submissions: "+adi_correct+"\nTotal Submissions: "+adi_submissions
        alert=notify2.Notification("SPOJ-Aditya\n",string1)
        alert.show()
except:
    print("Some error occured")
time.sleep(3)
try:
    if notify2.init("kam"):
        string2="Correct submissions: "+kam_correct+"\nTotal Submissions: "+kam_submissions
        alert=notify2.Notification("SPOJ-Kamesh\n",string2)
        alert.show()
except:
    print("Some error occured")

#end of a simple scraping,cheers:)
