import serial
import serial.tools.list_ports

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
    port_index = int(input("Escolha o número da porta serial que você deseja usar: ")) - 1
    port = available_ports[port_index]

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

        # Dados para enviar
        data = 'Hello, Serial Port!'

        # Escreve dados na porta serial
        ser.write(data.encode())  # Encode a string para bytes
        print(f"Dados enviados: {data}")

        # Fecha a porta serial
        ser.close()
        print("Porta serial fechada.")
    except serial.SerialException as e:
        print(f"Erro ao abrir a porta serial: {e}")
    except ValueError as e:
        print(f"Valor inválido: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
