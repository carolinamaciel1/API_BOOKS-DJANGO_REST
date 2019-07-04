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

3. Navegando pelo endpoint /books

```
Em http://127.0.0.1:8000/books é possível ter acesso ao json com as informações da api, para adicionar um novo objeto preencha com os campos nome do livro, autor do livro, data de registro do livro na biblioteca, editora que publicou o livro com informações válidas.

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
