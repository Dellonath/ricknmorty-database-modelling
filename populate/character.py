import requests
import psycopg2

class CharacterExtractor:
    def __init__(self, page):
        self.page = page
        self.data = requests.get(page).json()
        self.__conn = "host='localhost' dbname='ricknmorty' user='postgres' password='postgres'"

    def get_results(self):
        return self.data['results']

    def create_row(self, data):
        row = (
            data['id'],                                         # the id of the character
            data['name'] if data['name'] else 'unknown',        # the name of the character
            data['status'] if data['status']  else 'unknown',   # the status of the character ('Alive', 'Dead' or 'unknown')
            data['species'] if data['species']  else 'unknown', # the species of the character  
            data['type'] if data['type']  else 'unknown',       # the type or subspecies of the character
            data['gender'] if data['gender']  else 'unknown',   # the gender of the character ('Female', 'Male', 'Genderless' or 'unknown')
            int(data['origin']['url'].split('/')[-1]) if data['origin']['url'].split('/')[-1]  else 127,       # the name and link to the character's origin location
            int(data['location']['url'].split('/')[-1]) if data['location']['url'].split('/')[-1]  else 127,   # name and link to the character's last known location endpoint
            [int(epId.split('/')[-1]) for epId in data['episode']]   # list of episodes in which this character appeared
        )

        return row                                    

    def insert_row(self, values_sql, query = 'INSERT INTO Character VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'):

        connection = psycopg2.connect(self.__conn)
        session = connection.cursor()
        session.execute(query, values_sql)
        connection.commit()
        session.close()
        connection.close()
