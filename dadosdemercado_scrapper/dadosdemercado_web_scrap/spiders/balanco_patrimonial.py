import scrapy


class StatusInvestSpider(scrapy.Spider):
    name = "balanco_patrimonial"
    start_urls = ["https://www.dadosdemercado.com.br/acoes/SAPR3"]

    def parse(self, response):
        # # dados sobre fluxo de caixa
        periodos_bp = response.css(".data:nth-child(5) th::text").getall()
        patrimonio_liquido = response.css(
            ".numbers tr:nth-child(18) td::text"
        ).getall()[1:]

        bp_por_periodo = {}

        for index in range(len(periodos_bp)):
            bp_por_periodo[periodos_bp[index]] = patrimonio_liquido[index]

        bp_por_ano = {}
        for periodo, bp in bp_por_periodo.items():
            if periodo.split("-")[0] not in bp_por_ano:
                bp_por_ano[periodo.split("-")[0]] = int(bp)

        yield bp_por_ano
