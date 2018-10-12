# TvSeries-airdate-Mailer

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                            tvseriesdb.py                                                                                                              +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                                                                                                                                                       
+                                                                                                                                                       
+  The file is a implementation of the project "http://innovaccer.com/media/hackercamp/SDE-Intern-Assignment.pdf"                                       
+  
+  requirements - python2.7, MYSQLdb
+   
+
+  Must Dos:
+  Before running the python file give the mysql username and password in the mysqlusername, mysqlpassword varaiables respectively!
+  
+  In the command line$ python2.7 tvseries.db
+
+  //will create a database to store the values, acts like a cache which prevents fetching of already seen values
+  //creates some warnings if the database is already created, you can happily ignore them
+  
+  Valid Email:
+  Now, it will ask you to give a valid email id, enter a valid email id else it will go back and start again
+
+  Authentication CODE: 
+  After entering the valid email id, it will send you a authentication code, enter the code to validate else yo will face authentication error
+
+  Enter TvSeries Names:
+  After entering the code, it asks you to enter the names of tv series separated by a comma for which you want the airdates of next episode/seasons
+  No problem if you dont remember the tvseries names exactly, type the nearest possible name! go on
+
+  Wait for a while and watch ****
+
+  Response:
+  yaayy! You will now receive a mail regarding the airdates of the TV Series   
+
+  You can continue to play the game or press "0" to exit the game!!
+
+  Thank you!
+
+
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


***********************************************************************************************************************************************************
*                            TvSeries2.py
***********************************************************************************************************************************************************
* 
*   Dont worry if you dont have MYSQLdb or facing problems with mysqldb!  this program runs without mysqldb
*
*   Commandline$: python2.7 TvSeries2.py
*   
*   Valid Email:
*   It will ask you to enter a valid format email, enter it
*
*
*   Authentication Code:
*   Enter the authenticatio code sent to your mail, this is done to avoid spam, please bear with me
*
*   Enter Tvseries name:
*   After entering the code, it asks you to enter the names of tv series separated by a comma for which you want the airdates of next episode/seasons
*   No problem if you dont remember the tvseries names exactly, type the nearest possible name! go on
*
*   Wait for a while and watch ****
*
*   Response:
*   yaayy! You will now receive a mail regarding the airdates of the TV Series   
*
*   You can continue to play the game or press "0" to exit the game!!
*
*   Thank you!
*
*********************************************************************************************************************************************************

#######################################################################################################################################################
#                                       TvSeries.py
#######################################################################################################################################################
#
#
*  This file is same as the above TvSeries2.py implemented in python3
#
#  Use this file if you want to run the code in python3, runs without MYSQLdb
#
#  It has the same guidelines as like the above "TvSeries2.py" program
#
#  Commandline$ python TvSeries.py
#
#  Thank you!
#
#######################################################################################################################################################




