import requests

ano = int(input('Qual ano deseja pesquisar? (2010 - 2015) '))

if ano < 2010 or ano > 2015:
    print('Ano indisponivel, escolha entre 2010 e 2015')

else:

    url = f'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={ano}'

    response = requests.get(url)

    filmes = response.json()

    for filme in filmes:

        print(f'Título: {filme["title"]:<40} Nomeações: {filme["nominations"]:>3}   Prêmios: {filme["awards"]:>3}')
