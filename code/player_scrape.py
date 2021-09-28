from bs4 import BeautifulSoup
import requests
import pandas as pd

url_player = 'https://lol.fandom.com/wiki/{0}/{1}_Season/Summer_Season/Player_Statistics'
region = ['LCS','LEC','LPL','LCK','VCS']



##for reg in region:
##reg_url = url_player.format(reg)
# response = requests.get(url_player)
# page = response.text
# soup = BeautifulSoup(page, "lxml")

col_lst_players = (['team','player','gp','w','l','wr','k','d','a','kda','cs','cs/m','g','g/m',
					'kpar','ks','gs','cp','champs','region','year'])
our_df = pd.DataFrame(columns = col_lst_players)

for year in range(2018,2021):
	if year > 2018:
		region = ['LCS','LEC','LPL','LCK','VCS']
	else:
		region = ['NA_LCS','EU_LCS','LPL','LCK','VCS']
	for reg in region: 
		url_player_reg = url_player.format(reg,year)
		print(url_player_reg)
		response = requests.get(url_player_reg)
		page = response.text
		soup = BeautifulSoup(page, "lxml")

		table = soup.find('table', class_ = "wikitable sortable spstats plainlinks hoverable-rows")
		tbody = table.find('tbody')
		trs = tbody.find_all('tr')[5:]
		#print(trs)
		for tr in trs:
			row_dict = {}
			idx = 0
			for td in tr.find_all('td'):
				if td.get('class') == ['spstats-team']:
					row_dict[col_lst_players[idx]] = td.find('a').get('title')
				else:
					row_dict[col_lst_players[idx]] = td.text
				idx+=1
			row_dict['region'] = reg
			row_dict['year'] = year
			our_df = our_df.append(row_dict, ignore_index = True)



print(our_df.info)

our_df.to_csv('../test_player_db.csv', index = False, index_label = False, header = False)
#CREATE TABLE player_stats (team TEXT, player TEXT, gp INTEGER, w INTEGER, l INTEGER, 
#wr TEXT, k INTEGER, d INTEGER, a INTEGER, kda FLOAT, cs INTEGER, csm FLOAT, g INTEGER, gm FLOAT, kpar TEXT, ks TEXT, gs TEXT, cp INTEGER, champs TEXT, region TEXT)