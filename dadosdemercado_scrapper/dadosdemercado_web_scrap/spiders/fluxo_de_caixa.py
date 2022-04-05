import scrapy


class StatusInvestSpider(scrapy.Spider):
    name = "fluxo_de_caixa"
    start_urls = ["https://www.dadosdemercado.com.br/acoes/SAPR3"]

    def parse(self, response):
        # # dados sobre fluxo de caixa
        periodos_fc = response.css(".data:nth-child(7) th::text").getall()
        fluxo_de_caixa = response.css(
            ".data:nth-child(7) tr:nth-child(1) td::text"
        ).getall()[1:]

        fc_por_periodo = {}

        for index in range(len(periodos_fc)):
            fc_por_periodo[periodos_fc[index]] = fluxo_de_caixa[index]

        fc_por_ano = {}
        for periodo, fc in fc_por_periodo.items():
            if periodo.split("-")[0] not in fc_por_ano:
                fc_por_ano[periodo.split("-")[0]] = int(fc)
            else:
                fc_por_ano[periodo.split("-")[0]] += int(fc)

        yield fc_por_ano
