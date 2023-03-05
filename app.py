import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='dailyexpense',
)

cursor = conexao.cursor()

data = "04-03-2023"
nome = "teste1"
valor = 112

# CREATE
#comando = f'insert into daily_expense(data, nome, valor) values("{data}","{nome}",{valor})'
#print(comando)
#cursor.execute(comando)
#conexao.commit()                # confirma alteracao no banco


# READ
#comando = "SELECT * FROM daily_expense"
#print(comando)
#cursor.execute(comando)
#resultado = cursor.fetchall()    # ler dados do banco
#print(resultado)


# UPDATE
#data = "04-04-2023"
#id = 2
#comando = f'update daily_expense set data = "{data}" where id = {id}'
#print(comando)
#cursor.execute(comando)
#conexao.commit() 


# DELETE
id = 2
comando = f'delete from daily_expense where id = {id}'
print(comando)
cursor.execute(comando)
conexao.commit() 

cursor.close()
conexao.close()