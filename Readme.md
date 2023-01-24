
# Função lambda para ler csv e salvar no banco de dados

Projeto desenvolvido para o teste da empresa EDESOFT, utilizando Chalice AWS - para facilitar o deploy do lambda e criação do endpoint na API  Gateway da AWS

## Stack utilizada

**Front-end:** React, Redux, Material Ui


## Documentação

- Necessario configurar o banco de dados no arquivo app.py


### Credenciais para deploy
```
$ mkdir ~/.aws
$ cat >> ~/.aws/config
[default]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
region=YOUR_REGION (such as us-west-2, us-west-1, etc)
```

### Deploy
```
    chalice deploy
```


### local
```
    chalice local
```


## Melhorias

Para desenvolvimento
- Setar variaveis de ambiente 
- TDD / Testes
- Configurações de segurança da Api Gateway. 


