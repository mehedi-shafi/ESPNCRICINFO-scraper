import cricscraper as scrapper
import structure
from datetime import datetime

# will crawl and scrape through all player 
# profiles. Run this to update entire dataset

if __name__ == '__main__':
    today_date = datetime.now().strftime("%d-%m-%Y")
    export_file_name = 'player_data_raw_{}.csv'.format(today_date)
    export_structured_file_name = 'player_data_final_{}.csv'.format(today_date)
    scrapper.scrape(export_file_name, scrapper.FIRST_PLAYER_ID, scrapper.LAST_PLAYER_ID)
    structure.structure_data(export_file_name, export_structured_file_name)