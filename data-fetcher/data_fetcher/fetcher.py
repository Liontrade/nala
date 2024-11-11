import yfinance as yf
from utils.logger import logger


def fetch(symbol, period='1y', interval='1d'):
    """Fetch historical stock data for a given symbol."""
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period=period, interval=interval)
        logger.info(f'Fetched data for {symbol}')
        return data
    except Exception:
        logger.error(f'Failed to fetch data for {symbol}')
        raise


def fetch_multiple(symbols, period='1y', interval='1d'):
    """Fetch historical stock data for multiple symbols."""
    try:
        data = {}
        for symbol in symbols:
            data[symbol] = fetch(symbol, period, interval)
            logger.info(f'Fetched data for {symbol}')
        return data
    except Exception:
        logger.error(f'Failed to fetch data for {symbols}')
        raise
