# HELLO FALCON

Programa simples para criar uma endpoint no navegar localmente.

## Começando

O presente projeto foi desenvolvido em Linux/Ubuntu, e todas as suas instruções serão baseadas nesses sistema operacional. Siga as descrições para rodar o programa.

### Pré-requisitos

Primeiramente será necessário ter instalado em sua máquina:
- Python 3.7+
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation/)

### Instalando

Crie um ambiente virtual:
```python
virtualenv -p python3.7 ENV
```

Entre no ambiente virtual:
```python
source ENV/bin/activate
```

Dentro do ambiente virtual, instale as dependências:
```python
pip install -r requirements/base.txt
```

### Rodando o programa

Com o ambiente preparado, execute o código principal:
```python
gunicorn hello:app
```

Assim que executar o comando, o terminal retornará uma mensagem equivalente a essa:
```bash
[2019-09-04 20:58:43 -0300] [7019] [INFO] Starting gunicorn 19.9.0
[2019-09-04 20:58:43 -0300] [7019] [INFO] Listening at: http://127.0.0.1:8000 (7019)
[2019-09-04 20:58:43 -0300] [7019] [INFO] Using worker: sync
[2019-09-04 20:58:43 -0300] [7022] [INFO] Booting worker with pid: 7022
```

Essa é a mensagem indicando que o programa está rodando localmente.

Agora, basta acessar o navegador no endereço `http://127.0.0.1:8000` ou `localhost:8000`.
