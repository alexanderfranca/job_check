# job_check
Small script to download information

# Install Scrapy first 
pip install scrapy

# Create a Scrapy project first 
scrapy startproject job_check

# Move the script to the correct location and run it
cp job_check/job_check.py job_check/job_check/spiders/

cd job_check/job_check/spiders/

scrapy crawl fiotec <URL>



**URL** is the URL you want to get data from.
