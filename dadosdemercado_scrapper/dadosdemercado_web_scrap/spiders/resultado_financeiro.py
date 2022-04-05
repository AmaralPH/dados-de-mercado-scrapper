import scrapy


class StatusInvestSpider(scrapy.Spider):
    name = "resultado_financeiro"
    start_urls = ["https://www.dadosdemercado.com.br/acoes/SAPR3"]

    def parse(self, response):
        # dados sobre resultados
        periodos_results = response.css(
            ".data:nth-child(6) th::text"
        ).getall()[1:]

        receita_liquida = response.css(
            ".data:nth-child(6) tr:nth-child(1) td::text"
        ).getall()[2:]

        lucro_liquido = response.css(
            ".data:nth-child(6) tr:nth-child(11) td::text"
        ).getall()[2:]

        custos = response.css(
            ".data:nth-child(6) tr:nth-child(2) td::text"
        ).getall()[2:]

        despesas_operacionais = response.css(
            ".data:nth-child(6) tr:nth-child(4) td::text"
        ).getall()[2:]

        impostos = response.css(
            ".data:nth-child(6) tr:nth-child(8) td::text"
        ).getall()[2:]

        for index in range(len(periodos_results)):
            yield {
                "ano": periodos_results[index].split("-")[0],
                "receita_liquida": receita_liquida[index],
                "lucro_liquido": lucro_liquido[index],
                "custos": custos[index],
                "despesas_operacionais": despesas_operacionais[index],
                "impostos": impostos[index],
            }