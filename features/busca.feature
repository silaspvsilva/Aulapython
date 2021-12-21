#language: pt


  Funcionalidade: fluxo de busca

    #noinspection CucumberUndefinedStep
    @busca
    Cenário: realizar busca
      Dado que acesso o site do python
      E preencho o input de pesquisa
      Quando clico no botão de pesquisar
    Então devo visualizar os resultados da pesquisa
