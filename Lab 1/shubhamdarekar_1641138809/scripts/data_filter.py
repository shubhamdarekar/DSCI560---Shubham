import bs4

with open("data/raw_data/web_data.html", 'r', encoding='utf-8') as file:
    raw_contents =  file.read()

soup = bs4.BeautifulSoup(raw_contents, 'html.parser')


def extract_market_data(soup):
    market_data = []
    market_cards = soup.select('.MarketCard-container')
    print("Extra:",market_cards)
    for card in market_cards:
        symbol = card['href'].split('/')[-1] if 'href' in card.attrs else 'N/A'
        stock_position = card.select_one('.MarketCard-row:nth-child(1)')
        change_pct = card.select_one('.MarketCard-row:nth-child(3)')

        stock_position_text = stock_position.text.strip() if stock_position else 'N/A'
        change_pct_text = change_pct.text.strip() if change_pct else 'N/A'

        market_data.append([symbol, stock_position_text, change_pct_text])
    return market_data

market_data = extract_market_data(soup)

print(market_data)