import sqlite3

def create_bd(nome_banco, nome_tabela):
    try:
        conexao = sqlite3.connect(nome_banco)

        cursor = conexao.cursor()
        try:
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {nome_tabela}
                    (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        nome TEXT NOT NULL,
                        idade INT NOT NULL
                    );
            ''')
            conexao.commit()

            cursor.execute(
                f'''
                    INSERT INTO {nome_tabela} (nome, idade)
                    VALUES ('Pedro', 18)
                '''
            )
            conexao.commit()

            cursor.execute(
                f'''
                    INSERT INTO {nome_tabela} (nome, idade)
                    VALUES ('Gabriel', 6)
                '''
            )
            conexao.commit()
        except:
            print("Erro ao criar a tabela")

        conexao.close()
    except:
        print("Erro ao criar o banco")

create_bd("tr2.db", "usuario")