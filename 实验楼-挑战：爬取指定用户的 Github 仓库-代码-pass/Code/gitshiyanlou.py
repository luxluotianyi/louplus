import scrapy

class GitShiyanlou(scrapy.Spider):

	name = 'git-shiyanlou'

	@property
	def start_urls(self):

		url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'

		return (url_tmpl.format(i) for i in range(1,5))

	def parse(self, response):
		for respository in response.xpath('//div[@id="user-repositories-list"]/ul[1]/li'):
			yield {
				'name':  respository.xpath('.//div[@class="d-inline-block mb-1"]/h3/a/text()').re_first('\w+'),
				'update_time': respository.xpath('.//div[@class="f6 text-gray mt-2"]/relative-time/@datetime').extract_first()
			}



