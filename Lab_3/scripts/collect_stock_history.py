import yfinance as yf
from mysql_helper import *

# create_database_query = "CREATE DATABASE IF NOT EXISTS DSCI560_Stocks"

tables_queries = [
    """
    CREATE TABLE IF NOT EXISTS Stocks_analysis (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        ticker VARCHAR(10) NOT NULL,
        sector VARCHAR(100),
        industry VARCHAR(100),
        pe_ratio DECIMAL(10,2),
        pb_ratio DECIMAL(10,2),
        de_ratio DECIMAL(10,2),
        roe DECIMAL(10,2),
        eps DECIMAL(10,2),
        dividend_yield DECIMAL(10,2)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS stock_history (
        id INT PRIMARY KEY AUTO_INCREMENT,
        stock_id INT NOT NULL,
        collected_interval VARCHAR(10),
        date DATE NOT NULL,
        open_price DECIMAL(10,2),
        high_price DECIMAL(10,2),
        low_price DECIMAL(10,2),
        close_price DECIMAL(10,2),
        volume BIGINT,
        dividend_amount DECIMAL(10,2),
        stock_split DECIMAL(10,2),
        insertion_time DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (stock_id) REFERENCES Stocks_analysis(id)
    );
    """
]
"""period : str
            Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            Either Use period parameter or use start and end
        interval : str
            Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            Intraday data cannot extend last 60 days
"""
stocks_to_collect = [{'ticker':'AAPL','period':'1y','interval':'1d'}, {'ticker':'AAPL','period':'5d','interval':'1m'},
                     { 'ticker':'NVDA','period':'1y','interval':'1d'},{ 'ticker':'NVDA','period':'5d','interval':'1m'},
                     { 'ticker':'MSFT','period':'1y','interval':'1d'},{ 'ticker':'MSFT','period':'5d','interval':'1m'},
                     { 'ticker':'TSLA','period':'1y','interval':'1d'},{ 'ticker':'TSLA','period':'5d','interval':'1m'},
                     { 'ticker':'AMZN','period':'1y','interval':'1d'},{ 'ticker':'AMZN','period':'5d','interval':'1m'},
                     { 'ticker':'GOOGL','period':'1y','interval':'1d'},{ 'ticker':'GOOGL','period':'5d','interval':'1m'},
                     { 'ticker':'INTC','period':'1y','interval':'1d'},{ 'ticker':'INTC','period':'5d','interval':'1m'},
                     { 'ticker':'CSCO','period':'1y','interval':'1d'},{ 'ticker':'CSCO','period':'5d','interval':'1m'},
                     { 'ticker':'ADBE','period':'1y','interval':'1d'},{ 'ticker':'ADBE','period':'5d','interval':'1m'}]
# stocks_to_collect = ['AAPL','NVDA','MSFT','TSLA','AMZN','GOOGL','FB','INTC','CSCO','ADBE']

def initialize_database():
    connection = create_connection()
    cursor = connection.cursor()

    # cursor.execute(create_database_query)
    cursor.execute("USE DSCI560_Stocks")
    
    for query in tables_queries:
        cursor.execute(query)
    
    commit_and_close(connection)
    print("Database initialized successfully")
    
def save_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Stocks_analysis WHERE ticker = %s", [ticker])
    stock_in_db = cursor.fetchone()
    
    if not stock_in_db:
        cursor.execute("""
        INSERT INTO Stocks_analysis (name, ticker, sector, industry, pe_ratio, pb_ratio, de_ratio, roe, eps, dividend_yield)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, [info.get('shortName', 'Unknown'), ticker, info.get('sector', ''), info.get('industry', ''), 
              info.get('trailingPE', 0.0), info.get('priceToBook', 0.0), info.get('debtToEquity', 0.0), 
              info.get('returnOnEquity', 0.0), info.get('trailingEps', 0.0), info.get('dividendYield', 0.0)])
    else:
        cursor.execute("""
        UPDATE Stocks_analysis
        SET name = %s, sector = %s, industry = %s, pe_ratio = %s, pb_ratio = %s, de_ratio = %s, roe = %s, eps = %s, dividend_yield = %s
        WHERE ticker = %s
        """, [info.get('shortName', 'Unknown'), info.get('sector', ''), info.get('industry', ''),
              info.get('trailingPE', 0.0), info.get('priceToBook', 0.0), info.get('debtToEquity', 0.0),
              info.get('returnOnEquity', 0.0), info.get('trailingEps', 0.0), info.get('dividendYield', 0.0), ticker])
    commit_and_close(connection)
    return True
    
    
    
def collect_stock_history(ticker,period='1y',interval='1d'):
    save_stock_info(ticker)
    
    connection = create_connection()
    cursor = connection.cursor()
    
    stock = yf.Ticker(ticker)
    history = stock.history(period=period,interval=interval)
    
    cursor.execute("SELECT * FROM Stocks_analysis WHERE ticker = %s", [ticker])
    
    stock = cursor.fetchone()
    
    if not stock:
        return "Stock not found in database"
    stock_id = stock[0]
    
    
    
    for date, row in history.iterrows():
        cursor.execute("""
        INSERT INTO stock_history (stock_id,collected_interval,	date,	open_price,	high_price,	low_price,	close_price,	volume,	dividend_amount,	stock_split)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, [stock_id,interval, date, row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Dividends'], row['Stock Splits']])
    
    commit_and_close(connection)
    
    print("Saved_history of Stocks: ",ticker," Period: ",period," Interval: ",interval)
    
    
def save_table_to_csv(table_name,filename):
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    with open(f"{filename}.csv", 'w') as writer:
        writer.write(','.join([column[0] for column in cursor.description]) + '\n')
        for row in rows:
            writer.write(','.join([str(cell) for cell in row]) + '\n')
    
    commit_and_close(connection)
    print(f"Table {table_name} saved to {filename}.csv")
    
    

    
    
if __name__ == "__main__":
    # initialize_database()
    
    # for stock in stocks_to_collect:
    #     collect_stock_history(stock['ticker'], stock['period'], stock['interval'])
        
    save_table_to_csv("Stocks_analysis","Lab_3/raw_data/Stocks_analysis")
    save_table_to_csv("stock_history","Lab_3/raw_data/stock_history")
    

