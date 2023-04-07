Assistente de Voz pessoal usando ChatGPT
========================================

Este é um projeto ainda em estágio inicial de um assistente de voz pessoal utilizando uma integração com a API da OpenAI, usando o modelo de inteligência ChatGPT. Dentro dele é possível determinar o nome para ativação das ações, assim como a palavra ou frase determinando o desligamento da aplicação.

|Nome|Tipo|Descrição|
|----|----|---------|
|`openai.api_key`|string|A chave secreta para interação com os serviços da OpenAI. Pode ser gerada no [console de desenvolvedor](https://platform.openai.com/account/api-keys) da empresa.|
|`model_engine`|string|O modelo da inteligência a ser utilizado como gerador das respostas. Uma lista completa pode ser visualizada atraves da [pagina na doumentação](https://platform.openai.com/docs/models) da OpenAI|
|`assistant_name`|string|Nome ou palavra chave a ser utilizada como comando para o assistente ouvir a interação|
|`end_assistant_command`|string|Palavra ou frase a ser utilizada como comando para encerramento da aplicação|

## Execução local

Para executar o projeto localmente é necessário ter instalado a versão mais atualizada do Python.

Clone esse projeto em sua máquina e inicie um ambiente virtual ('virtual environment') utilizando a ferramenta [virtualenv](https://virtualenv.pypa.io/en/latest/).

Para instalar a ferramenta:
```
pip install virtualenv
```

Para iniciar o ambiente:
```
virtualenv venv
```

Para selecionar o ambiente como fonte das bibliotecas:
```
source venv/Scripts/activate
```

Se no CMD do windows, utilizar somente o comando a seguir:
```
.\venv\Scripts\activate
```

Por último, instale os pacotes necessários a partir do arquivo de requirements presentes no projeto:
```
pip install -r requirements.txt
```

Agora está tudo pronto! Para finalizar o procedimento, agora execute a aplicação já com as propriedades devidamente preenchidas usando o comando:
```
python app.py
```


## Colaborações

O projeto foi criado com o intuito de melhorar a experiência com assistentes virtuais a partir da ferramenta que recentemente tomou a internet de assalto: o ChatGPT. Pela natureza colaborativa do experimento, toda e qualquer colaboração ou melhoria é bem-vinda!

Contate-me através do email f.netto01@gmail.com ou simplesmente através da plataforma Github.

## Licença

O projeto se encontra sob a licença MIT.