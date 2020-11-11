from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
api_url = None


@given('a pagina de registro da praga')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-pest-dev.herokuapp.com/pest'
    print('url :'+api_url)


@when('ele registar os campos da praga')
def step_impl_when(context):
    request_bodies['POST'] = {"priority": "Alta",
                              "problem": "Sistema eletronico com defeito",
                              "description": "sistema esta aquecendo muito, o que fazer"}
    response = requests.post(
                            'https://smartvit-pest-dev.herokuapp.com/pest',
                            json=request_bodies['POST']
                            )


@then('os dados devem passar pelo servico atraves do BFF e armazenar no banco')
def step_impl_then(context):
    api_bff_url = 'https://smartvit-user-bff-dev.herokuapp.com/pest/'
    response = requests.post(
                            api_bff_url,
                            json=request_bodies['POST']
                            )
    assert response.status_code != 200