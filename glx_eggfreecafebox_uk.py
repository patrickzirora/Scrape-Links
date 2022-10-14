# Eggfree Cake Box - UK
# Blocked by cloudflare
# Copy json item to github
github_link ="https://github.com/patrickzirora/Scrape-Links/blob/main/eggfreecafebox"

import scrapy
from locations.items import GeojsonPointItem
import datetime
import json

class GlxEggfreeCakeBoxUKSpider(scrapy.Spider):
    name = 'glx_eggfreecafebox_uk'
    item_attributes = {'brand': 'Eggfree Cake Box'}
    allowed_domains = ['www.eggfreecake.co.uk']
    download_delay = 0.05

    start_urls = [ github_link ]

    def parse(self, response):

        location_uk = json.loads( response.text )

        for location in location_uk:
         
            yield GeojsonPointItem(
                lat=location.get('latitude'),
                lon=location.get('longitude'),
                ref=location.get('store_code'),
                phone=location.get('phone'),
                name='Eggfree Cake Box ' + location.get('name'),
                opening_hours='',
                addr_full=location.get('address'),
                city=location.get('city'),
                state=location.get('region'),
                country=location.get('country'),
                postcode=location.get('postcode'),
                website='https://www.eggfreecake.co.uk/storelocator/' + location.get('link'),
                extras={
                    'brand': 'Eggfree Cake Box',
                    'fascia': 'Eggfree Cake Box',
                    'category': 'Confectionary',
                    'edit_date': int( datetime.datetime.now().strftime('%Y%m%d') ),
                    'source': 'glx',
                    'lat_lon_source': 'API Endpoint'
                }
            )