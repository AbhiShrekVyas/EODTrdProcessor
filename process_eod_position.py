from general_functions import *
from injest_instruments import *
from injest_sod_positions import *
from injest_trades import *
from injest_accounts import *
import csv
import time


def write_eod_positions(self):
    csv_file = 'PositionsReport.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        header = ['instrument_id', 'account_id',
                  'sod_quantity', 'mtm_price', 'value', 'timestamp']
        writer.writerow(header)
        for record in self.sod_positions:
            writer.writerow([record.instrument_id, record.account_id,
                            record.sod_quantity, record.mtm_price, record.value, record.time_stamp])


def positions_processing(self, posn_ingestion, trades_ingestion, posn_file_path):
    # Initialize CSV writer
    self.posn_ingestion = posn_ingestion
    self.trades_ingestion = trades_ingestion
    self.posn_file_path = posn_file_path
    extract_generation = SODPosnFileIngestion(posn_file_path)
    updated_qty = 0  # Initialize updated_qty for each trade_record
    eod_posn = None  # Initialize eod_posn to None for each trade_record

    # Update EOD Positions based on trading done
    for trade_record in trades_ingestion.trades:
        print(trade_record.traded_price)
        for posn_record in posn_ingestion.sod_positions:
            if (trade_record.side == -1):
                print('trade record side:', trade_record.side)
                trade_record.traded_quantity = (
                    trade_record.traded_quantity * -1)

            if (trade_record.instrument_id == posn_record.instrument_id and trade_record.account_id == posn_record.account_id):
                print(get_time(), '[INFO] [Position existed on instrument_id:', posn_record.instrument_id,
                      ' and account_id:', posn_record.account_id, 'combination, hence netting the position]')
                if eod_posn is None:
                    print(
                        get_time(), '[INFO] [Trade being netted first time as eod_posn is None]')
                    updated_qty = posn_record.sod_quantity + trade_record.traded_quantity
                    eod_posn = SODPositions(trade_record.instrument_id, trade_record.account_id,
                                            updated_qty, trade_record.traded_price, (updated_qty * trade_record.traded_price), datetime.utcnow())
                    break
                else:
                    print(get_time(),
                          '[INFO] [Adding more trades to netted trade]')
                    updated_qty = updated_qty + trade_record.traded_quantity
                    eod_posn = SODPositions(trade_record.instrument_id, trade_record.account_id, updated_qty,
                                            trade_record.traded_price, (updated_qty * trade_record.traded_price), datetime.utcnow())
                    break
            else:
                if eod_posn is None:
                    print(get_time(), '[INFO] [New position opened on instrument_id:', trade_record.instrument_id,
                          'and account_id:', trade_record.account_id, ', adding to EOD report]')
                    eod_posn = SODPositions(trade_record.instrument_id, trade_record.account_id, trade_record.traded_quantity,
                                            trade_record.traded_price, (trade_record.traded_quantity * trade_record.traded_price), datetime.utcnow())
                    time.sleep(0.5)
                    break
                else:
                    if (trade_record.instrument_id == eod_posn.instrument_id and trade_record.account_id == eod_posn.account_id):
                        print(get_time(), '[INFO] [Update on Existing Position, instrument_id:', trade_record.instrument_id,
                              'and account_id:', trade_record.account_id, ', adding to EOD report]')
                        net_qty = abs(eod_posn.sod_quantity +
                                      trade_record.traded_quantity)
                        print('net_qty is', net_qty)
                        net_value = eod_posn.value + \
                            (trade_record.traded_quantity *
                             trade_record.traded_price)
                        print('net_value is', net_value)
                        eod_posn = SODPositions(trade_record.instrument_id, trade_record.account_id,
                                                net_qty, trade_record.traded_price, net_value, datetime.utcnow())
                        extract_generation.sod_positions.append(eod_posn)
                        time.sleep(0.5)
                        break
                    else:
                        print(get_time(), '[INFO] [Another New position opened on instrument_id:', trade_record.instrument_id,
                              'and account_id:', trade_record.account_id, ', adding to EOD report]')
                        eod_posn = SODPositions(trade_record.instrument_id, trade_record.account_id, trade_record.traded_quantity,
                                                trade_record.traded_price, (trade_record.traded_quantity * trade_record.traded_price), datetime.utcnow())
                        time.sleep(0.5)
                        break
        
    extract_generation.sod_positions.append(eod_posn)
    # extract_generation.display_sod_positions()
    write_eod_positions(extract_generation)
    print(get_time(), '[INFO] [EOD Positions report created successfully!]')


def add_sod_positions_to_eod(sod_positions_file, eod_positions_file):
    # Read SOD_positions.csv
    with open(sod_positions_file, 'r', newline='') as sod_file:
        sod_positions_list = list(csv.reader(sod_file))

    # Read EOD_positions.csv
    with open(eod_positions_file, 'r', newline='') as eod_file:
        eod_positions_list = list(csv.reader(eod_file))

    # Create a set of existing (instrument_id, account_id) combinations in EOD_positions.csv
    existing_positions = set((row[0], row[1]) for row in eod_positions_list)

    # Add new SOD positions to EOD positions if the combination is not already present
    for sod_position in sod_positions_list:
        instrument_id = sod_position[0]
        account_id = sod_position[1]
        if (instrument_id, account_id) not in existing_positions:
            eod_positions_list.append(sod_position)

    # Write updated EOD_positions.csv
    with open(eod_positions_file, 'w', newline='') as eod_file:
        writer = csv.writer(eod_file)
        writer.writerows(eod_positions_list)
