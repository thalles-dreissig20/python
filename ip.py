import socket

def obter_endereco_ip():
    try:
        host_name = socket.gethostname()

        endereco_ip = socket.gethostbyname(host_name)

        return endereco_ip
    except socket.error as e:
        print(f"Erro ao obter o endereço IP: {e}")
        return None

endereco_ip = obter_endereco_ip()

if endereco_ip:
    print(f"Endereço IP do seu computador: {endereco_ip}")
else:
    print("Não foi possível obter o endereço IP.")