Tools :
--------
1- Visual Studio Code 
2- PostgreSQL 
3- Linux terminal 
4- VirtualBox VM 
5- Vagrant 
6- Database (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/
57b5f748_newsdata/newsdata.zip)

Project Requirements :
----------------------
1- What are the most popular three articles of all time?
2- Who are the most popular article authors of all time?
3- On which days did more than 1% of requests lead to errors?

How to run the program :
-------------------------
1- Install Visual Studio Code (https://code.visualstudio.com/download)
2- Install virtual machine (VM) (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
3- Vagrant (https://www.vagrantup.com/) 
4- configration unzip (https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
4- cd Inside vagrant then vagrant up and vagrand ssh 
3- run command : cd /vagrant
4- for sql unzip database and put newsdata.sql in vagrant directory 
   then run command : psql -d news -f newsdata.sql
5- Put Logs_Analysis.py in vagrant directory then run command 
   python3 Logs_Analysis.py

Views:
-------------------------
run this command to create view: 

------------View 1------------------------------------
psql -d news -c "CREATE VIEW statustotal AS SELECT time ::date,status FROM log"

------------View 2------------------------------------
psql -d news -c "CREATE VIEW statusfailed AS SELECT time, count(*) AS num FROM statustotal WHERE status = '404 NOT FOUND' GROUP BY time;"

------------View 3------------------------------------
 psql -d news -c "CREATE VIEW statusall as SELECT time, count(*) AS num FROM statustotal WHERE status = '404 NOT FOUND' OR status = '200 OK' GROUP BY time;"

-------------View4-------------------------------------
psql -d news -c "CREATE VIEW percentagecounts AS SELECT statusall.time, statusall.num AS numall, statusfailed.num AS numfailed, statusfailed.num::double precision/statusall.num::double precision * 100 AS percentagefailed FROM statusall, statusfailed WHERE statusall.time = statusfailed.time;"

