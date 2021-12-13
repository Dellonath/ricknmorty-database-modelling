from location import LocationExtractor
from episode import EpisodeExtractor
from character import CharacterExtractor
from appear import AppearExtractor

if __name__ == "__main__":
    
    location_extractor = LocationExtractor('https://rickandmortyapi.com/api/location?page=1')
    num_registers = location_extractor.data['info']['count'] + 1
    while location_extractor.page:
        print(location_extractor.page)

        locations = location_extractor.get_results()
        for location in locations:
            row = location_extractor.create_row(location)
            location_extractor.insert_row(row)
        
        next_page = location_extractor.data['info']['next']
        if next_page is not None: location_extractor = LocationExtractor(next_page)
        else: break
        
    # inserto to null values in id_last_location
    location_extractor.insert_row([num_registers, 'unknown', 'unknown', 'unknown'])
    
    episode_extractor = EpisodeExtractor('https://rickandmortyapi.com/api/episode?page=1')
    while episode_extractor.page:
        print(episode_extractor.page)
        episodes = episode_extractor.get_results()
        for episode in episodes:
            row = episode_extractor.create_row(episode)
            episode_extractor.insert_row(row)
        
        next_page = episode_extractor.data['info']['next']
        if next_page is not None: episode_extractor = EpisodeExtractor(next_page)
        else: break
    
    character_extractor = CharacterExtractor('https://rickandmortyapi.com/api/character?page=1')
    appear_extractor = AppearExtractor()
    while character_extractor.page:
        print(character_extractor.page)
        characters = character_extractor.get_results()
        for character in characters:
            row = character_extractor.create_row(character)
            character_extractor.insert_row(row[:-1])
            for appearance in row[-1]:
                appear_extractor.insert_row(row[0], appearance)
        
        next_page = character_extractor.data['info']['next']
        if next_page is not None: character_extractor = CharacterExtractor(next_page)
        else: break
