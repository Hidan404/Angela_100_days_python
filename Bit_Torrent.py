# Importa a biblioteca libtorrent, que permite baixar arquivos via protocolo BitTorrent
import libtorrent as lt
import time  # Biblioteca para usar pausas (sleep) e controle de tempo

# Função principal que realiza o download a partir de um link magnet
def baixar_torrent_por_magnet(link_magnetico, destino='.'):
    print(f'[*] Iniciando download do magnet:\n{link_magnetico}\n')

    # Cria uma nova sessão do BitTorrent, que gerencia os downloads
    sessao = lt.session()

    # Define a faixa de portas a serem usadas para conexões de rede (pode ignorar o aviso de obsoleto)
    sessao.listen_on(6881, 6891)

    # Cria os parâmetros de configuração para o torrent
    parametros = lt.add_torrent_params()
    
    # Define o caminho onde os arquivos baixados serão salvos
    parametros.save_path = destino

    # Define o link magnet que será usado para iniciar o download
    parametros.url = link_magnetico

    # Remove a flag "pausado", para que o download comece imediatamente
    parametros.flags &= ~lt.add_torrent_params_flags_t.flag_paused

    # Ativa o gerenciamento automático do torrent pela sessão
    parametros.flags |= lt.add_torrent_params_flags_t.flag_auto_managed

    # Define o modo de seed (indica que os dados estão prontos para compartilhar — mesmo que não estejam ainda)
    parametros.flags |= lt.add_torrent_params_flags_t.flag_seed_mode

    # Adiciona o torrent à sessão com os parâmetros definidos acima
    manipulador = sessao.add_torrent(parametros)

    # Aguarda até que os metadados do torrent (informações como nomes de arquivos, tamanho etc.) sejam carregados
    print("[*] Baixando metadata...")
    while not manipulador.has_metadata():
        time.sleep(1)  # Espera 1 segundo
        print(".", end='', flush=True)  # Mostra progresso no terminal
    print("\n[✓] Metadata obtida.")

    # Começa o download dos arquivos após obter os metadados
    print("[*] Iniciando o download dos arquivos...")

    # Enquanto o torrent ainda não estiver completamente baixado
    while not manipulador.is_seed():
        status = manipulador.status()
        print(f"Progresso: {status.progress * 100:.2f}% | "
              f"Baixando: {status.download_rate / 1000:.2f} kB/s | "
              f"Peers conectados: {status.num_peers}", end='\r')
        time.sleep(1)

    # Quando o download estiver completo
    print("\n[✓] Download completo!")
    print(f"Arquivos salvos em: {destino}")

# Ponto de entrada principal do programa
if __name__ == '__main__':
    # Link magnet para o torrent que será baixado
    magnet = "magnet:?xt=urn:btih:aa9e9a825e7e4fdafda67e08dc516d96a0356472&dn=Crie aplicativos em Python com ChatGPT integrado via API!&tr=udp://tracker.openbittorrent.com:1337/announce&tr=udp://tracker.bittor.pw:1337/announce&tr=http://tracker.renfei.net:8080/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=http://tracker.opentrackr.org:1337/announce&tr=udp://open.stealth.si:80/announce&tr=udp://tracker.torrent.eu.org:451/announce&tr=udp://exodus.desync.com:6969/announce&tr=udp://open.free-tracker.ga:6969/announce&tr=http://www.torrentsnipe.info:2701/announce&tr=http://tracker.internetwarriors.net:1337/announce&tr=http://tracker.bittor.pw:1337/announce&tr=http://www.genesis-sp.org:2710/announce&tr=http://tracker.skyts.net:6969/announce&tr=udp://open.demonii.com:1337/announce&tr=udp://leet-tracker.moe:1337/announce&tr=http://p4p.arenabg.com:1337/announce"
    
    # Chama a função para iniciar o download
    baixar_torrent_por_magnet(magnet)
