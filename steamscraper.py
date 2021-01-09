import requests
from bs4 import BeautifulSoup
import lxml
print("PLEASE READ!!!!\n"
      "The Steam user you're trying to scrape the data from MUST have all their steam profile futures. \n They must have atleast 1 video,workshop item,badges,friends,groups,reviews,artwork. This works on High Level steam users best as they are most likely to have them unlocked.If not,\n The program wil output their Steam data list and run a try/except block. \n")
link = input("Please enter the Steam User Profile:\n ")
results = requests.get(link)
src = results.content
soup = BeautifulSoup(src,'lxml')

profile_level = soup.find('span', class_='friendPlayerLevelNum').text
profile_name = soup.find('span',class_='actual_persona_name').text
profile_comments = soup.find('a', class_='commentthread_allcommentslink')

com_result = str(profile_comments.text)
com_result = com_result.replace('View',' ')
com_result = com_result.replace('all',' ')


profile_games = []
profile_alldata = []

for game in soup.find_all('div',class_='game_name'):
    profile_games.append(game.text)

for prof_data in soup.find_all('span',class_='profile_count_link_total'):
    result = str(prof_data.string)
    result = result.replace('\t', '')
    result = result.replace('\r', '')
    result = result.replace('\n', '')
    result = result.replace('None', 'Failed to Retrieve')
    profile_alldata.append(result)

print(f"Raw profile data incase any errors happen: {profile_alldata} \n")
print(f' Name: {profile_name}\n Level: {profile_level}\n Last Games Played: {profile_games}\n Profile Comments: {com_result.lstrip()}')

if soup.find('div',class_='profile_in_game_header'):
    print(soup.find('div',class_='profile_in_game_header').text, profile_games[0])

try:
    print(f'\nProfile Awards: {profile_alldata[0]}\n Badges: {profile_alldata[1]}\n Games: {profile_alldata[2]}\n Screenshots: {profile_alldata[4]}\n Videos: {profile_alldata[5]}\n Workshop Items: {profile_alldata[6]}\n Game Reviews: {profile_alldata[7]}\n Game Guides: {profile_alldata[8]}\n Artwork: {profile_alldata[9]}\n Groups Joined: {profile_alldata[10]}\n Friends: {profile_alldata[11]}')
except:
    print(f" \nCan't scrape reliable data due to insufficient Steam Profile futures, outputting raw data instead: {profile_alldata}")
