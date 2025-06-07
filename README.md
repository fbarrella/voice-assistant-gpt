Assistente de Voz pessoal usando ChatGPT
========================================

Este é um projeto ainda em estágio inicial de um assistente de voz pessoal utilizando uma integração com a SDK da OpenAI, usando o modelo de inteligência Deepseek. Dentro dele é possível determinar o nome para ativação das ações, assim como a palavra ou frase determinando o desligamento da aplicação.

|Nome|Tipo|Descrição|
|----|----|---------|
|`API_KEY`|string|A chave secreta para interação com o modelo Deepseek (deepseek/deepseek-r1-0528:free), via API do _OpenRouter.ai_. Pode ser gerada no [página do modelo](https://openrouter.ai/deepseek/deepseek-r1-0528:free/api) do site.|
|`MODEL_ENGINE`|string|O modelo da inteligência a ser utilizado como gerador das respostas. Pode-se definir qualquer um desejado, mas no exemplo aqui usaremos o modelo free da Deepseek: **deepseek/deepseek-r1-0528:free** |
|`CALLOUT`|string|Nome ou palavra chave a ser utilizada como comando para o assistente ouvir a interação|
|`DISMISSAL`|string|Palavra ou frase a ser utilizada como comando para encerramento da aplicação|

Basta adicionar esses parâmetros em um arquivo `.env` no projeto, com os determinados valores associados. Somente o parâmetro `API_KEY` é obrigatório, os outros são opcionais.

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