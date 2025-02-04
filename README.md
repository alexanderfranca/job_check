# job_check
Small script to download information

# Install Scrapy first 
pip install scrapy

# Create a Scrapy project first 
scrapy startproject job_check_scrap

# Move the script to the correct location and run it
cp job_check/job_check.py job_check_scrap/job_check_scrap/spiders/

cd job_check_scrap/job_check_scrap/spiders/

scrapy crawl job_check -a url="URL"

**OR** (if you want the output in a CSV file)


scrapy crawl job_check -a url="URL" > MY_OUTPUT.csv



**URL** is the URL you want to get data from.
