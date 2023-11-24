# Setup

Esta página definirá o passo a passo para configurar este projeto.


Para executa-lo você precisará de [Python](https://www.python.org/), **PIP** e **GIT**.

> Este projeto foi desenvolvido usando a versão Python `Python 3.11`.

## Clonar o repositório

```bash
git clone https://github.com/ZRafaF/educa-utf-olc

cd educa-utf-olc
```

## Criando um ambiente virtual

> A etapa a seguir não é obrigatória, mas é **recomendada**. Se você quiser saber um pouco mais sobre ambientes virtuais de python visite [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)

```bash
python -m pip install --user virtualenv

python -m venv venv
```

Um diretório `venv` deve ser criado na pasta raiz do projeto.

Como ativar:

!!! admonition-windows "Ativação no **Windows**"

    ``` bash title=""
    venv/Scripts/activate
    ```

or

!!! admonition-linux "Ativação no **Linux**"

    ``` bash title=""
    source venv/bin/activate
    ```

---

Com isso o ambiente virtual estará ativado e qualquer biblioteca instalada será aplicada apenas à esse ambiente.

## Instalando dependências

```bash
pip install -r requirements.txt
```

Esse comando irá instalar todas as dependências contidas no arquivo `requirements.txt`




## Documentação
Para poder editar a documentação será preciso instalar suas **dependências** com:

```bash
pip install -r docs/requirements.txt
```

Após isso utilize o comando a seguir para servir a documentação no `localhost`:

``` sh
mkdocs serve
```

Ou o comando a seguir para criar uma build completa da documentação

``` sh
mkdocs build
```

!!! info
    A documentação desse projeto também pode ser acessada em formato de `.pdf`, entretanto esse so será criado caso seja a variável de ambiente `ENABLE_PDF_EXPORT` seja igual a `1`.
    ``` sh
    ENABLE_PDF_EXPORT: 1
    ```