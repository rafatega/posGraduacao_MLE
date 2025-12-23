# Machine Learning Engineering

# Python para ML e IA

## Aula 1 - Por que a pessoa engenheira de Machine Learning precisa saber APIs?

O engenheiro de Machine Learning é responsável por transformar um modelo em produto.

É muito comum termos um modelo de ML rodando localmente, em nossos notebooks, não entregando valor contínuo para o negócio. Para resolver esse problema, precisamos criar um serviço consumivel (API).

### Definições

* API
Application Programming Interface, um conjunto de regras e protocolos que permite a comunicação entre diferentes softwares, fornecendo rotas para acessar funcionalidades específicas.

![API](../app/Imagens/analogiaAPI.png)
O usuário vai pedir o prato, o garçom (API) vai levar o pedido para a cozinha (servidor) e depois trazer a comida pronta para o usuário.

* Qual o papel de uma API em Machine Learning?
1. Conecta o modelo treinado a aplicações finais.
2. Recebe dados de entrada e retorna previsões.
3. Evita explosição desnecessária do código para os usuários finais.

* Por que integrar ML e APIs?
1. Disponibilizar previsões em tempo real.
2. Padronizar acesso a modelos entre diferentes sistemas.
3. Ganhar escalabiliodade: cada serviço cuida  de uma parte.
4. Melhorar a segurança: controle de quem acessa o modelo.
5. Otimizar o desenvolvimento colaborativo.
6. Tornar o modelo um `produto` de fato.

### Exemplos práticos
1. Sistema de recomendação de filmes via endpoint /recommend.
2. Análise de sentimento para redes sociais e help desk.
3. Classificação de imagem em apps de diagnóstico médico.
4. Previsão de demanda em e-commerce.
5. Google Maps API: Permitindo que desenvolvedore integrem mapas, rotas e funcionalidades em seus aplicativos.
6. Twitter API: fornece acesso aos dados de tweets, permitindo que desenvolvedores criem análise de sentimento dos tweets.

### Exemplo de fluxo
Recomendação de filmes:
1. Usuário envia histórico de preferências via POST;
2. API processa dados e consulta modelo de recomendação;
3. Resposta é uma lista de filmes sugeridos;
4. Front-end recebe e exibe para o usuário;
5. Tudo isso sem revelar a lógica interna do modelo.

### API Rest
* REST (Representational State Transfer) é um estilo arquitetural para projetar APIs.
* Utiliza métodos HTTP (GET, POST, PUT, DELETE) para operações.
* Stateless: cada requisição é independente.
* Cacheável: melhora desempenho e escalabilidade.

* Exemplo de endpoint:
1. URL: https://api.meusistema.com/predict
2. Método: POST com payload de dados.
3. Resposta: JSON com previsões.
4. Separação clara entre cliente e servidor.
5. Permite versionamento: /v1/predict, /v2/predict.

### Dicas de estrutura de Endpoints
1. Usar verbos HTTP corretamente (GET para obter dados, POST para criar).
2. Nomear endpoints de forma intuitiva (/predict, /train).
3. Evitar URLs muito longas ou complexas.
4. Retornar códigos de status HTTP adequados (200, 400, 500).
5. Manter consistência entre endpoints e parâmetros.

### Boas práticas para o desenvolvimento
1. Código limpo e organizado por rotas.
2. Padrões claros de nomenclatura.
3. Testes unitários e de integração.
4. Manter a lógica de negócio separada da lógica de API.
5. Evitar "tudo em um único arquivo".
6. Uso de ambientes virtuais e gerenciadores de dependências.
7. Lidar com exceções e erros de forma adequada.
8. Logar eventos críticos e respostas do servidor.
9. Garantir retornos em JSON.
10. Reduzir latência com otimizações simples.

### Autenticação e autorização
* Autenticação: Verifica a identidade do usuário (ex: tokens, API keys).
* Autorização: Define o que o usuário autenticado pode fazer (ex: permissões).

### Documentação com Swagger
* Ferramenta para documentar APIs de forma interativa e atualizada.
* Permite testar endpoints diretamente na documentação.
* Reduz a curva de aprendizado para novos desenvolvedores.

### Ferramebtas e arquiteturas
* Fast API
Framework moderno e rápido para APIs em Python, com validação automática de dados e documentação integrada. 
* Flask
Framework leve e flexível que permite criar APIs simples e rápidas, ideal para prototipagem e projetos de ML.
* Django Rest Framework
Extensão do Django para construir APIs robustas e escaláveis, com suporte a autenticação, permissões e serialização de dados.

Neste curso passaremos mais por Fast API e Flask.

### Desafios em produção
1. Latência: Ocorre quando o tempo de resposta é alto. Para mitigar isso, precisamos otimizar  o código, usar caching e balanceamento de carga. Além de monitorar o desempenho constantemente.
2. Escalabilidade: Aumentar a capacidade do sistema para lidar com mais requisições. Utilizar contêineres (Docker), orquestração (Kubernetes) e serviços em nuvem (AWS, GCP).
3. Segurança: Proteger dados sensíveis e evitar ataques. Implementar autenticação, autorização, criptografia e monitoramento de segurança.
4. Custo: Gerenciar os custos operacionais. Otimizar recursos, usar serviços sob demanda e monitorar gastos regularmente.



