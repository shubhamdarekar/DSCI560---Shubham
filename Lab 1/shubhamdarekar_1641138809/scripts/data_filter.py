import bs4
import csv

print("Reading HTML file...")
with open("data/raw_data/web_data.html", 'r', encoding='utf-8') as file:
    raw_contents = file.read()

print("Parsing HTML content...")
soup = bs4.BeautifulSoup(raw_contents, 'html.parser')


def extract_market_data(soup):
    print("Extracting market data...")
    market_data = []
    market_cards = soup.select('.MarketCard-container')
    for card in market_cards:
        card_details = {}
        
        card_details['marketCard_symbol'] = card.select_one('.MarketCard-symbol').get_text().strip()
        card_details['marketCard_stockPosition'] = card.select_one('.MarketCard-stockPosition').get_text().strip()
        card_details['marketCard-changePct'] = card.select_one('.MarketCard-changesPct').get_text().strip()
        market_data.append(card_details)
        
    print("Market data extraction complete.")
    return market_data


def extract_latest_news(soup):
    print("Extracting latest news...")
    news_data = []
    news_cards = soup.select('.LatestNews-headlineWrapper')
    for card in news_cards:
        card_details = {}
        
        card_details['title'] = card.select_one('.LatestNews-headline').get_text().strip()
        card_details['link'] = card.select_one('.LatestNews-headline')['href']
        card_details['LatestNews-timestamp'] = card.select_one('.LatestNews-timestamp').get_text().strip()
        news_data.append(card_details)
    
    print("Latest news extraction complete.")
    return news_data

def convert_to_csv(data, filename):
    print(f"Converting data to CSV: {filename}...")
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"CSV created: {filename}")


market_data = extract_market_data(soup)
news_data = extract_latest_news(soup)

convert_to_csv(market_data, 'data/processed_data/market_data.csv')
convert_to_csv(news_data, 'data/processed_data/news_data.csv')