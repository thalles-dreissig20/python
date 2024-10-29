import psutil

def obter_informacoes_do_sistema():
    cpu_percent = psutil.cpu_percent(interval=1)

    memoria = psutil.virtual_memory()

    disco = psutil.disk_usage('/')

    return {
        'CPU_percent': cpu_percent,
        'Memoria': {
            'Total': memoria.total,
            'Disponivel': memoria.available,
            'Percentual': memoria.percent
        },
        'Disco': {
            'Total': disco.total,
            'Usado': disco.used,
            'Livre': disco.free,
            'Percentual': disco.percent
        }
    }

informacoes = obter_informacoes_do_sistema()
print(informacoes)
