import sys
import urllib2  
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
from datetime import datetime, timedelta
import string
import re
import random
import MySQLdb
import MySQLdb


mysqlusername = "root"
mysqluserpassword = "vamshi@123"
db = MySQLdb.connect(host="localhost",  # your host 
                     user=mysqlusername,       # username
                     passwd=mysqluserpassword     # password
                    )   # name of the database
 
# Create a Cursor object to execute queries.
cur = db.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS MOVIEBUFFS2;")
cur.execute("use  MOVIEBUFFS2;")

cur.execute("CREATE TABLE IF NOT EXISTS TvSeriesData(id int(11) NOT NULL AUTO_INCREMENT, series varchar(300), description varchar(1000), PRIMARY KEY (id));")


dik = {}

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


MY_ADDRESS = 'svkc1234'
PASSWORD = 'bkmgnmezmwskzexx'

s = smtplib.SMTP(host='smtp.gmail.com', port='587')
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
message = "The most awaited TV Series Game of Thrones Season 8 coming in 2019! stay tuned!!"

ans = []
tvseries = []
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def getlist():
	print("Enterd to make a dictionary!")
	quote_page = "https://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv"
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, "html.parser")
	for ele in soup.find_all('td', attrs={'class':'titleColumn'}):
		s = ele.find()
		cast = s.attrs['title']
		name = ele.find('a', attrs={'title':cast})
		dik[name.text] = cast
	print("dictionary done!!!")



def getMailData(secondlink, thirdlink):
	'''print("enetred the final destination!!")'''
	flag = 0

	if(thirdlink!="None"):
		quote_page2 = thirdlink
		page2 = urllib2.urlopen(quote_page2)
		soup2 = BeautifulSoup(page2, 'html.parser')
		ele2 = soup2.find_all('div', attrs={'class':'airdate'})
		pl = []
		for elem in ele2:
			pl.append(elem.text.strip())
		'''print("printing from third link!!")
		print(pl)'''
		regex = re.compile('[%s]' % re.escape(string.punctuation))
		formatpl = []
		for item in pl:
			formatpl.append(regex.sub(u'', item.strip().lower()))
		'''print("formatpl ", formatpl)'''
		formatdate = []
		formatdateyear = []
		for item in formatpl:
			if(len(item.split())==3):
				formatdate.append(datetime.strptime(item, "%d %b %Y"))
			
			if(len(item.split())==1):
				formatdateyear.append(datetime.strptime(item, "%Y"))

			if(len(item.split())==2):
				formatdate.append(datetime.strptime(item, "%b %Y"))
		'''print("dates are -- ",formatdate)'''
		'''print("years are --- ", formatdateyear)'''
		present = datetime.now()
		finaldate = []
		for t in formatdate:
			if(t>=present):
				finaldate.append(t)
		'''print("final dates are ", finaldate)'''

		if(len(finaldate)>=1):
			flag = 1
			'''print("the next episod on airs ",finaldate[0])'''
			sol = "The next episode airs on " + str(finaldate[0])
			ans.append(sol)
		else:
			if((len(formatdateyear)>=1) and (formatdateyear[0]>=datetime.strptime("2018", "%Y"))):
				flag=1
				'''print("we have upcoming episodes from  the current season in ", formatdateyear[-1])'''
				sol = "we have upcoming episodes from  the current season in " + str(formatdateyear[-1])  
				ans.append(sol)
			else:
				print("!!")

	if(flag==0):
		'''print("In the second link ")'''
		quote_page = secondlink
		page = urllib2.urlopen(quote_page)
		soup = BeautifulSoup(page,'html.parser')
		ele = soup.find_all('div', attrs = {'class':'airdate'})
		pl = []
		for elem in ele:
			pl.append(elem.text.strip())

		'''print(pl)'''
		regex = re.compile('[%s]' % re.escape(string.punctuation))
		formatpl = []
		for item in pl:
			formatpl.append(regex.sub(u'', item.strip().lower()))
		'''print("format pl from last link ", formatpl)'''
		formatdate = []
		formatdateyear = []
		for item in formatpl:
			if(len(item.split())==3):
				formatdate.append(datetime.strptime(item, "%d %b %Y"))
			if(len(item.split())==2):
				formatdate.append(datetime.strptime(item, "%b %Y"))
			if(len(item.split())==1):
				formatdateyear.append(datetime.strptime(item, "%Y"))
		'''print("dates are -- ",formatdate)'''
		'''print("years are --- ", formatdateyear)'''
		if(len(formatdate)==0):
			'''print("No current episodes, next season on ", formatdateyear[-1])'''
			sol = "No current episodes, wait for upcoming season " 
			ans.append(sol)
		else:
			finaldate = []
			present = datetime.now()
			for t in formatdate:
				if(t>=present):
					finaldate.append(t)
			'''print("final dates are ", finaldate)'''

			if(len(finaldate)>=1):
				flag = 1
				'''print("the next episod  airs on ",finaldate[0])'''
				sol = "The next Episode airs on " + str(finaldate[0])
				ans.append(sol)
			else:
				if((len(formatdateyear)>=1) and (formatdateyear[0]>=datetime.strptime("2018","%Y"))):
					flag=1
					'''print("we have upcoming episodes from the current season on ", formatdateyear[-1])'''
					sol = "we have upcoming episodes from the current season on " + str(formatdateyear[-1])
					ans.append(sol)
				else:
					'''print("Done with the episodes, No new seasons as of now. Stay Tuned!!")'''
					sol = "Done with the episodes, No new seasons as of now. Stay Tuned!!"
					ans.append(sol)



		
		



def getEpisodeData(link):
	'''print("LOL\n")'''
	'''print("getting the final links")'''
	quote_page = link
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	ele = soup.find('div', attrs = {'class':'seasons-and-year-nav'})
	for elem in ele:
		u = ele.find('a')
		'''print(u)'''
	x = ele.find_all('a')
	'''print(x)'''
	slink = x[0]
	thirdlink = "None"
	if(len(x)>1):
		tlink = x[1]
		thirdlink = tlink.attrs['href']
		thirdlink = "https://www.imdb.com" + thirdlink

	'''print(slink.attrs)'''
	secondlink = slink.attrs['href']
	'''print(secondlink)'''
	secondlink = "https://www.imdb.com" + secondlink
	getMailData(secondlink, thirdlink)



def getOriginal(item):
	similarity = 0
	for key in dik:
		if similarity < similar(key, item):
			similarity = similar(key, item)
			cast = dik[key]
			series = key
	origtvlist.append(series)


def getLink(text2):
	'''print("getting first link")'''
	quote_page = "https://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv"
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, "html.parser")
	similarity = 0
	for key in dik:
		if similarity < similar(key, text2):
			similarity = similar(key, text2)
			cast = dik[key]
			series = key
	tvseries.append(series)
	name_box = soup.find('a',attrs={'title':cast})
	'''print("fetched")'''
	name = name_box.text
	'''print(name)'''
	'''print(name_box.attrs)
	print(name_box.attrs['href'])'''
	link = name_box.attrs['href']
	link = "https://www.imdb.com" + link 
	getEpisodeData(link)




for i in range(1):
	getlist()
	'''print("len of dictionary is ", len(dik))
	print(" ******* the following is the dictionary **********")
	for ele in dik.items():
		print(ele[0], "   ", ele[1])'''


while(1):
	del ans[:]
	del tvseries[:]
	tvdict = {}
	print("********* Welcome ************")
	print("Enter valid email id for info about the TV Series else 0")
	text = raw_input()
	if(text=="0"):
		break
	regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
	if(re.match(regex,text)==None):
		print("Not a valid mail format! Please check  your mail ID")
		continue
	print("In order to avod spam lets check if its your mail, enter the CODE sent to your mail")
	msg = MIMEMultipart()       # create a message
	msg['From']=MY_ADDRESS
	msg['To']=text
	msg['Subject']="CODE for Movie Buffs!!"
	rnd = random.randint(1001,9001)
	final = " The CODE for Movie Buffs is " + str(rnd)
	msg.attach(MIMEText(final, 'plain'))
	msgstring = msg.as_string()
	s.sendmail(MY_ADDRESS, text, msgstring)
	del msg
	code = raw_input()
	if(code!=str(rnd)):
		print("Authentication failure")
		continue;
	

	if(text!='0'):
		print("your email is - ", text)
		print("Enter your required TV Series separated by a comma")
		print("Its okay if you cant spell the series name exactly, type the nearest possible word!!!")
		text2 = raw_input()
		tvlist = text2.split(',')
		origtvlist = []
		for item in tvlist:
			getOriginal(item)
		'''print("the original tv list is -- ",origtvlist)'''
		cur.execute("SELECT * FROM TvSeriesData;")
		for row in cur.fetchall():
			tvdict[row[1]]=row[2]
		'''print("the tvdict is --- ", tvdict)'''

		'''for item in tvlist:
			getLink(item)'''

		for item in origtvlist:
			if item in tvdict.keys():
				tvseries.append(item)
				ans.append(tvdict[item])
			else:
				getLink(item)
				s1 = tvseries[-1]
				s2 = ans[-1]
				cur.execute("INSERT INTO TvSeriesData(series, description) VALUES (%s, %s);",(s1,s2))
		msg = MIMEMultipart()       # create a message
		msg['From']=MY_ADDRESS
		msg['To']=text
		msg['Subject']="Movie Buffs! YES WE ARE!!"
		final = ""
		for i in range(len(ans)):
			final = final + "Tv series name: " + tvseries[i] + "\n"
			final = final + "Status: " + ans[i] + "\n"
			final = final + "\n"
		db.commit()

		msg.attach(MIMEText(final, 'plain'))
		msgstring = msg.as_string()
		s.sendmail( MY_ADDRESS, text, msgstring)
		del msg
		print("Please check your mail")
		print("Thank you for choosing our service")
	else:
		break

