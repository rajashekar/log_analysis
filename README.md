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

Go to http://localhost:8000/
## Demo
![Demo](https://github.com/rajashekar/log_analysis/blob/master/demo.png)
