import pymysql
import dbconfig

connection = pymysql.connect(host='localhost', user=dbconfig.db_user, password=dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS business_map"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS business_map.business_list(
        id int NOT NULL AUTO_INCREMENT,
        latitude FLOAT(10,6),
        longitude FLOAT(10,6),
        date DATETIME,
        name_of_business VARCHAR(50),
        category VARCHAR(100),
        description VARCHAR(1000),
        update_at TIMESTAMP ,
        PRIMARY KEY (id)
        )"""
        cursor.execute(sql);
        connection.commit()
finally:
    connection.close()