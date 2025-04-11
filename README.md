# Consulta de Filmes Indicados ao Oscar (2010–2015)

Este script em Python permite consultar filmes indicados ao Oscar entre os anos de 2010 e 2015, utilizando dados extraídos dinamicamente do site [scrapethissite.com](https://www.scrapethissite.com/). O usuário informa o ano desejado, e o programa retorna uma lista com o título do filme, número de nomeações e prêmios recebidos. Caso um ano fora do intervalo válido seja inserido, o script emite um aviso.

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- [Requests](https://pypi.org/project/requests/): Para fazer requisições HTTP à API do site.

##  Como Executar

1. Certifique-se de ter o Python instalado na sua máquina.
2. Instale a biblioteca `requests` (caso ainda não tenha):

```bash
pip install requests
```

## 📋 Exemplo de Uso
```bash
Qual ano deseja pesquisar? (2010 - 2015) 2013
Título: 12 Years a Slave                        Nomeações:  9   Prêmios:  3
Título: American Hustle                         Nomeações: 10   Prêmios:  0
Título: Gravity                                 Nomeações: 10   Prêmios:  7
...
```
## ❗ Observações
O script depende da estrutura da resposta da API externa, então pode parar de funcionar se o site modificar o formato dos dados.