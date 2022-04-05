# dados-de-mercado-scrapper

Repositório para projeto de estudos sobre Scrapy

Para rodar o projeto é necessário instalar o gerenciador de pacotes anaconda e o framework Scrapy

O projeto tem 4 spiders: balanco_patrimonial.py, fluxo_de_caixa.py, quantidade_de_acoes.py, resultado_financeiro.py

Atualmente os spiders buscam ações da Sanepar (código SAPR3), mas caso o projeto seja baixado, pode-se alterar o código da ação no final da URL na linha 6 de cada spider

Para baixar o relatório no formato json, precisamos executar no terminal de dentro do diretório dadosdemercado_web_scrap o comando $scrapy crawl RELATORIO_DESEJADO -O NOME_DO_AQUIVO_DESTINO.json

O projeto ainda está em construção, mas já consegue retornar as informações desejadas
