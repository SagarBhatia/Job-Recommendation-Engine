import docxpy
import pandas as pd
from bs4 import BeautifulSoup as bs
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#File Location
f='D:\Downloads\Basic-Resume-Template_Word\Word\Basic Resume Template.docx'
text=docxpy.process(f)

#soup=bs(text,'lxml')
print("---------------------")
#df=pd.read_csv("D:\Downloads\skills.csv")
#df2=df['SKILLS']
skills=['python','php','java','javascript','perl','android','c++','c','wordpress','photoshop','graphic design','cloud','asp.net','vb.net','.net','mysql','ajax','microcontroller','data structure','data mining','data warehouse','data plane','sql','selenium','qtp','web developer','bigdata','big data','ios developer','swift','flutter','hadoop','csharp','c sharp','c#','css','html','matlab','angular js','angular','nodejs','node js','node.js','angular.js','reactjs','react js','react.js','vuejs','vue js','vue.js','ui developer','jsp','jquery','rdbms','xhtml','dhtml','appdjango','vbscript','embedded c','app developer','wireless','iot','spring','pascal','javabeans','java beans','linux','azure','firebase','aws','xml','fortran','data analysis','solidity','amazon web service','redhat','alexa','cyber security','cordova','automation','drupal','machine learning','artificial intelligence','blockchain','hyperledger','ethereum','data migration','json','swing','backbone','ado','lamp','arduino','image processing','ccna','flask','mongodb','ruby','hibernate','oracle','ibm db2','teradata','ms access','joomla','indesign','acrobat','corel draw','docker','kubernetes','cobol','robotics','cyber security','augmented reality','virtual reality','autocad','solidworks','illustrator','ui/ux','ux/ui']
text2=text.replace("\n"," ")
text2=text2.lower()
#print(text2)
list1=[]
#search=''
for i in skills:
    if(i in text2):
#        print(i)
        list1.append(i)
 #       search=search+' '+i
#print(list1)
s=''
s=','.join(i for i in list1)

#print("String: "+s)

# get the path of ChromeDriverServer
#dir = os.path.dirname(__file__)
chrome_driver_path ="D:\Python Practice\chromedriver.exe"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(3)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.monsterindia.com")

# get the search textbox
search_field = driver.find_element_by_id("SE_home_autocomplete")

# enter search keyword and submit
search_field.send_keys(s)
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
lists= driver.find_elements_by_class_name("job-tittle")

# get the number of elements found
print ("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   print (listitem.text)

   print("----------------------------------------")
   i=i+1
   if(i>10):
      break

# close the browser window
driver.quit()
