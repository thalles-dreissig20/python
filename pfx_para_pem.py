from OpenSSL import crypto

def converter_pfx_para_pem(caminho_pfx, senha_pfx, caminho_pem):
    with open(caminho_pfx, 'rb') as pfx_file:
        pfx_data = pfx_file.read()

    p12 = crypto.load_pkcs12(pfx_data, senha_pfx)

    with open(caminho_pem, 'w') as pem_file:
        pem_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey()).decode())
        pem_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate()).decode())
        for ca in p12.get_ca_certificates():
            pem_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, ca).decode())

caminho_pfx = 'arquivo.pfx'
senha_pfx = 'password'
caminho_pem = 'certificado.pem'

converter_pfx_para_pem(caminho_pfx, senha_pfx, caminho_pem)