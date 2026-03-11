# Image Processing Orchestrator

## Sobre o Projeto

O **Image Processing Orchestrator** é a api principal do projeto no qual contém mais um microserviço que é responsável por processar imagens e retornar uma resposta com o resultado da operação além de um microserviço responsável por notificar o usuário.

Neste projeto é onde o usuário irá interagir com o sistema, enviando imagens para o serviço de processamento e recebendo respostas de sucesso ou falha.

## Comandos Básicos

Este projeto utiliza um `Makefile` para facilitar a execução de tarefas comuns. Abaixo estão os comandos disponíveis:

### Execução

```bash
make install-hooks  # Instala os hooks de pré-commit para garantir a qualidade do código
make test           # Executa os testes da aplicação
make run            # Inicia o servidor de desenvolvimento
make ruff           # Verifica o código com o linter Ruff
make fix            # Corrige problemas detectados pelo linter Ruff
make format         # Formata o código automaticamente com o Ruff
```

### Exemplo de Uso

Para iniciar o projeto, execute:

```bash
make install-hooks
make run
```

Para executar os testes:

```bash
make test
```

Para verificar e corrigir problemas no código:

```bash
make ruff
make fix
```

Consulte o `Makefile` para detalhes adicionais sobre cada comando.

## Arquitetura do Projeto

Este repositório contém um diagrama de arquitetura que ilustra a estrutura e o fluxo de dados do sistema.

[Arquitetura do Projeto](docs/arquitetura.png)
