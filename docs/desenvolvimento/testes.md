<!--
 Copyright (c) 2023 Rafael F.M. & Reinaldo
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

# Testes

Os testes da aplicação foram realizados através do [pytest](https://docs.pytest.org/) e os seguintes módulos auxiliares:

* [pytest-httpserver](https://github.com/csernazs/pytest-httpserver): Um módulo para simulação de um *HTTP endpoint*. Consulte a [documentação](https://pytest-httpserver.readthedocs.io/en/latest/index.html) para mais detalhes.
* [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio): Um módulo que oferece suporte a funções `assíncronas`.

## Instalando dependências

Para instalar as dependências necessárias, execute o seguinte comando no terminal:

```bash
pip install -r tests/requirements.txt
```

## Executando os testes

Siga os passos abaixo para executar a bateria de testes:

1. Certifique-se de que todas as [requisitos foram instalados](./setup.md#instalando-dependencias).
2. Execute o seguinte comando:
```bash
pytest .\tests\ 
```
Isso garantirá que todos os aspectos críticos da aplicação foram testados de maneira abrangente.
