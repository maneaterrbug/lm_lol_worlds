from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://lol.fandom.com/wiki/{}/2019_Season/Summer_Season'

response = requests.get(url)
page = response.text

##soup = BeautifulSoup(page, "lxml")

##print(soup.find_all('tr', class_ = 'standings-upwithbye teamhighlight teamhighlighter').find_all('td'))

region = ['LCS','LEC','LPL','LCK','VCS']


col_lst_bo1 = ['standing', 'team', 'record', 'match_winrate', 'streak']
col_lst_bo3 = ['standing', 'team', 'record', 'match_winrate', 'game_record','game_winrate','game_spread','streak','region']
df_team_ranks = pd.DataFrame(columns = col_lst_bo3)

##add for year in range here

for reg in region:
	reg_url = url.format(reg)
	response = requests.get(reg_url)
	page = response.text
	soup = BeautifulSoup(page, "lxml")

	for table in soup.find_all('table', class_ = 'wikitable2 standings'):
		for tr in table.select('tr[class *= "standings"]'):
			idx = 0
			row_dict = {}

			for td in tr.find_all('td'):
				if reg in ['LCS','LEC']:        
				## and year != 2017:
					row_dict[col_lst_bo1[idx]] = td.text
				else:
					row_dict[col_lst_bo3[idx]] = td.text
				idx += 1

			row_dict['region'] = reg
			df_team_ranks = df_team_ranks.append(row_dict, ignore_index = True)




print(df_team_ranks)

## player scraping here

#-upwithbye teamhighlight teamhighlighter