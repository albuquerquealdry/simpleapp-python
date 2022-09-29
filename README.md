# simpleapp-python

# Teste prático

## 1. Crie um Dockerfile
- Segue na estrutura raiz do projeto o dockerfile, para o processo de contenização necessitei adicionar o requirements.txt para instalar a depedência do flask.

## 1.1 Envie a imagem para um docker registry
- A imagem segue no seguinte registry: https://hub.docker.com/repository/docker/aldry1303/python-tempest-app

## 2.0 A partir da imagem da aplicação criada na questão 1, crie um Helm Chart para a aplicação:
- O chart está dentro da estrutura python-app-tempest, que é o mesmo nome do chart que criei, eu descidir criar dentro do chart apenas as funcionalidades básicas
de um service e um deployment mantendo 3 réplicas.

* Para utilizar vizualizar o template é só setar o comando na raiz do projeto.

~~~javascript
helm template python-app-tempest ./python-app-tempest/ --set versionContainer=1.0.0
~~~