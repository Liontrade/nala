import os


class Config:
    SYMBOLS = os.getenv('SYMBOLS', 'AAPL,GOOG,MSFT,AMZN').split(',')
    PERIOD = os.getenv('PERIOD', '1y')
    INTERVAL = os.getenv('INTERVAL', '1d')
