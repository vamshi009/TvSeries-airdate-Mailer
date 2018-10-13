# TvSeries-airdate-Mailer

1. tvseriesdb.py
    + requirements - python2.7, MYSQLdb
    +  Before running the python file give the mysql username and password in the mysqlusername, mysqlpassword varaiables respectively!
    +  Run it with ```python2.7 tvseries.db```
        + will create a database to store the values, acts like a cache which prevents fetching of already seen values
        +  creates some warnings if the database is already created, you can happily ignore them
    + Valid mail format
    	+ Enter a valid email id format ,  else it will go back and start again
    + Authentication code
    	+  After entering the valid email id, it will send you a authentication code to your mail, enter the code to validate else you will face 	authentication error
    + TvSeries Names:
        +  After entering the code, it asks you to enter the names of tv series separated by a comma for which you want the airdates of next episode/seasons
        +  No problem if you dont remember the tvseries names exactly, type the nearest possible name!
    +  Response:
        +  yaayy! You will now receive a mail regarding the airdates of the TV Series   
    +  Press "0" to exit the game!!


2. TvSeries2.py

   + Dont worry if you dont have MYSQLdb or facing problems with mysqldb!  this program runs without mysqldb

   + Commandline$: ```python2.7 TvSeries2.py```
   
   + Valid Email:
   		+ It will ask you to enter a valid format email, enter it


   + Authentication Code:
   		+ Enter the authentication code sent to your mail, this is done to avoid spam, please bear with me

   + Enter Tvseries name:
   		+ After entering the code, it asks you to enter the names of tv series separated by a comma for which you want the airdates of next episode/seasons
   		+ No problem if you dont remember the tvseries names exactly, type the nearest possible name! go on

   + Wait for a while and watch ****

   + Response:
   		+ yaayy! You will now receive a mail regarding the airdates of the TV Series   

   + You can continue to play the game or press "0" to exit the game!!

   + Thank you!


3. TvSeries.py


  + This file is same as the above TvSeries2.py implemented in python3

  + Use this file if you want to run the code in python3, runs without MYSQLdb

  + It has the same guidelines as like the above ```TvSeries2.py``` program

  + Commandline$ ```python TvSeries.py```

  + Thank you!





