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
http://127.0.0.1:8000/admin

login: admin
senha: novaSenha@
```

## Navegando pelo endpoint /books
###### CREATE
```
Em http://127.0.0.1:8000/books é possível ter acesso ao json com as informações da api, para adicionar um novo objeto preencha  os campos nome do livro, autor do livro, data de registro do livro na biblioteca, editora que publicou o livro com informações válidas. Clique no botão "POST" para criar um novo objeto.

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
```
###### UPDATE 

```
Em http://127.0.0.1:8000/books/id/ é possível ter acesso ao json com as informações de cada livro individualmente, modifique as informações de algum campo e clique no botão "PUT" para aplicar as mudaças a algum campo. 

ex: http://127.0.0.1:8000/books/3/

{
    "id": 3,
    "name_book": "Alice: As aventuras de Alice no país das maravilhas e através do espelho e oque encontrou por lá",
    "author_book": "Lewis Carroll",
    "publishing_company": "Zahar",
    "registration_date": "2019-07-02"
}

```
###### DELETE

```
Em http://127.0.0.1:8000/books/id/ além de ter acesso ao json com as informações de cada livro individualmente, temos também a disposição um botão para deletar o livro específico. Após clicar em "DELETE" e na confirmação "DELETE" o livro é excluído do db e deixa de existir na API.

Se você excluir o id e tentar buscar o objeto que foi excluído, uma mensagem de "Not found" irá aparecer.

ex: http://127.0.0.1:8000/books/6/

{
    "detail": "Not found."
}
```
###### SEARCH AND FILTERS

```
Em http://127.0.0.1:8000/books/ temos a nossa disposição um botão "FILTERS", nele podemos fazer buscas no endpoint books. Podemos buscar por id, name book, author book, registration date e podemos ordenar o registration date em ordem ascending e descending.
```

## Navegando pelo endpoint /copybook

###### CREATE
```
Em http://127.0.0.1:8000/copybook/ é possível ter acesso ao json com as informações da api, para adicionar um novo objeto preencha  os campos date register, edition and book com informações válidas. Clique no botão "POST" para criar um novo objeto.

{
    "date_register": [
        "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
    ]
}
```
###### UPDATE 

```
Em http://127.0.0.1:8000/copybook/id/ é possível ter acesso ao json com as informações de cada livro individualmente, modifique as informações de algum campo e clique no botão "PUT" para aplicar as mudaças a algum campo. 

ex: http://127.0.0.1:8000/copybook/3/

{
    "id": 3,
    "date_register": "2019-01-02",
    "edition": 12,
    "book": 2
}

```

###### DELETE

```
Em http://127.0.0.1:8000/copybook/id/ além de ter acesso ao json com as informações de cada livro individualmente, temos também a disposição um botão para deletar o livro específico. Após clicar em "DELETE" e na confirmação "DELETE" o exemplar do livro é excluído do db e deixa de existir na API.

Se você excluir o id e tentar buscar o objeto que foi excluído, uma mensagem de "Not found" irá aparecer.

ex: http://127.0.0.1:8000/copybook/23/

{
    "detail": "Not found."
}
```
###### SEARCH AND FILTERS

```
Em http://127.0.0.1:8000/copybook/ temos a nossa disposição um botão "FILTERS", nele podemos fazer buscas no endpoint copybook. Podemos buscar por edition e date register e podemos ordenar estes em ordem ascending e descending.
```

## Navegando pelo endpoint /rentbook

###### CREATE
```
Em http://127.0.0.1:8000/rentbook/ é possível ter acesso ao json com as informações da api, para adicionar um novo objeto preencha  os campos name, date initial rent, delivery date forecast, date devolution, librarian e book com informações válidas. Clique no botão "POST" para criar um novo objeto.

{
    "date_initial_rent": [
        "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
    ],
    "delivery_date_forecast": [
        "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
    ]
}
```
###### UPDATE 

```
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

```

###### DELETE

```
Em http://127.0.0.1:8000/copybook/id/ além de ter acesso ao json com as informações de cada aluguel individualmente, temos também a disposição um botão para deletar o aluguel específico. Após clicar em "DELETE" e na confirmação "DELETE" o aluguel do livro é excluído do db e deixa de existir na API.

Se você excluir o id e tentar buscar o objeto que foi excluído, uma mensagem de "Not found" irá aparecer.

ex: http://127.0.0.1:8000/rentbook/10/

{
    "detail": "Not found."
}
```
###### SEARCH AND FILTERS

```
Em http://127.0.0.1:8000/rentbook/ temos a nossa disposição um botão "FILTERS", nele podemos fazer buscas no endpoint copybook. Podemos buscar por id, name e delivery date forecast, podemos ordenar name e delivery date forecast  em ordem ascending e descending.
```





