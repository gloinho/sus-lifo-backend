# SUS-LIFO-BACKEND

> Processo Seletivo DOX - Teste técnico (SUS-LIFO)

O gerente (da UPA) ficou maluco! Precisamos de um sistema para gerenciar a fila de pacientes que não param de chegar e a regra é: o último a chegar é o primeiro a ser atendido.
Você deverá implementar um mini-sistema web com as seguintes caracteristicas:

- Front web em Flutter
- Duas telas: a inicial mostrará o último paciente que chegou na fila, a alternativa deverá permitir ao usuário de registrar um novo paciente. O input do usuário nesse caso é somente seu nome
- **Backend em python usando o framework flask.**
- **Os dados deverão ser persistidos em um banco de dados MySQL.**
- **Tecnologia recomendada: sqlalchemy**
- Entregável: arquivo zip com o código para o front e o back com instruções de como rodar o código.
- Será analisado sobretudo a organização do código

## Pre-requisitos

- python
- docker
- docker-compose

## Como usar

1. Clone o repositório ou baixe o arquivo zipado.
2. Crie e ative o ambiente virtual

```bash
pip install virtualenv
```

### Windows

```bash
py -m venv .venv
.venv/Scripts/activate
```

### Linux

```bash
python3 -m venv .venv
source venv/bin/activate
```

3. Instale as dependencias necessárias

```bash
pip install -r requirements.txt`
```

4. Suba o container

```bash
docker-compose up -d
```

5. Rode os seguintes comandos

```bash
flask db migrate
flask db update
flask run
```

6. Acesse o swagger
   `http://localhost:5000`
