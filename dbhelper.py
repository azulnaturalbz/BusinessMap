import pymysql
import dbconfig


class DBHelper:

    def connect(self, database="business_map"):
        return pymysql.connect(host='localhost',
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT * FROM business_list;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO business_list (description) VALUES(%s);"
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM business_list;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()

    def add_business(self,bizname,bizaddr,usrtel,email,homepage,category,date,latitude,longitude,description):
        connection = self.connect()
        try:
            query = "INSERT INTO business_list (name_of_business,address,phone" \
                    ",email,url,category,in_date,latitude,longitude,description) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            with connection.cursor() as cursor:
                cursor.execute(query,(bizname, bizaddr, usrtel, email, homepage, category, date, latitude, longitude,
                                      description))
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

    def get_all_business(self):
        connection = self.connect()
        try:
            query = "SELECT name_of_business,address,phone,email,url,category,in_date,latitude,longitude,description FROM business_list"
            with connection.cursor() as cursor:
                cursor.execute(query)
            named_businesses = []
            for business in cursor:
                name_business = {
                    'bizname': business[1],
                    'bizaddr': business[2],
                    'usrtel': business[3],
                    'email': business[4],
                    'homepage': business[5],
                    'date': business[6],
                    'category': business[7],
                    'latitude': business[8],
                    'longitude': business[9],
                    'description': business[10]
                }
                named_businesses.append(name_business)
            return named_businesses
        finally:
            connection.close()


    #Bulding out just text submission to database table
    def get_all_inputs1(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM business_description;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_input1(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO business_description (description) VALUES(%s);"
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        finally:
            connection.close()

    def clear_all1(self):
        connection = self.connect()
        try:
            query = "DELETE FROM business_description;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()