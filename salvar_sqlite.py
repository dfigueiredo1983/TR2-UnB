import sqlite3

conn = sqlite3.connect('tr2.db')
cursor = conn.cursor()

cursor.execute("""INSERT INTO ultrasonic (medida, data, hora) VALUES ('54.0', '22/06/2024', '14:05')""")

conn.commit()

print('Dados inseridos com sucesso')
conn.close()