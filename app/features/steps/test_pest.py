from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
response_codes = {}
api_url = None


@given('a pagina de registro da praga')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-pest-stg.herokuapp.com/pest'
    print('url :'+api_url)


@when('ele registar os campos da praga')
def step_impl_when(context):
    request_bodies['POST'] = {"idVineyard": "5fad331b38b2670687db57e2",
                              "type": "cigarras",
                              "startTime": "12-11-2020"}
    response = requests.post(
                            api_url,
                            json=request_bodies['POST']
                            )
    statuscode = response.status_code
    response_codes['POST'] = statuscode


@then('os dados devem passar pelo servico atraves do BFF e armazenar no banco')
def step_impl_then(context):
    print('Post rep code ;'+str(response_codes['POST']))
    assert response_codes['POST'] == 200