# Início

O EducaUTF OLC é um microsserviço dedicado à classificação de dados e ciência de dados dentro do [EducaUTF](https://educautf.td.utfpr.edu.br/).

Escrito em Python, este serviço aceita solicitações de acesso ao seu conteúdo por meio de uma REST API. Em sua fase inicial, o OLC concentra-se na avaliação de **artigos** e **capítulos** em ascensão.

## O que é o EducaUTF?

O [EducaUTF](https://educautf.td.utfpr.edu.br/) tem como missão simplificar a criação e acessibilidade de materiais pedagógicos. 

Os usuários podem desenvolver materiais no formato de um **Blog interativo** utilizando um superconjunto da linguagem de marcação [Markdown](https://www.markdownguide.org/). Esse superconjunto permite que os editores incorporem componentes pré-fabricados em suas páginas, proporcionando uma experiência mais interativa para os usuários.

## Objetivos Futuros do EducaUTF OLC

O EducaUTF OLC continuará a evoluir, com planos futuros incluindo a execução de diversos algoritmos. Isso abrangerá desde **algoritmos de recomendação**, que ajudarão os usuários a descobrir conteúdos mais relevantes, até outras funcionalidades inovadoras. Estamos comprometidos em aprimorar constantemente a experiência de aprendizado no EducaUTF.

## Sobre essa documentação

A documentação deste microsserviço está organizada em diferentes tópicos, sendo acessível de diversas maneiras:

* **Web**: Explore online [aqui](https://zrafaf.github.io/educa-utf-olc).
* **PDF**: Faça o download [aqui](https://github.com/ZrafaF/educa-utf-olc/blob/gh-pages/pdf/document.pdf).


Se você está interessado em contribuir, um excelente ponto de partida é o tópico [Desenvolvimento](./desenvolvimento/index.md)

## Deploy

A implantação desta aplicação é realizada por meio de Docker Containers. Todo o repositório de imagens está disponível em [zrafaf/educa_utf_olc](https://hub.docker.com/r/zrafaf/educa_utf_olc).

O processo de *deploy* é executado através de um ***pull request*** na *branch* `release`. Isso inicia uma automática build e release usando o [GitHub Actions](https://github.com/features/actions). Estamos sempre buscando aprimorar e facilitar o processo de implantação.
