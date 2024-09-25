from flask import Flask, jsonify, request
from fetcher import Fetcher
import json
import os
import pandas as pd

app = Flask(__name__)


def load_symbols_from_json():
    with open('symbol-scrapper/symbols.json', 'r') as f:
        return json.load(f)


def format_symbol_for_yahoo(symbol):
    return symbol.replace('.', '-')


@app.route('/historical_data', methods=['GET'])
def get_historical_data():
    if os.path.exists('symbol-scrapper/symbols.json'):
        tickers = load_symbols_from_json()
    else:
        tickers = ['AAPL', 'TSLA', 'GOOGL', 'MSFT', 'AMZN']

    tickers = request.args.getlist('tickers') or tickers
    period = request.args.get('period', default='1mo', type=str)
    interval = request.args.get('interval', default='1d', type=str)

    result = {}
    for ticker in tickers:
        formatted_ticker = format_symbol_for_yahoo(ticker)
        fetcher = Fetcher(formatted_ticker)
        data = fetcher.get_historical_data(period=period, interval=interval)

        if data is not None:
            if not pd.api.types.is_datetime64_any_dtype(data.index):
                data.index = pd.to_datetime(data.index)

            data.index = data.index.strftime('%Y-%m-%d')
            result[ticker] = data.to_dict(orient='index')
        else:
            result[ticker] = {"error": f"Unable to fetch historical data for {ticker}"}

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
