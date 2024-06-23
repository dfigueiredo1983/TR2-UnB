import serial

porta_serial = 'COM3'
baud_rate = 9600

instance_serial = serial.Serial(porta_serial, baud_rate)

try:
    while True:
        if instance_serial.in_waiting > 0:
            # lê uma linha de dados
            linha = instance_serial.readline().decode('utf-8').rstrip()
            print(linha)
except KeyboardInterrupt:
    print("Encerrando a leitura da porta serial")
finally:
    instance_serial.close()