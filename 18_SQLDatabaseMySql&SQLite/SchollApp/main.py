import mysql.connector

def insert_product():
    connection = mysql.connector.connect(host="localhost", user = "root", password="12Plp***", database="node_app")
    cursor = connection.cursor()
    
    
    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
    values = ("SAmsung",1000,"1.jpg","deneme")
    
    cursor.execute(sql,values)
    try:
         connection.commit()
    except mysql.connector.Error as err:
        print("Hata :" , err)
    finally:
        connection.close()
        print("Baglanti Kapandi.")    
insert_product()