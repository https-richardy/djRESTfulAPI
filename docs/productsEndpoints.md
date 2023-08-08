## **Criando um Produto**  

### **Descrição**
Este endpoint permite criar um novo produto na API. Apenas usuários autenticados com permissões de administrador podem acessá-lo. A autenticação é feita via JWT (JSON Web Token)

> **POST** `/v1/store/product/create/`

### **Parâmetros da Requisição**
* **headers**:  
    `Authorization: Bearer <JWT_TOKEN>`  
    Substitua `<JWT_TOKEN>` pelo token JWT obtido após a autenticação do usuário.
* **body**:
    ```json
    {
        "title": "Nome do Produto",
        "cover": "imagem_base_64",
        "description": "Descrição do Produto",
        "category": {
            "title": "clothing"
        },
        "price": 29.99,
        "stock": 100
    }
    ```

### **Resposta**
* Status: `201 Created`  
    O Produto foi criado com sucesso.  

* Status: `401 Unauthorized`:
    ```json
    {
        "detail": "Você não tem permissão para realizar esta ação."
    }
    ```
    O usuário não está autenticado ou não possui as permissões necessárias para criar um produto.  

* Status `400 Bad Request`:
    ```json
    {
        "title": [
            "Este campo é obrigatório."
        ],
        "cover": [
            "Este campo é obrigatório."
        ],
        "description": [
            "Este campo é obrigatório."
        ],
        "category": [
            "Este campo é obrigatório."
        ],
        "price": [
            "Este campo é obrigatório."
        ],
        "stock": [
            "Este campo é obrigatório."
        ]
    }
    ```
    Erros de validação ocorrem quando os campos obrigatórios não são fornecidos ou estão em formato inválido.  


### **Autenticação**
A autenticação para acessar este endpoint é feita por meio de JSON Web Token (JWT). Certifique-se de incluir o token JWT válido no cabeçalho de autorização da requisição para ter acesso aos recursos de criação de produtos. Caso o token seja inválido ou ausente, o servidor responderá com o status 401 Unauthorized e impedirá o acesso ao endpoint. Certifique-se de obter o token JWT válido por meio do processo de autenticação adequado antes de fazer a chamada para este endpoint.

---

##  **Deleção de Produto**  

### **Descrição**
Este endpoint permite deletar um produto específico da API. Apenas usuários autenticados com permissões de administrador podem acessá-lo. A autenticação é feita via JWT (JSON Web Token).

> **DELETE** /v1/store/product/<<int:pk>>/delete/  
* Substitua `int:pk` pelo ID númeirco do produto que deseja deletar.

### **Pâmetros de Requisição**
* **Headers**:  
    `Authorization: Bearer <JWT_TOKEN>`  
    Substitua `<JWT_TOKEN>` pelo token JWT obtido após a autenticação do usuário.

### **Resposta**
* Status `204 No Content`:  
    Indica que o produto foi deletado com sucesso.

* Status `401 Unauthorized`:  
    ```json
    {
        "detail": "Você não tem permissão para realizar esta ação."
    }
    ```
    O usuário não está autenticado ou não possui as permissões necessárias para deletar um produto.

* Status `404 Not Found`:  
    ```json
    {
        "detail": "Não encontrado."
    }
    ```
    O Produto com o ID especificado não foi encontrado.

---
## **Obtendo Detalhes do Produto**  

### **Descrição**

Este endpoint permite visualizar os detalhes de um produto específico na API. Não requer autenticação, e qualquer usuário pode acessá-lo para obter informações sobre um produto.



> **GET** /v1/store/product/<<int:pk>>/  
* Substitua `<int:pk>` pelo ID numérico do produto que deseja visualizar.

### **Parâmetros de Requisição**  
Nenhum parâmetro de requisição é necessário.

### **Resposta**  
* Status `200 OK`:
    ```json
    {
        {
            "id": 1,
            "title": "Camiseta Branca",
            "cover": "imagem_url",
            "description": "Camiseta de algodão branca com estampa",
            "category": {
                "id": 1,
                "title": "clothing"
            },
            "price": "29.99",
            "stock": 100
        }
    }
    ```
    A resposta inclui o ID, título, capa, descrição, categoria, preço e estoque do produto.
* Status `404 Not Found`:  
    ```json
    {
        "detail": "Não encontrado."
    }
    ```

### **Autenticação**
Não é necessária autenticação para acessar este endpoint. Qualquer usuário pode fazer uma solicitação GET para visualizar os detalhes de um produto. Certifique-se de fornecer o ID do produto correto na URL para especificar qual produto você deseja visualizar.

---

## **Listando Produtos**  

### **Descrição**
Este endpoint permite listar todos os produtos disponíveis na API.
Não requer autenticação, e qualquer usuário pode acessá-lo para visualizar a lista de produtos. A resposta inclui a paginação dos resultados.


> **GET /v1/store/products/**


### **Parâmetros de Requisição**
Nenhum parâmetro de requisição é necessário.

### **Resposta**
* Status `200 OK`:
    ```json
    {
        "count": 10,
        "next": "http://localhost:8000/v1/store/products/?page=2",
        "previous": null,
        "results": [
            {
                "id": 1,
                "title": "Camiseta Branca",
                "cover": "imagem_url_aqui",
                "description": "Camiseta de algodão branca com estampa",
                "category": {
                    "id": 1,
                    "title": "clothing"
                },
                "price": "29.99",
                "stock": 100
            },
            // ... mais produtos
        ]
    }
    ```
* Status `404 Not Found`:
    ```json
    {
        "detail": "Não encontrado."
    }
    ```
    Nenhum produto foi encontrado.

### **Autenticação**
Não é necessária autenticação para acessar este endpoint. Qualquer usuário pode fazer uma solicitação GET para visualizar a lista de produtos. A resposta incluirá os links para a próxima página (next) e a página anterior (previous) sempre que houver mais resultados disponíveis. Certifique-se também de que a resposta esteja sendo tratada adequadamente para lidar com a paginação.

---

## **Filtrando produtos**  

### **Descrição**
Este endpoint permite listar produtos com a capacidade de aplicar filtros aos resultados. Não requer autenticação, e qualquer usuário pode acessá-lo para visualizar a lista de produtos filtrados. A resposta inclui a paginação dos resultados.

> **GET** /v1/store/products/search/

> **GET** /v1/store/products/search/?min_price=20&max_price=50&title=camiseta

### **Parâmetros de Requisição**
* **Query Parameters**  
    * `min_price` (opcional): Filtra produtos com preço maior ou igual ao valor fornecido.
    * `max_price` (opcional): Filtra produtos com preço menor ou igual ao valor fornecido.
    * `title` (opcional): Filta produtos que contenham o título especificado, de forma case-insensitive.
    * `category` (opcional): Filtra produtos pela categoria especificada.

### **Resposta**
* Status `200 OK`:
    ```json
        {
            "count": 5,
            "next": "http://localhost:8000/v1/store/products/?tile=camisa&page=1",
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "title": "Camiseta Branca",
                    "cover": "url da imagem",
                    "description": "Camiseta de algodão branca com estampa",
                    "category": {
                        "id": 1,
                        "title": "clothing"
                    },
                    "price": "29.99",
                    "stock": 100
                },
                // ... mais produtos
            ]
        }
    ```
* Status `404 Not Found`:
    ```json
    {
        "detail": "Não encontrado."
    }
    ```

### **Autenticação**
Não é necessária autenticação para acessar este endpoint. Qualquer usuário pode fazer uma solicitação GET para visualizar a lista de produtos filtrados. Certifique-se de utilizar os query parameters fornecidos na URL para aplicar os filtros desejados. A resposta incluirá os links para a próxima página (next) e a página anterior (previous) sempre que houver mais resultados disponíveis após a aplicação dos filtros.

---

## **Atualizando um produto**  

### **Descrição**
Este endpoint permite atualizar os detalhes de um produto específico na API. Apenas usuários autenticados com permissões de administrador podem acessá-lo. A autenticação é feita via JWT (JSON Web Token).

> **PUT** /v1/store/product/<<int:pk>>/update/

> **PATCH** /v1/store/product/<<int:pk>>/update/

* Substitua `<int:pk>` pelo ID numérico do produto que deseja atualizar.

#### **Suporte a `PUT` e `PATCH`**
O endpoint de atualização de produto suporta tanto o método PUT quanto o método PATCH:  
* **PUT**: 
    Ao usar o método PUT, você deve fornecer todos os campos obrigatórios do produto no corpo da requisição, mesmo que eles não tenham sido alterados. Isso resultará na substituição completa das informações do produto pelos valores fornecidos no corpo.
* **PATCH**: 
    No método PATCH, você pode fornecer apenas os campos que deseja atualizar no corpo da requisição. Os campos não fornecidos permanecerão inalterados.


Lembre-se de que você pode optar por usar PUT ou PATCH, dependendo da sua necessidade. Se quiser substituir completamente as informações do produto, use PUT. Se quiser atualizar apenas campos específicos, use PATCH. Ambos os métodos podem ser usados para realizar a atualização do produto com sucesso.


### **Parâmetros de Requisição**  
* **Headers**:  
    `Authorization: Bearer <JWT_TOKEN>`  
    Substitua `<JWT_TOKEN>` pelo token JWT obtido após a autenticação do usuário.
