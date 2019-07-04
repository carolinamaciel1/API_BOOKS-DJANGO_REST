# Django application
Aplicação crud de biblioteca.

## Setup do ambiente 
1. Clone o repositório 

``` 
$ git clone https://github.com/carolinamaciel1/django-application.git
```

2. Dentro do repositório crie uma máquina virtual para subir o servidor django 

```
$ py manage.py -m venv venv
```
**cd venv > cd Scripts > activate**


3. Instale o requirements.txt

```
$ pip install requirements.txt
```

4. Migre o DB

```
$ py manage.py migrate
```



## Para efetuar testes no sistema

1. Suba o servidor django

```
$ py manage.py runserver
```

2. Logue como super user para ter acesso aos recursos da api 

Se tentar ter acesso aos endpoints sem ter logado aparecerá uma mensagem de "Authentication credentials were not provided."

```
---------------------
FRONT END DJANGO REST 
---------------------

http://127.0.0.1:8000/admin

login: admin
senha: novaSenha@

----------------
 PYTHON REQUEST 
----------------

Authorization 

Type > Basic Auth

username: admin
senha: novaSenha@

```

## Navegando pelo endpoint /books
###### CREATE
```
---------------------
FRONT END DJANGO REST 
---------------------

Em http://127.0.0.1:8000/books é possível ter acesso ao json com as informações da api, para adicionar um novo objeto preencha  os campos name_book, author_book,registration date e publishing company com informações válidas. Clique no botão "POST" para criar um novo objeto.

{
    "name_book": [
        "This field may not be blank."
    ],
    "author_book": [
        "This field may not be blank."
    ],
    "registration_date": [
        "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
    ]
}

----------------
 PYTHON REQUEST 
----------------

import requests

url = "http://127.0.0.1:8000/books/"

payload = {"name_book": "Livro Testando","author_book":"Autor Testando","registration_date":"2019-07-04"}
headers = {
    'Authorization': "Basic YWRtaW46bm92YVNlbmhhQA==",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "e90a10d4-d170-473d-a996-949331ff02c8,6651e1d5-ed7a-4883-a07e-f06cfdb80208",
    'Host': "127.0.0.1:8000",
    'accept-encoding': "gzip, deflate",
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'content-length': "428",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
data = json.dumps(payload)
response = requests.request("POST", url, data=data, headers=headers)


```
###### UPDATE 

```
---------------------
FRONT END DJANGO REST 
---------------------

Em http://127.0.0.1:8000/books/id/ é possível ter acesso ao json com as informações de cada livro individualmente, modifique as informações de algum campo e clique no botão "PUT" para aplicar as mudaças a algum campo. 

ex: http://127.0.0.1:8000/books/3/

{
    "id": 3,
    "name_book": "Alice: As aventuras de Alice no país das maravilhas e através do espelho e oque encontrou por lá",
    "author_book": "Lewis Carroll",
    "publishing_company": "Zahar",
    "registration_date": "2019-07-02"
}

----------------
 PYTHON REQUEST 
----------------

ATUALIZANDO TODOS OS CAMPOS 

url = "../books/36/"

payload = {"name_book": "A menina e o porquinho", "author_book": "Autor desconhecido", "publishing_company":"Editora desconhecida","registration_date":"2019-07-04"}

headers = {...}
data = json.dumps(payload)
response = requests.request("PUT", url, data=data, headers=headers)

ATUALIZANDO CAMPO ESPECÍFICO

payload = {"author_book": "Elwyn Brooks White"}

headers = {...}
data = json.dumps(payload)
response = requests.request("PATCH", url, data=data, headers=headers)




```
###### DELETE

```
---------------------
FRONT END DJANGO REST 
---------------------

Em http://127.0.0.1:8000/books/id/ além de ter acesso ao json com as informações de cada livro individualmente, temos também a disposição um botão para deletar o livro específico. Após clicar em "DELETE" e na confirmação "DELETE" o livro é excluído do db e deixa de existir na API.

Se você excluir o id e tentar buscar o objeto que foi excluído, uma mensagem de "Not found" irá aparecer.

ex: http://127.0.0.1:8000/books/6/

{
    "detail": "Not found."
}

----------------
 PYTHON REQUEST 
----------------

url = "../books/36/"
headers = {...}
response = requests.request("DELETE", url, headers=headers)


```
###### SEARCH AND FILTERS

```
---------------------
FRONT END DJANGO REST 
---------------------

Em http://127.0.0.1:8000/books/ temos a nossa disposição um botão "FILTERS", nele podemos fazer buscas no endpoint books. Podemos buscar por id, name book, author book, registration date e podemos ordenar o registration date em ordem ascending e descending.

Exemplos de busca:

http://127.0.0.1:8000/books/?search=A+menina+que+roubava+livros

----------------
 PYTHON REQUEST 
----------------

import requests

url = "http://127.0.0.1:8000/books/"

querystring = {"search":"A+menina+e+o+porquinho"}

headers = {...}

response = requests.request("GET", url, headers=headers, params=querystring)


```

## Navegando pelo endpoint /copybook

###### CREATE
```
---------------------
FRONT END DJANGO REST 
---------------------

Em http://127.0.0.1:8000/copybook/ é possível ter acesso ao json com as informações da api, para adicionar um novo objeto preencha  os campos date register, edition and book com informações válidas. Clique no botão "POST" para criar um novo objeto.

{
    "date_register": [
        "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
    ]
}

----------------
 PYTHON REQUEST 
----------------

import requests

url = "http://127.0.0.1:8000/copybook/"

payload = {"date_register":"2019-07-04","edition":1,"book":3}
headers = {
    'Authorization': "Basic YWRtaW46bm92YVNlbmhhQA==",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "5f7918dd-7bff-4372-a4e5-a5b72a386009,3225642b-4fea-4e70-b189-9cd21d83077b",
    'Host': "127.0.0.1:8000",
    'accept-encoding': "gzip, deflate",
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'content-length': "389",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
data = json.dumps(payload)
response = requests.request("POST", url, data=data, headers=headers)

```

###### UPDATE 

```
---------------------
FRONT END DJANGO REST 
---------------------

Em http://127.0.0.1:8000/copybook/id/ é possível ter acesso ao json com as informações de cada livro individualmente, modifique as informações de algum campo e clique no botão "PUT" para aplicar as mudaças a algum campo. 

ex: http://127.0.0.1:8000/copybook/3/

{
    "id": 3,
    "date_register": "2019-01-02",
    "edition": 12,
    "book": 2
}

----------------
 PYTHON REQUEST 
----------------

ATUALIZANDO TODOS OS CAMPOS 

url = "../copybooks/3/"

payload = {"date_register":"2019-07-04","edition":14,"book":3}

headers = {...}
data = json.dumps(payload)
response = requests.request("PUT", url, data=data, headers=headers)

ATUALIZANDO CAMPO ESPECÍFICO

payload = {"book":2}

headers = {...}
data = json.dumps(payload)
response = requests.request("PATCH", url, data=data, headers=headers)
```

###### DELETE

```
---------------------
FRONT END DJANGO REST 
---------------------

Em http://127.0.0.1:8000/copybook/id/ além de ter acesso ao json com as informações de cada livro individualmente, temos também a disposição um botão para deletar o livro específico. Após clicar em "DELETE" e na confirmação "DELETE" o exemplar do livro é excluído do db e deixa de existir na API.

Se você excluir o id e tentar buscar o objeto que foi excluído, uma mensagem de "Not found" irá aparecer.

ex: http://127.0.0.1:8000/copybook/5/

{
    "detail": "Not found."
}

----------------
 PYTHON REQUEST 
----------------

url = "../copybooks/5/"
headers = {...}
response = requests.request("DELETE", url, headers=headers)

```
###### SEARCH AND FILTERS

```

---------------------
FRONT END DJANGO REST 
---------------------

Em http://127.0.0.1:8000/copybook/ temos a nossa disposição um botão "FILTERS", nele podemos fazer buscas no endpoint copybook. Podemos buscar por edition e date register e podemos ordenar estes em ordem ascending e descending.

Exemplos de busca:

http://127.0.0.1:8000/copybook/?search=12

Exemplos de filtro e ordenação:

http://127.0.0.1:8000/copybook/?ordering=edition&search=12


----------------
 PYTHON REQUEST 
----------------

import requests

url = "http://127.0.0.1:8000/books/"

querystring = {"search":12}

headers = {...}

response = requests.request("GET", url, headers=headers, params=querystring)



```

## Navegando pelo endpoint /rentbook

###### CREATE
```
---------------------
FRONT END DJANGO REST 
---------------------

Em http://127.0.0.1:8000/rentbook/ é possível ter acesso ao json com as informações da api, para adicionar um novo objeto preencha  os campos name, date initial rent, delivery date forecast, date devolution, librarian e book com informações válidas. Clique no botão "POST" para criar um novo objeto.

{
    "date_initial_rent": [
        "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
    ],
    "delivery_date_forecast": [
        "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
    ]
}

----------------
 PYTHON REQUEST 
----------------

import requests

url = "http://127.0.0.1:8000/rentbook/"

payload = {"name":"Rosa Souza","date_initial_rent":"2019-07-04","delivery_date_forecast":"2019-07-22","date_devolution":null,"librarian":1,"book":3}
headers = {
    'Authorization': "Basic YWRtaW46bm92YVNlbmhhQA==",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "11772453-12b2-45af-b999-fbf3ccf89e2b,7bb0914d-5ace-49d9-8284-6ede6ffefa06",
    'Host': "127.0.0.1:8000",
    'accept-encoding': "gzip, deflate",
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'content-length': "639",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
   
data = json.dumps(payload)
response = requests.request("POST", url, data=data, headers=headers)

```
###### UPDATE 

```
---------------------
FRONT END DJANGO REST 
---------------------

Em http://127.0.0.1:8000/rentbook/id/ é possível ter acesso ao json com as informações de cada livro individualmente, modifique as informações de algum campo e clique no botão "PUT" para aplicar as mudaças a algum campo. 

ex: http://127.0.0.1:8000/rentbook/4/

{
    "id": 4,
    "name": "Maria",
    "date_initial_rent": "2019-07-05",
    "delivery_date_forecast": "2019-07-20",
    "date_devolution": null,
    "librarian": 1,
    "book": 12
}

----------------
 PYTHON REQUEST 
----------------

ATUALIZANDO TODOS OS CAMPOS 

import requests

url = "http://127.0.0.1:8000/rentbook/4/"

payload = {"name":"Rosa Souza Gomes","date_initial_rent":"2019-07-04","delivery_date_forecast":"2019-07-22","date_devolution":null,"librarian":1,"book":4}
headers = {...}
data = json.dumps(payload)
response = requests.request("PUT", url, data=data, headers=headers)


ATUALIZANDO CAMPO ESPECÍFICO

import requests

url = "http://127.0.0.1:8000/rentbook/4/"

payload = {"book":3}
headers = {...}
response = requests.request("PATCH", url, data=payload, headers=headers)


```

###### DELETE

```
---------------------
FRONT END DJANGO REST 
---------------------

Em http://127.0.0.1:8000/copybook/id/ além de ter acesso ao json com as informações de cada aluguel individualmente, temos também a disposição um botão para deletar o aluguel específico. Após clicar em "DELETE" e na confirmação "DELETE" o aluguel do livro é excluído do db e deixa de existir na API.

Se você excluir o id e tentar buscar o objeto que foi excluído, uma mensagem de "Not found" irá aparecer.

ex: http://127.0.0.1:8000/rentbook/4/

{
    "detail": "Not found."
}


----------------
 PYTHON REQUEST 
----------------

url = "../rentbook/4/"
headers = {...}
response = requests.request("DELETE", url, headers=headers)


```
###### SEARCH AND FILTERS

```
---------------------
FRONT END DJANGO REST 
---------------------

Em http://127.0.0.1:8000/rentbook/ temos a nossa disposição um botão "FILTERS", nele podemos fazer buscas no endpoint copybook. Podemos buscar por id, name e delivery date forecast, podemos ordenar name e delivery date forecast  em ordem ascending e descending.

----------------
 PYTHON REQUEST 
----------------

import requests

url = ".../rentbook/"

querystring = {"search":4}

headers = {...}

response = requests.request("GET", url, headers=headers, params=querystring)

```




