# 💌 Projeto de Envio de E-mails Seguros com Python

Este projeto foi desenvolvido como parte do desafio **100 Days of Python**, com o objetivo de automatizar o envio de e-mails personalizados, utilizando criptografia para proteger a senha do remetente.

## 📋 Funcionalidades

- Lê o corpo da mensagem de um arquivo `.txt`.
- Insere a data atual dinamicamente.
- Envia e-mails em datas específicas (segunda-feira).
- Criptografa a senha com `cryptography.fernet` e a armazena em um arquivo seguro.
- Realiza a autenticação SMTP com segurança.

## 🔐 Segurança implementada

- **Chave de criptografia (`chave.key`)** gerada com `Fernet`.
- **Senha do e-mail criptografada (`senha.bin`)**.
- A senha é **descriptografada apenas no momento da execução**.

## 🛠️ Tecnologias usadas

- Python 3.13+
- `smtplib` (biblioteca padrão para envio de e-mails)
- `datetime` (datas e horários)
- `cryptography.fernet` (criptografia de senha)
- `venv` para ambiente virtual



## 🔁 Fluxo do programa

1. `main.py` é executado.
2. Verifica o dia da semana (só envia o e-mail na segunda-feira).
3. Lê o corpo do e-mail do arquivo `msg_email.txt`.
4. Lê e descriptografa a senha do arquivo `senha.bin` usando `chave.key`.
5. Conecta ao servidor SMTP do Gmail e envia o e-mail.


