#imports
import urllib.request as urllib
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import re
import time
import csv

FIRST_PLAYER_ID = 5001
LAST_PLAYER_ID = 56249
CRAWLER_DELAY = 15 / 1000 # 15 ms

def scrape(output_csv_path, player_id=FIRST_PLAYER_ID, last_player_id=LAST_PLAYER_ID):
    success = 0
    start_time = time.time()
    with open(output_csv_path, "w+") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        while player_id <= last_player_id:
            this_loop_time = time.time()
            try:                
                url = 'http://www.espncricinfo.com/ci/content/player/{}.html'.format(player_id)
                soup = bs(urllib.urlopen(url).read(), "html.parser")                
                name = soup.head.title.get_text().split('|')[0]
                country = soup.find_all('p', class_="ciPlayerlhscountrytxt")[0].get_text()
                tables = soup.find_all('table', class_="engineTable")
                batting_and_fielding_rows = tables[0].find_all('tr')
                row_num = 1
                batting_and_fielding_dict = {}
                bowling_dict = {}
                for row in batting_and_fielding_rows:
                    if row_num == 1:
                        row_num += 1
                        continue
                    val = getValues([value.get_text() for value in row.find_all('td')])                    
                    batting_and_fielding_dict[val[0]] = val
                    row_num += 1
                
                bowling_rows = tables[1].find_all('tr')
                row_num = 1
                for row in bowling_rows:
                    if row_num == 1:
                        row_num += 1
                        continue
                    val = getValues([value.get_text() for value in row.find_all('td')])                    
                    bowling_dict[val[0]] = val
                    row_num += 1
                writer.writerow([name, country, batting_and_fielding_dict, bowling_dict])
                success += 1
            except:
                print(player_id, ", getting from: ", url, " failed")
                player_id += 1
                continue
            print(player_id, ", getting from: ", url, " required time: ", (time.time()-this_loop_time), "(s)")
            player_id += 1
            time.sleep(CRAWLER_DELAY)
            if success % 50 == 0:
                csvfile.flush()
    with open("stat.txt", "w") as text_file:
        req = time.time() - start_time
        text_file.write("Total time = %d(s)\n" % req)
        text_file.write("Total success = %d(s)\n" % success)
        text_file.write("Average succeful scrape time = %d(s)\n" % (req/success))

def getValues(values):
    val =[value.replace('\t', '') for value in values]
    val = [value.replace(' ', '') for value in val]
    return [value.replace('\n','') for value in val]

def clearLastSpace(str):
    if str[-1] == ' ': return str[0: -1]
    else: return str
