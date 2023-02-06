import scrapy
from ..items import EdmundsScraperItem


class BaseInfoSpider(scrapy.Spider):
    """ This spider basically scrapes the car urls from the base url and stores the in a variable car_urls"""
    name = 'edmunds'
    page_number = 1
    #   concatenating page_number and start_ulrs for dunamic pages/pagination
    start_urls = [
       # 'https://www.edmunds.com/cars-for-sale-by-owner/'
        'https://www.edmunds.com/acura/ilx/2022/'
    ] 

    def parse(self, response):
        #   Store all urls for each car in the below variable
        #all_car_urls = response.css('a.usurp-inventory-card-vdp-link::attr(href)').extract()
        all_car_urls = response.css('a::attr(href)').extract()
        
        #   Loop each url in start_urls to scrape required informations using callback function
        for url in all_car_urls:
            yield response.follow(url, callback=self.car_url) 

        #   Since the last page is 476th page this condition will run only when the current page is
        #   less than the last page. Thus the next paginated page will be scrapped
        if self.page_number <= 100:  
            self.page_number += 1
            #next_page = 'https://www.edmunds.com/cars-for-sale-by-owner/?pagenumber=' + str(self.page_number)
            next_page = 'https://www.edmunds.com/acura/ilx/2022/consumer-reviews/?pagenum=' + str(self.page_number)
            yield response.follow(next_page, callback=self.parse) 
    

    def car_url(self, response):
        #`Creating an instance of items 
        items = EdmundsScraperItem()
        #name = response.css('h1.text-black::text').extract()
        name = response.css('p::text').extract()
        #name += response.css('p::text').extract()
        # price = response.css('div.heading-2').css('span::text').extract()
        # vin = response.css('div.text-gray-darker').css('span::text').extract()[1]
        # vehicle_sum = response.css('.vehicle-summary').css('.row').css('.col::text').extract()
        # top_spec = response.css('.features-and-specs').css('.row').css('li.mb-0_5::text').extract()

        #   Adding rquired details to items data
        items['Name'] = name
        # items['Price'] = price
        # items['VIN'] = vin
        # items['Vehicle_Summary'] = vehicle_sum
        # items['Top_Features_And_Specs'] = top_spec
        yield items