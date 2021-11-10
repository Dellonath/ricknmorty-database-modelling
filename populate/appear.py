import psycopg2
from character import CharacterExtractor

class AppearExtractor:
    def __init__(self):
        self.__conn = "host='localhost' dbname='ricknmorty' user='postgres' password='postgres'"
                    
    def insert_row(self, character_id, episode_id, query = 'INSERT INTO Appear VALUES (DEFAULT, %s, %s);'):

        connection = psycopg2.connect(self.__conn)
        session = connection.cursor()
        session.execute(query, [character_id, episode_id])
        connection.commit()
        session.close()
        connection.close()
