<!--
 Copyright (c) 2023 Rafael F.M. & Reinaldo
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

# Documentação

A documentação desse projeto foi criada utilizando [MkDocs](https://www.mkdocs.org/) juntamente com [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) e alguns outros plugins.

## Auto documentação

Para gerar documentação automática do código está sendo usado o [mkdocstring](https://mkdocstrings.github.io/), com o handler [mkdocstrings-python](https://mkdocstrings.github.io/python/)

O padrão utilizado nesse projeto é o [Google-style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html), também são suportados alguns outros veja [griffe](https://mkdocstrings.github.io/griffe/docstrings/) para saber mais.

## Setup

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