import scrapy
from ..items import IndyaItem

class IndyaSpider(scrapy.Spider):
    name = 'indya'
    start_urls = ['https://www.houseofindya.com/zyra/necklace-sets/cat']

    def parse(self, response):
        all_product_list = response.css('ul#JsonProductList')
        all_li = all_product_list.css('li')
        all_data_urls = all_li.xpath("@data-url").extract()
        for url in all_data_urls:
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        items = IndyaItem()
        title = response.css('div.prodRight h1::text')[0].extract()
        cost_price = response.css('div.prodRight span::text')[1].extract()
        sale_price = response.css('div.prodRight span::text')[2].extract()
        description = response.css('div#tab-1').css('p::text').extract()
        images = response.css('a.ProductPopupbox').xpath("@data-image").extract()
        items['title'] = title
        items['cost_price'] = cost_price
        items['sale_price'] = sale_price
        items['description'] = description
        i = 0
        for img in images:
            x = 'img'+ str(i)
            items[x] = img
            i+=1
        yield items
