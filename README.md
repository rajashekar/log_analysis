## About
This project displays report details based on postgresql database.

## Prerequesites
Below software needs to be installed
 - Python3 
 - Virtual Box
 - Vagrant

## Execution steps
```
git clone https://github.com/udacity/fullstack-nanodegree-vm.git
cd fullstack-nanodegree-vm
vagrant up
vagrant ssh
cd /vagrant
wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
unzip newsdata.zip
psql -d news -f newsdata.sql
git clone https://github.com/rajashekar/log_analysis.git
cd log_analysis
python3 report.py
```

Sample output - 
```
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