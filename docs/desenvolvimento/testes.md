<!--
 Copyright (c) 2023 Rafael F.M. & Reinaldo
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

# Testes

Os testes da aplicação foram realizados através do [pytest](https://docs.pytest.org/) e os seguintes módulos auxiliares:

* [pytest-httpserver](https://github.com/csernazs/pytest-httpserver): Modulo para mockup de um *HTTP endpoint*, para mais informações visite a sua [documentação](https://pytest-httpserver.readthedocs.io/en/latest/index.html)
* [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio): Modulo para suporte à funções `assíncronas`.

## Executando os testes

Para executar a bateria de testes siga os seguintes passos:

1. Garanta que os [requisitos foram instalados](./setup.md#instalando-dependencias).
2. execute o comando:
```bash
pytest .\tests\ 
```
