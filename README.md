# pcce_api_test

## Instalação
#### Após baixar o repositório execute no raiz:

1 - `pip install -r requirements.txt`

2 - `python manage.py makemigrations`

3 - `python manage.py migrate`

3 - `python manage.py runserver`

## Endpoints

#### Do endereço **localhost:8000** teste chamadas http para os seguintes endpoints: 

**api/v1/armas** para listar e criar armas

**api/v1/municoes** para listar e criar municoes

**api/v1/calibres** para listar e criar calibres

**api/v1/objetos_tipo** para listar e criar objetos_tipo

**api/v1/armas/:id** para detalhar e atualizar arma

**api/v1/municoes/:id** para detalhar e atualizar municao

**api/v1/calibres/:id** para detalhar e atualizar calibre

**api/v1/objetos_tipo/:id** para detalhar e atualizar objeto_tipo

**api/v1/objetos** para listar objetos (apenas leitura - instanciada por objeto_tipo)


