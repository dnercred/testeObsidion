import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='172.17.0.2',
                              database='ListasBubble')
cnx.close()



sql="""

CREATE TABLE ListasgeralViverBemdenner(
nome VARCHAR(250),
telefone VARCHAR(15)

);"""


cnx.execute(sql)
cnx.commit()