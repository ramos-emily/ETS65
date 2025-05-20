import os
import pandas as pd
from django.core.management.base import BaseCommand
from api_smart.models import Ambientes, Sensor

class Command(BaseCommand):
    help = 'Importa dados dos arquivos Excel para Ambientes e Sensores'

    def handle(self, *args, **kwargs):
        base_path = os.path.join(os.getcwd(), 'api_smart', 'management', 'commands')

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

        def importar_sensores(arquivo, tipo_sensor):
            path = os.path.join(base_path, arquivo)
            if os.path.exists(path):
                df = pd.read_excel(path)
                self.stdout.write(f'Importando sensores tipo {tipo_sensor} - {len(df)} registros...')
                for _, row in df.iterrows():
                    sensor_id = row.get('sensor_id') or row.get('Sensor_ID') or row.get('id')
                    mac_address = row.get('mac_address') or row.get('MAC_Address') or '00:00:00:00:00'
                    unidade_med = row.get('unidade_med') or row.get('unidade') or 'un'
                    valor = str(row.get('valor') or row.get('Valor') or '')
                    latitude = float(row.get('latitude') or 0.0)
                    longitude = float(row.get('longitude') or 0.0)
                    status = row.get('status') or 'ativo'

                    sensor, created = Sensor.objects.update_or_create(
                        sensor_id=sensor_id,
                        defaults={
                            'mac_address': mac_address,
                            'tipo_sensor': tipo_sensor,
                            'unidade_med': unidade_med,
                            'valor': valor,
                            'latitude': latitude,
                            'longitude': longitude,
                            'status': status,
                        }
                    )
                    action = "Criado" if created else "Atualizado"
                    self.stdout.write(f'{action} Sensor: {sensor.sensor_id} ({tipo_sensor})')
            else:
                self.stdout.write(self.style.ERROR(f'Arquivo {arquivo} não encontrado em {base_path}'))

        importar_sensores('contador.xlsx', 'contador')
        importar_sensores('luminosidade.xlsx', 'luminosidade')
        importar_sensores('temperatura.xlsx', 'temperatura')
        importar_sensores('umidade.xlsx', 'umidade')

        self.stdout.write(self.style.SUCCESS('Importação concluída!'))
