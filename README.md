Tools :
--------
1- Visual Studio Code
2- PostgreSQL
3- Linux terminal 
4- virtual machine (VM) & Vagrant

Project Requirements :
----------------------
1- What are the most popular three articles of all time?
2- Who are the most popular article authors of all time?
3- On which days did more than 1% of requests lead to errors?

How to run the program :
-------------------------
1- Install Visual Studio Code : Install on it Python
2- Install virtual machine (VM) & Vagrant after that configration then 
   vagrant up and vagrand ssh 
3- run command : cd /vagrant
4- for sql download newsdata.sql then run command psql -d news -f 
   newsdata.sql
5- Put Logs_Analysis.py in vagrant directory then run command 
   python3 Logs_Analysis.py

Views:
-------------------------
run this command to create view: 

psql -d news -c "create view errors_request_day as select time ::date as "DateError" ,count(1) as "num_errors"  from log where log.status='404 NOT FOUND' group by log.time order by "num_errors" desc"

-------used limit & offset for time------------
psql -d news -c "create view tb_percentage as select dateerror,(num_errors * 100 /(select  count(1) from log where time ::date = dateerror)) as "percentage" from errors_request_day limit 5 offset 0 "







