from pprint import pprint
import re
import scrapy

class JobCheckSpider(scrapy.Spider):
    name = "job_check"

    def start_request(self):
        if len(sys.argv) < 2:
            print("Usage: scrapy crawl job_check <URL>")
            return

        url = sys.argv[1]
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        job_positions = {}

        for job in response.xpath('//div[@class="col-md-6 col-xs-12"]'):
            job_title = job.xpath('.//a[@itemprop="url"]/text()').get()
            if job_title:
                job_title = re.sub(r'\s+', ' ', job_title.strip())

                job_availability = job.xpath('.//a[@class="label label-info"]/text()').get()
                if not job_availability:
                    job_availability = "Closed"
                else:
                    job_availability = re.sub(r'\s+', ' ', job_availability.strip())

                job_published_date = job.xpath('.//time[@itemprop="datePublished"]/@datetime').get()

                if not job_published_date:
                    job_published_date = "date unknown"

                if not job_availability in job_positions:
                    job_positions[job_availability] = []

                job_positions[job_availability].append(
                        {
                            'title': job_title,
                            'availability': job_availability,
                            'published_at': job_published_date,
                        }
                )

        if job_positions:
            for availability, job_data in job_positions.items():
                for job in job_data:
                    print(f"\"{job['published_at']}\",\"{job['title']}\",\"{job['availability']}\"")


        next_page = response.xpath('//a[contains(@class, "pagenav") and contains(text(), "Próximo")]/@href').get()

        if next_page:
            yield response.follow(next_page, self.parse)
