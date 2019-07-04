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

2. Logue como super user para ter acesso a api 

```
login: admin
senha: novaSenha@
```
_Se tentar ter acesso aos endpoints sem ter logado aparecerá uma mensagem de "Authentication credentials were not provided."_
