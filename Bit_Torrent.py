import libtorrent as lt
import time
import os
import requests

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


class BaixarTorrentPorMagnet():
    def __init__(self):
        self.sessao = lt.session()
        self.sessao.listen_on(6881, 6891)

    def usando_vpn(self):
        vpn = UsandoVpn()
        return vpn.verificando_vpn()
    
    def main(self, link_magnetico, destino='downloads', resume_path='resume.data'):
        print(f"[*] Iniciando sessão libtorrent...")

        # Carregar estado anterior, se existir
        if os.path.exists(resume_path):
            with open(resume_path, 'rb') as f:
                resume_data = f.read()
        else:
            resume_data = None

        parametros = lt.add_torrent_params()
        parametros.save_path = destino
        parametros.url = link_magnetico
        parametros.flags &= ~lt.add_torrent_params_flags_t.flag_paused
        parametros.flags |= lt.add_torrent_params_flags_t.flag_auto_managed
        parametros.flags |= lt.add_torrent_params_flags_t.flag_seed_mode
        
        if resume_data:
            parametros = lt.read_resume_data(resume_data)

        manipulador = self.sessao.add_torrent(parametros)

        print("[*] Aguardando metadata...")
        while not manipulador.has_metadata():
            time.sleep(1)

        print("[✓] Metadata carregada. Iniciando download...\n")
        
        try:
            while not manipulador.is_seed():
                status = manipulador.status()
                print(f"Progresso: {status.progress * 100:.2f}% | "
                    f"Baixando: {status.download_rate / 1000:.2f} kB/s | "
                    f"Peers: {status.num_peers}", end='\r')
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[!] Download pausado manualmente. Salvando estado...")
            estado = lt.write_resume_data_buf(manipulador)
            with open(resume_path, 'wb') as f:
                f.write(estado)
            print("[✓] Estado salvo. Você pode retomar o download mais tarde.")
            return

        print("\n[✓] Download completo!")
        print(f"Arquivos salvos em: {destino}")





    

if __name__ == '__main__':
    print("🔒 Verificando se VPN está ativa...")
    if not UsandoVpn().usando_vpn():
        print("⚠️  AVISO: Seu IP real está visível. Recomendado ativar VPN antes de prosseguir.")
        input("Pressione ENTER para continuar mesmo assim (não recomendado)...")

    magnet = input("Digite o link magnet do torrent: ").strip()
    baixar = BaixarTorrentPorMagnet()
    baixar.main(magnet)
