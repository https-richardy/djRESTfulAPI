# **djRESTfulAPI**

## **Descrição**
Este projeto é uma RESTful API criada com **Django** e **Django Rest Framework** para demonstrar meu conhecimento em criação de APIs REST. A API possui funcionalidades de autenticação JWT, listagem de produtos, exclusão de produtos, recuperação, paginação, atualização de um produto e filtragem com base em filtros específicos.

## **Documentação**
A documentação completa da API está disponível na pasta "docs". Lá você encontrará detalhes sobre como utilizar cada endpoint, os parâmetros disponíveis e exemplos de requisições e respostas.

## **Requisitos**
Para executar este projeto localmente, você precisará ter o Python instalado em sua máquina, juntamente com as bibliotecas listadas no arquivo `requirements.txt`.

## **Instalação**
* Clone o repositório para sua máquina local:
    ```bash
    git clone https://github.com/https-richardy/djRESTfulAPI.git
    ```
* Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

* Crie o banco de dados e aplique as migrações:
    ```bash
    python manage.py migrate
    ```
    (considerando que você está na pasta raiz do projeto em "scr")

* Configuração de variáveis de ambiente:  
    Para garantir a segurança das informações sensíveis do projeto, como a chave secreta e as cedenciais do banco de dados, é recomendado utilizar variáveis de ambiente em vez de armazenar essas informações diretamente no arquivo de configuração. Segue abaixo o passo a passo para configurar as variáveis de ambiente:  
    * Renomeie o arquivo `.env-example` para `.env`.
    * Abra o arquivo `.env` em um editor de texto e preencha as informações necessárias.

* Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
## **Utilização**
Acesse a API em `http://localhost:8000/` e utilize os endpoints fornecidos para interagir com os recursos disponíveis. Para acessar o painel de administração, vá para `http://localhost:8000/admin/` e faça login com as credenciais do superusuário criado anteriormente e cadastre alguns produtos.
