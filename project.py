import serial
import serial.tools.list_ports
import time
import re

from datetime import datetime

import sqlite3

def create_dataBase(nome_banco, nome_tabela):
    try:
        conexao = sqlite3.connect(nome_banco)
        cursor = conexao.cursor()
        try:
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {nome_tabela} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        medida TEXT NOT NULL,
                        data TEXT NOT NULL,
                        hora TEXT NOT NULL
                    );
            ''')
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {nome_tabela} - {erro}")

        conexao.close()
    except:
        print(f"Erro ao criar o banco: '{nome_banco}'")


def list_serial_ports():
    """Lista todas as portas seriais disponíveis."""
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

def main():
    # Lista todas as portas seriais disponíveis
    available_ports = list_serial_ports()
    if not available_ports:
        print("Nenhuma porta serial encontrada.")
        return

    print("Portas seriais disponíveis:")
    for i, port in enumerate(available_ports, start=1):
        print(f"{i}: {port}")

    # Escolha a porta serial desejada
    port_index = int(input("Escolha o número da porta serial que você deseja usar: "))
    port = available_ports[port_index - 1]
    try:
        # Configuração da porta serial
        ser = serial.Serial(
            port=port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

        # Verifica se a porta serial está aberta
        if ser.isOpen():
            print(f"Porta serial {ser.port} aberta com sucesso.")
        else:
            print(f"Falha ao abrir a porta serial {ser.port}.")
            return

        nome_banco = "tr2.db"
        nome_tabela = "ultrasonic"

        create_dataBase(nome_banco, nome_tabela)
        conexao = sqlite3.connect(nome_banco)

        # Abre o arquivo para salvar os dados
        with open("dados_serial.txt", "a") as file:
            print("Gravando dados no arquivo 'dados_serial.txt'. Pressione Ctrl+C para parar.")

            # Loop infinito para ler dados da porta serial e salvar no arquivo
            while True:
                if ser.in_waiting > 0:
                    dados = ser.readline().decode('utf-8').strip()

                    if dados == "-1.00":
                        dados = "0.00"

                    print(f"Dados recebidos: {dados}")
                    data = datetime.now()
                    dia = data.strftime('%d/%m/%Y')
                    hora = data.strftime('%H:%M:%S')
                    print(f"Data atual: {dia}")
                    print(f"Hora atual: {hora}")

                    try:
                        cursor = conexao.cursor()
                        cursor.execute(f'INSERT INTO {nome_tabela} (medida, data, hora) VALUES ("{dados}", "{dia}", "{hora}")')
                        conexao.commit()
                    except Exception as erro:
                        print(f'Erro ao salvar no banco de dados. {erro}')

                    file.write(dados + " " + dia + " " + hora + "\n")
                    file.flush()  # Garante que os dados são gravados imediatamente no arquivo

    except serial.SerialException as e:
        print(f"Erro ao abrir a porta serial: {e}")
    except ValueError as e:
        print(f"Valor inválido: {e}")
    except KeyboardInterrupt:
        print("Leitura interrompida pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        ser.close()
        conexao.close()
        print("Porta serial fechada.")

if __name__ == "__main__":
    main()
