import ipaddress

def calcular_mascara_curinga(ip):
    try:
        # Se for um único IP, assume como /32
        if '/' not in ip:
            ip += '/32'
        
        # Converte a entrada em um objeto IPv4Network
        rede = ipaddress.IPv4Network(ip, strict=False)
        
        # Converte a máscara de sub-rede para um inteiro e depois para binário
        mascara_bin = f"{int(rede.netmask):032b}"
        
        # Inverte a máscara binária para obter a máscara curinga
        mascara_curinga_bin = ''.join('1' if bit == '0' else '0' for bit in mascara_bin)
        
        # Converte a máscara curinga binária para formato decimal
        mascara_curinga = '.'.join(str(int(mascara_curinga_bin[i:i+8], 2)) for i in range(0, 32, 8))
        
        return mascara_curinga
    
    except ValueError:
        return "Formato de IP inválido."

# Entrada do usuário
ip_ou_faixa = input("Digite um IP ou faixa de IP (ex: 192.168.1.0/24 ou 192.168.1.1): ")
mascara_curinga = calcular_mascara_curinga(ip_ou_faixa)
print(f"A máscara curinga para '{ip_ou_faixa}' é: {mascara_curinga}")
