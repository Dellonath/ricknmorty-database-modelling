import requests
import psycopg2

class EpisodeExtractor:
    def __init__(self, page):
        self.page = page
        self.data = requests.get(page).json()
        self.__conn = "host='localhost' dbname='ricknmorty' user='postgres' password='postgres'"

    def get_results(self):
        return self.data['results']

    def create_row(self, data):
        row = (   
            data['id'],                                           # the id of the episode
            data['name'] if data['name'] else 'unknown',          # the name of the episode
            data['air_date'] if data['air_date'] else 'unknown',  # the air date of the episode
            data['episode'] if data['episode'] else 'unknown'     # the code of the episode
        )

        return row                                    

    def insert_row(self, values_sql, query = 'INSERT INTO Episode VALUES (%s, %s, %s, %s);'):
        
        connection = psycopg2.connect(self.__conn)
        session = connection.cursor()
        session.execute(query, values_sql)
        connection.commit()
        session.close()
        connection.close()
