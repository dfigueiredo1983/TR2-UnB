import serial
import serial.tools.list_ports

# Função para listar todas as portas seriais disponíveis
def listar_portas_seriais():
    portas = serial.tools.list_ports.comports()
    for porta in portas:
        print(f"{porta.device}: {porta.description}")

# Listar todas as portas seriais disponíveis
# print("Portas seriais disponíveis:")
# listar_portas_seriais()

listar_portas_seriais()

# Configurações da porta serial (substitua 'COM3' pela porta correta)
porta_serial = 'COM3'
baud_rate = 9600

try:
    ser = serial.Serial(porta_serial, baud_rate)
    print(f"Conectado à porta {porta_serial} com baud rate {baud_rate}")

    try:
        while True:
            if ser.in_waiting > 0:
                linha = ser.readline().decode('utf-8').rstrip()
                print(linha)
    except KeyboardInterrupt:
        print("Encerrando a leitura da porta serial.")
    finally:
        ser.close()
except serial.SerialException as e:
    print(f"Erro ao tentar acessar a porta serial {porta_serial}: {e}")
