import requests
import bs4

url = "https://www.cnbc.com/world/?region=world"

response = requests.get(url)

if response.status_code == 200:
	soup = bs4.BeautifulSoup(response.text, 'html.parser')

	with open("data/raw_data/web_data.html", 'w', encoding='utf-8') as file:
		file.write(soup.prettify())

	with open("data/raw_data/web_data.html", 'r', encoding='utf-8') as file:
		for _ in range(10):
			print(file.readline().strip())
