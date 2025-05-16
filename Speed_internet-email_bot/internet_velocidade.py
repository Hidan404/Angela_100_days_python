import speedtest

def teste_interenet():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping

    return download_speed, upload_speed, ping

def formatar_resultados(download_speed, upload_speed, ping):
    download_speed = round(download_speed, 2)
    upload_speed = round(upload_speed, 2)
    ping = round(ping, 2)

    return f"Download: {download_speed} Mbps\nUpload: {upload_speed} Mbps\nPing: {ping} ms"