import requests
import psycopg2

class LocationExtractor:
    def __init__(self, page):
        self.page = page
        self.data = requests.get(page).json()
        self.__conn = "host='localhost' dbname='ricknmorty' user='postgres' password='postgres'"

    def get_results(self):
        return self.data['results']

    def create_row(self, data):
        row = (
            data['id'],                                             # the id of the location
            data['name'] if data['name'] else 'unknown',            # the name of the location
            data['type'] if data['type'] else 'unknown',            # the type of the location
            data['dimension'] if data['dimension'] else 'unknown'   # the dimension in which the location is located
        )

        return row                                    

    def insert_row(self, values_sql, query = 'INSERT INTO Location VALUES (%s, %s, %s, %s);'):

        connection = psycopg2.connect(self.__conn)
        session = connection.cursor()
        session.execute(query, values_sql)
        connection.commit()
        session.close()
        connection.close()
