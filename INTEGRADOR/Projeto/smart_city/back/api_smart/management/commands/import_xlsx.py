import os
import pandas as pd
from django.core.management.base import BaseCommand
from api_smart.models import Ambientes, Sensor

class Command(BaseCommand):
    help = 'Importa dados dos arquivos Excel para Ambientes e Sensores'

    def handle(self, *args, **kwargs):
        base_path = os.path.join(os.getcwd(), 'api_smart', 'management', 'commands')

        # Importar Ambientes
        ambientes_path = os.path.join(base_path, 'Ambientes.xlsx')
        if os.path.exists(ambientes_path):
            df_ambientes = pd.read_excel(ambientes_path)
            self.stdout.write(f'Importando Ambientes - {len(df_ambientes)} registros...')
            for _, row in df_ambientes.iterrows():
                ambiente, created = Ambientes.objects.update_or_create(
                    sig=row['sig'],
                    defaults={
                        'descricao': row['descricao'],
                        'ni': row['ni'],
                        'responsavel': row['responsavel'],
                    }
                )
                action = "Criado" if created else "Atualizado"
                self.stdout.write(f'{action} Ambiente: {ambiente.sig}')
        else:
            self.stdout.write(self.style.ERROR(f'Arquivo Ambientes.xlsx não encontrado em {base_path}'))

        # Função genérica para importar sensores
        def importar_sensores(arquivo, tipo_sensor):
            path = os.path.join(base_path, arquivo)
            if os.path.exists(path):
                df = pd.read_excel(path)
                self.stdout.write(f'Importando sensores tipo {tipo_sensor} - {len(df)} registros...')
                for _, row in df.iterrows():
                    mac_address = row['mac_address']
                    unidade_medida = row['unidade_medida']
                    valor = str(row['valor'])
                    latitude = float(row['latitude'])
                    longitude = float(row['longitude'])
                    status = row.get('status', 'ativo')
                    timestamp = row['timestamp']

                    sensor, created = Sensor.objects.update_or_create(
                        mac_address=mac_address,
                        defaults={
                            'sensor': tipo_sensor,
                            'unidade_medida': unidade_medida,
                            'valor': valor,
                            'latitude': latitude,
                            'longitude': longitude,
                            'status': status,
                            'timestamp': timestamp,
                        }
                    )
                    action = "Criado" if created else "Atualizado"
                    self.stdout.write(f'{action} Sensor: {mac_address} ({tipo_sensor})')
            else:
                self.stdout.write(self.style.ERROR(f'Arquivo {arquivo} não encontrado em {base_path}'))

        # Importar sensores por tipo
        importar_sensores('umidade.xlsx', 'umidade')
        importar_sensores('temperatura.xlsx', 'temperatura')
        importar_sensores('luminosidade.xlsx', 'luminosidade')
        importar_sensores('contador.xlsx', 'contador')

        self.stdout.write(self.style.SUCCESS('Importação concluída!'))
