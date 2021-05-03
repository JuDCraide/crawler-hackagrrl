<p align="center">
  <h1 align="center">Crawler Ada's Girls</h1>
</p>

<h4 align="center">
  <a href="#information_source-sobre-o-projeto">Sobre</a> |
  <a href="#nut_and_bolt-funcionalidades">Funcionalidades</a> |
  <a href="#books-tecnologias-e-ferramentas">Tecnologias e ferramentas</a>
</h4>
<h4 align="center">
  <a href="#package-como-baixar-o-projeto">Como baixar o projeto</a>
</h4>

## :information_source: Sobre o Projeto
Template utilizado para avalização de code review na Hack GRRRL 2021 ✨👩‍💻✨
### Objetivo e Motivações

Mesmo com todos os avanços em pleno século XXI, a sociedade continua sendo em sua maior parte machista. Tendo em vista o desafio "Ética e Marketing para o público feminino", resolvemos abordar a questão de como as mulheres, antes de comprar algum produto ou serviço, podem saber se a empresa/marca por trás do mesmo tem uma boa representatividade de mulheres em propagandas. Portanto, temos como propósito trazer informações relacionadas as propagandas das marcas (se têm diversidade, inclusão ou se são sexistas, machistas, objetificam a mulher...) e como é o engajamento delas em prol das causas femininas.

Nosso objetivo é prover, para as mulheres, de maneira simplificada, uma plataforma que reúna empresas/marcas e suas respectivas reputações com propagandas relacionadas a mulheres, além de notícias que corroborem com as avaliações.

Uma das principais inspirações para o desenvolvimento da nossa solução foi o site https://modalivre.org.br/. Uma plataforma de funcionamento semelhante, que incentiva o consumidor a comprar roupas de maneira consciente ao avalia marcas quanto ao emprego de trabalho escravo em suas produções e suas ações para evitar que isso aconteça.

### Que tecnologias vocês usaram no hackathon?
Para esse hackathon desenvolvemos 3 aplicações integradas para resolver o problema proposto.
Optamos por separar bem as funções entre os 3:

- Frontend utilizando javascript com ReactJS para desenvolver as interfaces com as usuárias.
- Backend, utilizando javascript com NodeJS e uma base de dados não relacional MongoDB, para armazenar e prover os dados sobre as empresas e notícias.
- Web Crawler, utilizando python para obter e analisar dados de sites de notícias


### Por que vocês escolheram essas tecnologias?
No frontend e backend utilizamos as tecnologias anteriormente citadas por já serem de conhecimento prévio de algumas integrantes da equipe. Já para o crawler foi escolhido o python pois pareceu a opção com a menor curva de aprendizado para atingir o objetivo proposto para ele.

### Qual foi a maior desafio (da parte de desenvolvimento) durante o hackathon? Como vocês resolveram?
Houveram algumas complicações relacionadas ao desenvolvimento do Crawler. Localizar a posição correta das tags e dos links foi um desafio, pois para cada site existe uma estrutura diferente. Para resolver esse desafio foi necessário uma análise detalhada do código de cada página, para assim, localizar corretamente as partes necessárias. Além disso, o curto tempo para desenvolver tamanha solução foi restritívo tendo que nos limitar a fazer um MVP.

### Qual foi o maior aprendizado (ou uma parte do código que vocês achem massa e estão orgulhosas)?
Ficamos orgulhosas de aprender a desenvolver um crawler, pois não tínhamos experiência, e com a qualidade em geral da solução entregue.

### Se vocês fossem participar de um hackathon semana que vem, fariam algo de diferente com relação às escolhas das tecnologias utilizadas?
Não, pois acreditamos que as tecnologias nos proporcionaram um grande aprendizado, além de entregar uma boa solução.

## :nut_and_bolt: Funcionalidades

✔️ Crawler do site https://www.globo.com/ que salva notícias relacionadas a propagandas para a nossa API

## :books: Tecnologias e ferramentas

O projeto foi desenvolvido utilizando as seguintes tecnologias

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python3](https://www.python.org/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Selenium](https://www.selenium.dev/)

## :package: Como baixar o projeto

Para copiar o projeto, utilize os comandos:

```bash
  # Clonar o repositório
  ❯ git clone https://github.com/JuDCraide/crawler-hackagrrl

  # Entrar no diretório
  ❯ cd crawler-hackagrrl
```

Antes de rodar o projeto extraia o conteúdo do zip no disco local C:

Para instalar as dependências e iniciar o projeto, você pode utilizar o pip3.

```bash
  # Instalar as dependências
  ❯ pip3 install selenium beautifulsoup4 requests

  # Iniciar o projeto
  ❯ python3 main.py
```

<h4 align="center">
  Feito com ❤️ por Júlia D. Craide 👋️ Entre em contato!
</h4>
