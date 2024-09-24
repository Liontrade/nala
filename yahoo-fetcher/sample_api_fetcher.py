# from flask import Flask, jsonify, request
# from fetcher import Fetcher
#
# app = Flask(__name__)
#
# @app.route('/historical_data', methods=['GET'])
# def get_historical_data():
#     ticker = request.args.get('ticker', default='AAPL', type=str)
#     period = request.args.get('period', default='1y', type=str)
#     interval = request.args.get('interval', default='1d', type=str)
#
#     fetcher = Fetcher(ticker)
#     data = fetcher.get_historical_data(period=period, interval=interval)
#
#     if data is not None:
#         # Konwersja indeksu (Timestamp) na string, aby uniknąć błędów
#         data.index = data.index.strftime('%Y-%m-%d')
#         return jsonify(data.to_dict(orient='index'))  # Przekazanie słownika z poprawnym formatem
#     else:
#         return jsonify({"error": "Unable to fetch historical data"}), 500
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, request
from fetcher import Fetcher

app = Flask(__name__)

@app.route('/historical_data', methods=['GET'])
def get_historical_data():
    # Możliwość podania wielu tickerów lub użycie domyślnej listy
    tickers = (request.args.getlist('tickers')  or ['AAPL', 'TSLA', 'GOOGL', 'MSFT', 'AMZN'])  # Możesz dodać więcej firm
    period = request.args.get('period', default='1y', type=str)
    interval = request.args.get('interval', default='1d', type=str)

    result = {}
    for ticker in tickers:
        fetcher = Fetcher(ticker)
        data = fetcher.get_historical_data(period=period, interval=interval)

        if data is not None:
            # Konwersja indeksu (Timestamp) na string, aby uniknąć błędów
            data.index = data.index.strftime('%Y-%m-%d')
            result[ticker] = data.to_dict(orient='index')
        else:
            result[ticker] = {"error": f"Unable to fetch historical data for {ticker}"}

    return jsonify(result)  # Zwrócenie danych dla wszystkich firm

if __name__ == '__main__':
    app.run(debug=True)