# Gerenciador de arquivos super simples utilizando Python e GCS

## Criando uma conta gratuíta (de teste) na GCS

* Acesse [GoogleCloudStorage](https://www.google.com/aclk?sa=l&ai=DChcSEwiPid74mrn-AhVq6FwKHZ6-AIIYABACGgJjZQ&sig=AOD64_0Bua6qNJPjx-4Ld0PHrzv5mV3Z0Q&adurl&ved=2ahUKEwj9i9f4mrn-AhWXH7kGHVJfBwgQqyQoAHoECAcQCw) para criar uma conta gratuíta.

* Necessário informar um cartão de crédito, mesmo que não seja cobrado.

## Instalando o gcloud cli
* Siga o tutorial disponível aqui [GoogleCloudCLI](https://cloud.google.com/sdk/docs/install?hl=pt-br) para a instalação. Lembrando que não ela não é necessária para que o python possa se conectar ao storage, apenas para que possamos utilizá-la através da Interface por Linha de Comando, através do terminal (como de fato sugere o termo cli). 

* Uma opção (das informadas no tutorial) muito simples é através do snap:
    - snap install google-cloud-cli --classic
    - Agora já é possível rodar gsutil e gcloud


## Exportando as variávies

- Realize o login:
    - gcloud auth login

* Exporte as credenciais de acesso:
    - gcloud auth application_default login
        - ![exportano credenciais](./images/credenciais_borrada.png)

        - ![credenciais](./images/exportando_credenciais_borradas.png)

    - Desta forma, o endereço do json exportado pode ser usado agora como variável de ambiente, assim como foi feito neste repositório, para que seja possível o acesso ao storage através do python.

## Utilizando a ferramenta gsutil
`Uma vez instalado o cli, podemos agora acessar o storage da cloud através do terminal, uma vez estando logado.`

- Uma vez realizado o login, é possível ter acesso ao storage através do gsutil, o qual possui muitas das funcionalidades disponíveis em um terminal linux:

    * __Listando arquivos:__
        - `gsutil ls ou gsutil ls -flag`
            - ![listando buckets](./images/listando_arquivos_1.png)
            - ![listando arquivos](./images/listando_arquivos_2.png)
            - ![listando arquivos por extensão](./images/listando_por_extensao.png)

    * __Copiando arquivos:__
        - `gsutil cp origem.extensao gs://nome_bucket/destino.extensao`
        - `gsutil cp gs://nome_bucket/origem.extensao destino.extensao`
        - ![copiando arquivos](./images/copiando_arquivos.png)

    * __Removendo arquivos:__
        - `gsutil rm gs://nome_bucket/arquivo.extensao`
        - ![removendo arquivos](./images/removendo_arquivos.png)

    
    * __Fonte__: 
        - https://cloud.google.com/storage/docs/discover-object-storage-gsutil?hl=pt-br
        - https://cloud.google.com/storage/docs/gsutil/commands/help

