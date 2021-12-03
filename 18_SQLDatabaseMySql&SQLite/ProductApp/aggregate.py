import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="localhost", user = "root", password="12Plp***", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def insertProducts(list):
    connection = mysql.connector.connect(host="localhost", user = "root", password="12Plp***", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def getProducts():
    connection = mysql.connector.connect(host="localhost", user = "root", password="12Plp***", database="node_app")
    cursor = connection.cursor()

    cursor.execute("Select * From Products Order By name, price")

    try:
        result = cursor.fetchall()    
        for product in result:
            print(f'id: {product[0]} name: {product[1]} price: {product[2]}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')
    
def getProductById(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password="12Plp***", database="node_app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()    

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

def getProductInfo():
    connection = mysql.connector.connect(host="localhost", user = "root", password="12Plp***", database="node_app")
    cursor = connection.cursor()

    # sql = "Select COUNT(*) from Products" sayısını verir
    # sql = "Select AVG(Price) from Products" ortalamasını verir
    # sql = "Select SUM(Price) from Products" toplamını verir
    # sql = "Select MIN(Price) from Products" max degeri verir.
    # sql = "Select MAX(Price) from Products" min degeri verir.
    sql = "Select Name,Price from Products Where Price = (Select MAX(Price) from Products)"

    cursor.execute(sql)

    result = cursor.fetchone()    

    print(f'result: {result[0]} {result[1]}')


getProductInfo()