import mysql.connector
def connectMysql(user,passwd,auth='mysql_native_password'):
    cnx = mysql.connector.connect(
        user=user,
        password=passwd,
        auth_plugin= auth,
        port = 3306
    )
    output = {}
    output['cnx'] = cnx
    output['user']=user
    output['pass']=passwd
    output['auth']=auth
    return output
def createDatabase(cnx1,database):
    cnx2 = mysql.connector.connect(
        user        =cnx1['user'],
        password    =cnx1['pass'],
        auth_plugin =cnx1['auth'],
        database    =database,
        port        = 3306
    )
    return cnx2

if __name__ == '__main__':
    import mysql.connector
    import cv2
    img = (cv2.imread('image/image.jpg'))
    # connect to mysql
    connect1= connectMysql('root','32991059N@t')
    cnx = connectMysql('root','32991059N@t')['cnx']
    # create database
    cursor = cnx.cursor()
    cursor.execute("SHOW DATABASES")

    database = "frame"
    for db in cursor:
        if database == db[0]:

            cnx = mysql.connector.connect(
                user=connect1['user'],
                password=connect1['pass'],
                auth_plugin=connect1['auth'],
                database='frame',
                port=3306
            )
            cursor = cnx.cursor()

    ##### create table
    cursor.execute("CREATE TABLE facerec (name VARCHAR(50), imageD BLOB, matchornot VARCHAR(50))")
    ###
    for db in cursor:
       print(db)





    with open("image/image.jpg", 'rb') as f:
        m = f.read()
    with open("recieve.jpg","wb") as fh:
        fh.write(m)

    cursor.execute("INSERT INTO facerec (name, imageD, imageDB) VALUES (%s,%s,%s)",("Tree",img,"match"))
