Feature: Captar requisicao feita no frontend e enviar ao microsservico pestt atraves do BFF 
  Como Sistema, quero pegar os dados informados no frontend pelo usuario,
  e registra-los no meu servico.

  Context: O usuario registra a praga
    Dado que os dados resgistrados utilizem o servico atraves do BFF

    Scenario: Usuario registrar praga desejada
        Given a pagina de registro da praga
        When ele registar os campos da praga
        | idVineyard               | type     | startTime                 |
        | 5f87a0efbf0df955915a3ebb | Largatas | 2020-10-15T02:07:08+00:00 |
        Then os dados devem passar pelo servico atraves do BFF e armazenar no banco
        | idVineyard               | type     | startTime                 |
        | 5f87a0efbf0df955915a3ebb | Largatas | 2020-10-15T02:07:08+00:00 |