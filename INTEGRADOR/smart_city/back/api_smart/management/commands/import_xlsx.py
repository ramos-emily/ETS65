import os
import pandas as pd
from django.core.management.base import BaseCommand
from api_smart.models import Ambientes, Sensor

class Command(BaseCommand):
    help = 'Importa dados dos arquivos Excel para Ambientes e Sensores'

    def handle(self, *args, **kwargs):
        caminho_base = os.path.join(os.getcwd(), 'api_smart', 'management', 'commands')

        caminho_ambientes = os.path.join(caminho_base, 'Ambientes.xlsx')
        if os.path.exists(caminho_ambientes):
            dados_ambientes = pd.read_excel(caminho_ambientes)
            self.stdout.write(f'Importando Ambientes - {len(dados_ambientes)} registros...')
            for _, linha in dados_ambientes.iterrows():
                ambiente, criado = Ambientes.objects.update_or_create(
                    sig=linha['sig'],
                    defaults={
                        'descricao': linha['descricao'],
                        'ni': linha['ni'],
                        'responsavel': linha['responsavel'],
                    }
                )
                acao = "Criado" if criado else "Atualizado"
                self.stdout.write(f'{acao} Ambiente: {ambiente.sig}')
        else:
            self.stdout.write(self.style.ERROR(f'Arquivo Ambientes.xlsx não encontrado em {caminho_base}'))

        def importar_sensores(nome_arquivo, tipo_sensor):
            caminho = os.path.join(caminho_base, nome_arquivo)
            if os.path.exists(caminho):
                dados = pd.read_excel(caminho)
                self.stdout.write(f'Importando sensores tipo {tipo_sensor} - {len(dados)} registros...')
                for _, linha in dados.iterrows():
                    endereco_mac = linha['mac_address']
                    unidade = linha['unidade_medida']
                    valor = str(linha['valor'])
                    latitude = float(linha['latitude'])
                    longitude = float(linha['longitude'])
                    status = linha.get('status', 'ativo')
                    timestamp = linha['timestamp']

                    sensor, criado = Sensor.objects.update_or_create(
                        mac_address=endereco_mac,
                        defaults={
                            'sensor': tipo_sensor,
                            'unidade_medida': unidade,
                            'valor': valor,
                            'latitude': latitude,
                            'longitude': longitude,
                            'status': status,
                            'timestamp': timestamp,
                        }
                    )
                    acao = "Criado" if criado else "Atualizado"
                    self.stdout.write(f'{acao} Sensor: {endereco_mac} ({tipo_sensor})')
            else:
                self.stdout.write(self.style.ERROR(f'Arquivo {nome_arquivo} não encontrado em {caminho_base}'))

        importar_sensores('umidade.xlsx', 'umidade')
        importar_sensores('temperatura.xlsx', 'temperatura')
        importar_sensores('luminosidade.xlsx', 'luminosidade')
        importar_sensores('contador.xlsx', 'contador')

        self.stdout.write(self.style.SUCCESS('Importação concluída!'))
