from injest_sod_positions import *


class Trades:
    def __init__(self, account_id, instrument_id, side, traded_quantity, traded_price):
        self.account_id = account_id
        self.instrument_id = instrument_id
        self.side = side
        self.traded_quantity = traded_quantity
        self.traded_price = traded_price


class TradeFileIngestion:
    def __init__(self, trade_file_path):
        self.trade_file_path = trade_file_path
        self.trades = []

    def ingest_trade_file(self):
        with open(self.trade_file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            trade_data = line.strip().split(',')
            account_id = int(trade_data[0])
            instrument_id = int(trade_data[1])
            side = int(trade_data[2])
            traded_quantity = int(trade_data[3])
            traded_price = float(trade_data[4])

            trades = Trades(
                account_id, instrument_id, side, traded_quantity, traded_price)
            self.trades.append(trades)

    def display_trades(self):
        for record in self.trades:
            print(f"account_id: {record.account_id}")
            print(f"instrument_id: {record.instrument_id}")
            print(f"side: {record.side}")
            print(f"traded_quantity: {record.traded_quantity}")
            print(f"traded_price: {record.traded_price}")
            print()
