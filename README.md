# Torneio de Futebol

Um pequeno sistema em Python que gerencia times, partidas e resultados de um torneio de futebol com tratamento de erros e logging.

## Funcionalidades

- Registro de times
- Criação de partidas
- Exibição da classificação e resultados
- Tratamento de erros (nome inválido, gols negativos, time inexistente)
- Logs em `erros.log`

## Executar localmente

```bash
python main.py
```

## Usar com Docker

```bash
docker build -t torneio-futebol .
docker run --rm torneio-futebol
```
