import scrapy


class StatusInvestSpider(scrapy.Spider):
    name = "quantidade_de_acoes"
    start_urls = ["https://www.dadosdemercado.com.br/acoes/SAPR3"]

    def parse(self, response):
        quantidade_de_acoes = response.css(
            "tbody:nth-child(1) tr:nth-child(5) td+ td::text"
        ).get()

        yield {"quantidade_de_acoes": int(quantidade_de_acoes)}
