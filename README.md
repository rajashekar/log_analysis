# Log Analysis
This project is done as part of Udacity Fullstack Developer course. The purpose of the project is to understand the concepts of SQL database and how to connect and retreive/modify data from database using Python DB-API. In this project, [PostgreSQL](https://www.postgresql.org/about/) is used and to connect from [Python3](https://www.python.org/) DB API library [Psycogp](http://initd.org/psycopg/) is used.

## Getting Started
### Prerequesites
Below software needs to be installed
 - [Python3](https://www.python.org/downloads/) 
 - [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
 - [Vagrant](https://www.vagrantup.com/downloads.html)

### Installing
To download the virtual machine using vagrant file
```
git clone https://github.com/udacity/fullstack-nanodegree-vm.git
```
To install downloaded virtual machine 
```
cd fullstack-nanodegree-vm
vagrant up
```
To login to vagrant virtual machine
```
vagrant ssh
```
To download the news database schema and loading up the required tables and data for news database.
```
cd /vagrant
wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
unzip newsdata.zip
psql -d news -f newsdata.sql
```

### How to Run
```
git clone https://github.com/rajashekar/log_analysis.git
cd log_analysis
python3 report.py
```
Output is generated to sample_output.txt
```
vagrant@vagrant:/vagrant/log_analysis$ more sample_output.txt
What are the most popular three articles of all time?
Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views

Who are the most popular article authors of all time?
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views

On which days did more than 1% of requests lead to errors?
Jul 17, 2016 - 2.26% errors
```

