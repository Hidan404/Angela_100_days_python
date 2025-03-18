import random


dados = [
    {
        "nome": "Instagram",
        "seguidores": 1000000,
        "descrição": "Rede social de fotos",
        "pais": "EUA"
    },
    {
        "nome": "Facebook",
        "seguidores": 2500000,
        "descrição": "Rede social",
        "pais": "EUA"
    },
    {
        "nome": "Twitter",
        "seguidores": 1500000,
        "descrição": "Rede social de microblogging",
        "pais": "EUA"
    },
    {
        "nome": "TikTok",
        "seguidores": 2000000,
        "descrição": "Rede social de vídeos curtos",
        "pais": "China"
    },
    {
        "nome": "YouTube",
        "seguidores": 3000000,
        "descrição": "Plataforma de vídeos",
        "pais": "EUA"
    },
    {
        "nome": "LinkedIn",
        "seguidores": 500000,
        "descrição": "Rede social profissional",
        "pais": "EUA"
    },
    {
        "nome": "Snapchat",
        "seguidores": 800000,
        "descrição": "Rede social de fotos e vídeos",
        "pais": "EUA"
    },
    {
        "nome": "Pinterest",
        "seguidores": 600000,
        "descrição": "Rede social de compartilhamento de imagens",
        "pais": "EUA"
    },
    {
        "nome": "Reddit",
        "seguidores": 700000,
        "descrição": "Rede social de fóruns",
        "pais": "EUA"
    },
    {
        "nome": "WhatsApp",
        "seguidores": 4000000,
        "descrição": "Aplicativo de mensagens",
        "pais": "EUA"
    },
    {
        "nome": "WeChat",
        "seguidores": 4500000,
        "descrição": "Aplicativo de mensagens",
        "pais": "China"
    },
    {
        "nome": "Telegram",
        "seguidores": 1200000,
        "descrição": "Aplicativo de mensagens",
        "pais": "Rússia"
    },
    {
        "nome": "Viber",
        "seguidores": 300000,
        "descrição": "Aplicativo de mensagens",
        "pais": "Japão"
    },
    {
        "nome": "Line",
        "seguidores": 500000,
        "descrição": "Aplicativo de mensagens",
        "pais": "Japão"
    },
    {
        "nome": "KakaoTalk",
        "seguidores": 400000,
        "descrição": "Aplicativo de mensagens",
        "pais": "Coreia do Sul"
    },
    {
        "nome": "Signal",
        "seguidores": 200000,
        "descrição": "Aplicativo de mensagens",
        "pais": "EUA"
    },
    {
        "nome": "Skype",
        "seguidores": 1000000,
        "descrição": "Aplicativo de chamadas de vídeo",
        "pais": "EUA"
    },
    {
        "nome": "Zoom",
        "seguidores": 2500000,
        "descrição": "Aplicativo de videoconferência",
        "pais": "EUA"
    },
    {
        "nome": "Microsoft Teams",
        "seguidores": 1500000,
        "descrição": "Aplicativo de colaboração",
        "pais": "EUA"
    },
    {
        "nome": "Slack",
        "seguidores": 800000,
        "descrição": "Aplicativo de colaboração",
        "pais": "EUA"
    },
    {
        "nome": "Discord",
        "seguidores": 1200000,
        "descrição": "Aplicativo de comunicação",
        "pais": "EUA"
    },
    {
        "nome": "Twitch",
        "seguidores": 900000,
        "descrição": "Plataforma de streaming",
        "pais": "EUA"
    },
    {
        "nome": "Mixer",
        "seguidores": 300000,
        "descrição": "Plataforma de streaming",
        "pais": "EUA"
    },
    {
        "nome": "Dailymotion",
        "seguidores": 400000,
        "descrição": "Plataforma de vídeos",
        "pais": "França"
    },
    {
        "nome": "Vimeo",
        "seguidores": 500000,
        "descrição": "Plataforma de vídeos",
        "pais": "EUA"
    },
    {
        "nome": "SoundCloud",
        "seguidores": 600000,
        "descrição": "Plataforma de música",
        "pais": "Alemanha"
    },
    {
        "nome": "Spotify",
        "seguidores": 3500000,
        "descrição": "Plataforma de música",
        "pais": "Suécia"
    },
    {
        "nome": "Apple Music",
        "seguidores": 3000000,
        "descrição": "Plataforma de música",
        "pais": "EUA"
    },
    {
        "nome": "Deezer",
        "seguidores": 700000,
        "descrição": "Plataforma de música",
        "pais": "França"
    },
    {
        "nome": "Tidal",
        "seguidores": 400000,
        "descrição": "Plataforma de música",
        "pais": "EUA"
    },
    {
        "nome": "Pandora",
        "seguidores": 500000,
        "descrição": "Plataforma de música",
        "pais": "EUA"
    },
    {
        "nome": "Shazam",
        "seguidores": 600000,
        "descrição": "Aplicativo de identificação de música",
        "pais": "EUA"
    },
    {
        "nome": "Google Play Music",
        "seguidores": 2000000,
        "descrição": "Plataforma de música",
        "pais": "EUA"
    },
    {
        "nome": "Amazon Music",
        "seguidores": 2500000,
        "descrição": "Plataforma de música",
        "pais": "EUA"
    },
    {
        "nome": "iTunes",
        "seguidores": 3000000,
        "descrição": "Plataforma de música",
        "pais": "EUA"
    },
    {
        "nome": "SoundHound",
        "seguidores": 400000,
        "descrição": "Aplicativo de identificação de música",
        "pais": "EUA"
    },
    {
        "nome": "Anghami",
        "seguidores": 500000,
        "descrição": "Plataforma de música",
        "pais": "Líbano"
    },
    {
        "nome": "Saavn",
        "seguidores": 600000,
        "descrição": "Plataforma de música",
        "pais": "Índia"
    },
    {
        "nome": "Wynk",
        "seguidores": 700000,
        "descrição": "Plataforma de música",
        "pais": "Índia"
    },
    {
        "nome": "Gaana",
        "seguidores": 800000,
        "descrição": "Plataforma de música",
        "pais": "Índia"
    },
    {
        "nome": "JioSaavn",
        "seguidores": 900000,
        "descrição": "Plataforma de música",
        "pais": "Índia"
    },
    {
        "nome": "Hungama",
        "seguidores": 1000000,
        "descrição": "Plataforma de música",
        "pais": "Índia"
    },
    {
        "nome": "QQ Music",
        "seguidores": 2000000,
        "descrição": "Plataforma de música",
        "pais": "China"
    },
    {
        "nome": "KuGou",
        "seguidores": 2500000,
        "descrição": "Plataforma de música",
        "pais": "China"
    },
    {
        "nome": "KuWo",
        "seguidores": 3000000,
        "descrição": "Plataforma de música",
        "pais": "China"
    },
    {
        "nome": "NetEase Music",
        "seguidores": 3500000,
        "descrição": "Plataforma de música",
        "pais": "China"
    },
    {
        "nome": "Yandex Music",
        "seguidores": 400000,
        "descrição": "Plataforma de música",
        "pais": "Rússia"
    },
    {
        "nome": "VK Music",
        "seguidores": 500000,
        "descrição": "Plataforma de música",
        "pais": "Rússia"
    },
    {
        "nome": "Boomplay",
        "seguidores": 600000,
        "descrição": "Plataforma de música",
        "pais": "Nigéria"
    },
    {
        "nome": "Audiomack",
        "seguidores": 700000,
        "descrição": "Plataforma de música",
        "pais": "EUA"
    },
    {
        "nome": "Mixcloud",
        "seguidores": 800000,
        "descrição": "Plataforma de música",
        "pais": "Reino Unido"
    }
]


def sortear_dois_paises():
    random.seed()
    paises = random.sample(dados, 2)
    pais1, pais2 = paises
    print(f"A - O país {pais1['pais']} rede social {pais1["nome"]} tem mais seguidores.")
    print(f"B - O país {pais2['pais']} ede social {pais2["nome"]} tem menos seguidores.")
    return pais1, pais2
    



def jogar_novamente():
    jogar_novamente = input("Deseja jogar novamente [S] ou [N]: ").lower().strip()
    if jogar_novamente == "s":
        comparar_seguidores()
    else:
        print("Obrigado por jogar!")
    
def comparar_seguidores():
    score = 0

    while True:
        pais1, pais2 = sortear_dois_paises()

        escolha = input("responda qual tem mais seguidores [A] ou [B]: ").lower().strip()
        if escolha not in ["a", "b"]:
            print("Escolha uma opção válida.")
            continue
        
        
        if escolha == "a":
            if pais1["seguidores"] > pais2["seguidores"]:
                print("Você acertou!")
                score += 1
            else:
                print(f"Você errou! seu score é {score}")
                jogar_novamente()
                break
        else:
            if pais2["seguidores"] > pais1["seguidores"]:
                print("Você acertou!")
                score += 1
            else:
                print(f"Você errou! seu score é {score}")
                jogar_novamente()
                break

        print(f"Seu score é {score}")
        


comparar_seguidores()
                
    