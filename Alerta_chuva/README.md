# 🌦️ AlertaClima5D - Aplicativo de Previsão do Tempo com Notificações

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Aplicativo Python que fornece alertas meteorológicos inteligentes com integração ao Telegram e notificações desktop para Linux.

![Demonstração do AlertaClima5D](demo.gif) <!-- Adicione um gif de demonstração posteriormente -->

## ✨ Funcionalidades Principais

- ⏰ Previsão horária estratégica (09h, 15h, 21h)
- 🌍 Suporte a qualquer localização global
- 📊 Consolidação de dados meteorológicos em JSON
- 🔔 Sistema dual de notificações:
  - 💻 Notificações desktop nativas (Linux)
  - 📲 Alertas via Telegram
- 🎨 Visualização intuitiva com emojis descritivos
- 🤖 Integração contínua com APIs meteorológicas

## 🛠️ Tecnologias Utilizadas

| Tecnologia               | Descrição                                  |
|--------------------------|-------------------------------------------|
| Python 3.10+             | Linguagem principal                       |
| OpenWeather API          | Dados meteorológicos em tempo real        |
| Telegram Bot API         | Comunicação com mensageiro                |
| JSON                     | Armazenamento local de dados              |
| notify-send              | Notificações desktop no Linux             |
| Requests                 | Comunicação HTTP com APIs                 |

## 📁 Estrutura do Projeto

```bash
AlertaClima5D/
├── app.py                 # Ponto de entrada principal
├── dados.py               # Lógica de coleta de dados da API
├── salvar_dados_json.py   # Persistência de dados local
├── icones_descricao.py    # Mapeamento de condições climáticas para emojis
├── enviar_msg_telegram.py # Integração com Telegram
├── requirements.txt       # Dependências do projeto
└── dados_clima.json       # Dados meteorológicos persistidos
