import scrapy

class QMcontentSpider(scrapy.Spider):
    name = "QMcontent"
    start_urls = []
    with open('data/QMLinks') as QMLinks:
        for line in QMLinks:
            start_urls.append(line[:-1])

    def parse(self, response):
        title = response.xpath('//title/text()').extract_first()
        divs = response.css('div.post__content.wysiwyg')
        ptextss = [ div.css('p::text') for div in divs ]

        with open('data/pages/'+title, 'w') as page:
            for ptexts in ptextss:
                for ptext in ptexts:
                    page.write(ptext.extract())

        self.log('Saved page {}'.format(title))
