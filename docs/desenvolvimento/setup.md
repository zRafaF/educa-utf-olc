# Setup

Esta página fornece um guia detalhado para configurar este projeto. Certifique-se de seguir cada passo cuidadosamente.

Para executar este projeto, você precisará de [Python](https://www.python.org/), **PIP** e **GIT**.

> Este projeto foi desenvolvido utilizando a versão `Python 3.11`.

## Clonar o repositório

Abra o terminal e execute os seguintes comandos:

```bash
git clone https://github.com/ZRafaF/educa-utf-olc

cd educa-utf-olc
```

## Criando um ambiente virtual

> A criação de um ambiente virtual não é obrigatória, mas é altamente **recomendada**. Para saber mais sobre ambientes virtuais em Python, visite [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html).

Execute os seguintes comandos para criar e ativar um ambiente virtual:

```bash
python -m pip install --user virtualenv

python -m venv venv
```

Um diretório ``venv`` será criado na pasta raiz do projeto.


### Ativação do Ambiente Virtual

!!! admonition-windows "Ativação no **Windows**"

    ``` bash title=""
    venv/Scripts/activate
    ```

ou

!!! admonition-linux "Ativação no **Linux**"

    ``` bash title=""
    source venv/bin/activate
    ```

---

Com o ambiente virtual ativado, qualquer biblioteca instalada será aplicada apenas a este ambiente.

## Instalando dependências

Execute o seguinte comando para instalar todas as dependências listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

Agora seu ambiente está pronto para executar a aplicação.

## Testes

Para obter informações sobre os testes, consulte [Desenvolvimento-Testes](./testes.md)

## Documentação

Para executar ou contribuir para a documentação, consulte [Desenvolvimento-Documentação](./documentacao.md)
