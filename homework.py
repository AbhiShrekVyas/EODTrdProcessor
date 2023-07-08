from general_functions import *
from injest_instruments import *
from injest_sod_positions import *
from injest_trades import *
from injest_accounts import *
from process_eod_position import *
from process_pnl import *

# Command to invoke program:
#        python homework.py -i instruments.csv -s sod_positions.csv -a accounts.csv -t trades.csv

validate_params()
print(get_time(), '[INFO] [Input parameters validated]')

print(get_time(), '[INFO] [before feeds injestion]')

# Following code demonstrates the usage of different classes (InstrFileIngestion, SODPosnFileIngestion, AccountsFileIngestion, and TradeFileIngestion)
#  to ingest and process various files (instruments, SOD positions, accounts, and trade summaries) based on the command-line arguments.
# Instrument Usage example
instr_file_path = sys.argv[2]
instr_ingestion = InstrFileIngestion(instr_file_path)
instr_ingestion.ingest_instr_file()
# instr_ingestion.display_instruments()

# SOD Positions Usage example
sod_posn_file_path = sys.argv[4]
posn_ingestion = SODPosnFileIngestion(sod_posn_file_path)
posn_ingestion.ingest_posn_file()
# posn_ingestion.display_sod_positions()

# Accounts List Usage example
acct_file_path = sys.argv[6]
accounts_ingestion = AccountsFileIngestion(acct_file_path)
accounts_ingestion.ingest_acct_file()
# accounts_ingestion.display_accounts()

# Trade Summary Usage example
trade_file_path = sys.argv[8]
trades_ingestion = TradeFileIngestion(trade_file_path)
trades_ingestion.ingest_trade_file()
# trades_ingestion.display_trades()

print(get_time(), '[INFO] [Feeds ingestion process complete]')

print(get_time(),
      '[INFO] [Generate EOD position report based on new trades and store in object..]')
positions_processing(accounts_ingestion, posn_ingestion,
                     trades_ingestion, sod_posn_file_path)

print(get_time(), '[INFO] [New EOD Position Processing complete ]')
print(get_time(),
      '[INFO] [Add unchanged positions into the EOD Positions Report.. ]')

eod_posn_file_path = 'PositionsReport.csv'
add_sod_positions_to_eod(sod_posn_file_path, eod_posn_file_path)

print(get_time(),
      '[INFO] [EOD Positions report with updated positions saved successfully!]')

print(get_time(),
      '[INFO] [Generate Daily PnL Report..]')

generate_pnl(instr_file_path,acct_file_path)

print(get_time(),
      '[INFO] [Daily PnL Report generated]')
