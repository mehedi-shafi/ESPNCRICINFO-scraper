import cricscraper as scrapper
import structure

# Test script to download first 5 players' 
# data and structure them

if __name__ == '__main__':
    from time import time
    start_time = time()
    scrapper.scrape('test.csv', scrapper.FIRST_PLAYER_ID, scrapper.FIRST_PLAYER_ID+5)
    structure.structure_data('test.csv', 'test_structure.csv')
    duration = time() - start_time
    print('Required time: {}'.format(duration))