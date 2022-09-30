# simpleapp-python

# Teste prático

## 1. Crie um Dockerfile
- Segue na estrutura raiz do projeto o dockerfile, para o processo de contenização necessitei adicionar o requirements.txt para instalar a dependência do flask.

## 1.1 Envie a imagem para um docker registry
- A imagem segue no seguinte registry: https://hub.docker.com/repository/docker/aldry1303/python-tempest-app

## 2.0 A partir da imagem da aplicação criada na questão 1, crie um Helm Chart para a aplicação:
- O chart está dentro da estrutura python-app-tempest, o mesmo nome do chart que criei, eu descidir criar dentro do chart apenas as funcionalidades básicas
de um service e um deployment mantendo 3 réplicas.

* Para utilizar visualizar o modelo é só setar o comando na raiz do projeto.

~~~javascript
helm template python-tempest-app ./python-app-tempest/ --set versionContainer=1.0.0
~~~

## 3:  Crie o cluster de Kubernetes (EKS) na AWS (automatizado, por exemplo, com Terraform ou CDK), e faça a implantação do Helm Chart da questão 2.

- Fiz o Cluster com kubernetes pelo terraform, o diretorio iac conto com os arquivos Terraform.
* Para iniciar o cluster é necessário logar no seu provider com a CLI da AWS e ezecutar o comando
~~~javascript
terraform init
~~~
* E Depois para verificar que recursos serão aplicados:
~~~javascript
terraform plan 
~~~
* E para aplicar:
~~~javascript
terraform apply 
~~~
- Para fazer deploy da aplicação via helm é só setar o seguinte comando:
~~~javascript
helm upgrade --install python-tempest-app ./python-app-tempest/ --set versionContainer=1.0.0
~~~

- Para testar a aplicação é só setar o comando:
~~~javascript
kubectl get svc 
~~~
- E chamar a aplicação via o endereço do loandbalancer gerado.
* OBS: Esperar uns minutos antes de chamar para o loandBalancer Syncar

## 4: Configure a monitoração dos recursos do Kubernetes (Prometheus, ELK, Datadog e etc....).

- Subir tudo via istio service mesh, para aplicar as alterações é só entrar no diretorio *setup-monitoring* e executar o seguinte comando:
~~~javascript
sh telemetry-istio.sh
~~~
- Em seguida estrá pronto e configurado o Kiali, o Prometheus, o Grafana e o Jeaguer.
    - O grafana já vem com dashboards nativos para a observabilidade dos componentes que estão com a label do istio-inject
- Você poderá ver os dashboards da seguinte maneira:
- Para vê o kiali 
~~~javascript
istioctl dashboard kiali
~~~
- Para vê o prometheus 
~~~javascript
istioctl dashboard prometheus
~~~
- Para vê o grafana 
~~~javascript
istioctl dashboard grafana
~~~

*OBS, caso não esteja com istioctl setado é só executar o istioctl indo até dento do bin do pacote do istio.

## 5: Implante a ferramenta para coleta dos logs da aplicação, devem ser visualizados em um dashboard.
- Implantei via grafana Loki e promtail, deixei um script em um diretório chamado *setup-loki-logs*, ele já faz todo
o setup e exponhe o grafana para vizualização de logs via LoandBalancer. 
- Para executar: 
~~~javascript
sh loki-logs.sh
~~~
* OBS: Esperar uns minutos antes de chamar para o loandBalancer Syncar.
- O deamonset vai mapear os namespaces e coletar tudo no loki possibilitando a visualização no grafana.
## 6: Desenvola o script (Python ou Go) que liste todos os recursos criados anteriormente na conta da AWS.

- Dentro do diretório automation-python tem o script com o seu Readme, que auxilia a execução.

## Obrigado <3
