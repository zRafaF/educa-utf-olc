<!--
 Copyright (c) 2023 Rafael F.M. & Reinaldo
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

# Desenvolvimento

Bem-vindo à página de desenvolvimento do EducaUTF OLC! Se você está interessado em contribuir para a aplicação, este é o ponto de partida perfeito. Aqui estão alguns recursos importantes para começar:

## Formatação

Para padronização da formatação foi utilizado o [black](https://github.com/psf/black).

## Executando

Antes de executar a aplicação garanta que o **ambiente de desenvolvimento** foi configurado corretamente, visite [desenvolvimento-setup](./setup.md) para saber mais.

Para iniciar a aplicação, execute o script ``main.py`` localizado no diretório ``src`` usando o seguinte comando:

``` sh
python src/python.py
```

Este comando iniciará a conexão com o backend do **EducaUTF** e criará um endpoint no endereço `127.0.0.1:8000`.

Além disso, você pode passar alguns **argumentos** opcionais para personalizar o comportamento da aplicação:

* `--pb_url`: Define a URL do backend da aplicação.
* `--host`: Define o endereço no qual a aplicação será servida.
* `--port`: Define a porta na qual a aplicação será servida.

```sh
python src/main.py --host=0.0.0.0 --port=3000 --pb_url=https://my_pb_backend/api
```

Certifique-se de ajustar os valores conforme necessário para atender às suas configurações específicas. Agora você está pronto para explorar a aplicação EducaUTF OLC localmente!
