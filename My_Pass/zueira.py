import webbrowser
import random
import time  

random.seed()  # Definindo a semente para gerar números aleatórios

def main():

    websites = random.choice([
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.twitter.com",
        "https://www.instagram.com",
        "https://www.linkedin.com",
        "https://www.reddit.com",
        "https://www.youtube.com",
        "https://www.wikipedia.org",
        "https://www.github.com",
        "https://www.stackoverflow.com"
    ])
    print("Abrindo o site:", websites)

    n = 0
    while n < 10:
        n += 1
        webbrowser.open(websites)
        time.sleep(2)

main()        