import libtorrent as lt
import time
import os
import requests
from pathlib import Path
from tkinter.filedialog import askopenfilename
from tkinter import Tk

class UsandoVpn():
    def __init__(self):
        self.ip = ''
        self.org = "" 
        self.location = ""

    def verificando_vpn(self):
        try:
            ip_info = requests.get('https://ipinfo.io').json()
            self.ip = ip_info.get('ip', '')
            self.org = ip_info.get('org', '')
            self.location = ip_info.get('country', '')
            print(f"[*] IP Detectado: {self.ip} ({self.org}, {self.location})")
            if "VPN" in self.org.upper() or "PRIVATE" in self.org.upper():
                return True
            return False
        except:
            return False


class BaixarTorrentPorMagnet:
    def __init__(self):
        # Sessão moderna com configuração segura
        self.sessao = lt.session()
        self.sessao.listen_on(6881, 6891)


    def usando_vpn(self):
        vpn = UsandoVpn()
        return vpn.verificando_vpn()

    def main(self, link_magnetico, destino='downloads', resume_path='resume.data'):
        print(f"[*] Iniciando sessão libtorrent com magnet link...")

        if not link_magnetico.startswith("magnet:?xt="):
            print("❌ Link magnet inválido.")
            return
        

        parametros = lt.parse_magnet_uri(link_magnetico)
        parametros.save_path = destino

        manipulador = self.sessao.add_torrent(parametros)
        self._baixar(manipulador, resume_path)

    def main_via_torrent_file(self, caminho_torrent, destino='downloads', resume_path='resume.data'):
        print(f"[*] Iniciando sessão libtorrent com arquivo .torrent...")

        info = lt.torrent_info(str(caminho_torrent))
        parametros = lt.add_torrent_params()
        parametros.ti = info
        parametros.save_path = destino

        manipulador = self.sessao.add_torrent(parametros)
        self._baixar(manipulador, resume_path)

    def _baixar(self, manipulador, resume_path):
        print("[*] Aguardando metadata...")
        while not manipulador.has_metadata():
            time.sleep(1)

        print("[✓] Metadata carregada. Iniciando download...\n")
        try:
            while not manipulador.is_seed():
                status = manipulador.status()
                print(f"\rProgresso: {status.progress * 100:.2f}% | "
                      f"Taxa: {status.download_rate / 1000:.2f} kB/s | "
                      f"Peers: {status.num_peers}", end='', flush=True)
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[!] Download pausado. Salvando estado...")
            estado = lt.write_resume_data_buf(manipulador)
            with open(resume_path, 'wb') as f:
                f.write(estado)
            print("[✓] Estado salvo para retomada.")
            return

        print("\n[✓] Download completo!")
        print(f"Arquivos salvos em: {manipulador.save_path()}")


    

if __name__ == '__main__':
    print("🔒 Verificando se VPN está ativa...")
    vpn = UsandoVpn()
    if not vpn.verificando_vpn():
        print("⚠️  AVISO: Seu IP real está visível. Recomendado ativar VPN antes de prosseguir.")
        input("Pressione ENTER para continuar mesmo assim (não recomendado)...")
    arquivo_torrent = input("Deseja carregar um arquivo torrent? S/N").strip()
    
    if arquivo_torrent == "S":
        Tk().withdraw()
        caminho = askopenfilename(title="Escolha o arquivo .torrent")

        if not caminho or not Path(caminho).exists():
            print("caminho invalido")
        else:
            print(f"Usando o caminho digitado {caminho}")
            baixar = BaixarTorrentPorMagnet()
            baixar.main_via_torrent_file(caminho)
    else:
        magnet = input("Digite o link magnet do torrent: ").strip()
        baixar = BaixarTorrentPorMagnet()
        baixar.main(magnet)
