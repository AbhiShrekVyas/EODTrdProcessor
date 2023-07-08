Command to invoke program:
        python homework.py -i instruments.csv -s sod_positions.csv -a accounts.csv -t trades.csv


• instruments.csv
    instruments.csv is a headerless comma-separated text file where each line contains information about a tradeable instrument.  The file is constructed as follows:
        ◦ InstrumentId - (int) unique identifier for an instrument
        ◦ DisplaySymbol - (str) symbol for the instrument
        ◦ PrimaryExchange - (str) ISO 10383 4 character market identifier code
        ◦ HandleValue - (float) currency value of 1 point price fluctuation
        ◦ Currency - (str) ISO 4217 3 character currency code

• accounts.csv
    accounts.csv is a headerless comma-separated text file where each line contains information about a trading account.  The file is constructed as follows:
        ◦ AccountId - (int) unique identifier for an account
        ◦ AccountName - (str) name of the account (32 char max)
        ◦ TeamName - (str) name of the team the account belongs to (32 char max)

• sod_positions.csv
    sod_positions.csv is a headerless comma-separated text file where each line contains the start of day position for a particular instrument and account.  The file is constructed as follows:
        ◦ InstrumentId - (int) identifier for an instrument (matches InstrumentId from instruments.csv)
        ◦ AccountId - (int) identifier for an account (matches AccountId from accounts.csv)
        ◦ Quantity - (int) represents the start of day quantity
        ◦ Mark - (float) represents the previous day’s closing price for mark to market purposes
        ◦ Value - (float) represents the currency value of a position
    
• trades.csv
    trades.csv is a headerless comma-separated text file where each line contains transaction information for a given trading day.  The file is constructed as follows:
        ◦ AccountId - (int) identifier for an account (matches AccountId from accounts.csv)
        ◦ InstrumentId - (int) identifier for an instrument (matches InstrumentId from instruments.csv)
        ◦ Side - (int) side of the trade.  -1 represents sell, 1 represents buy
        ◦ Quantity - (int) quantity of the transaction in shares or contracts
        ◦ Price - (float) price at which the transaction occurred


Healthy output for positions & pnl report:

PS E:\0 PyProjects\pyTestDRW> & C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe "e:/0 PyProjects/pyTest***/homework.py" -i instruments.csv -s sod_positions.csv -a accounts.csv -t trades.csv
[2023-06-07 00:37:31] [INFO] [Instruments file: instruments.csv received]
[2023-06-07 00:37:31] [INFO] [SOD Positions file: sod_positions.csv received]
[2023-06-07 00:37:31] [INFO] [Accounts file: accounts.csv received]
[2023-06-07 00:37:31] [INFO] [Trades file: trades.csv received]
[2023-06-07 00:37:31] [INFO] [Input parameters validated]
[2023-06-07 00:37:31] [INFO] [before feeds injestion]
[2023-06-07 00:37:31] [INFO] [Feeds ingestion process complete]
[2023-06-07 00:37:31] [INFO] [Generate EOD position report based on new trades and store in object..]
trade record side: -1
[2023-06-07 00:37:31] [INFO] [New position opened on instrument_id: 4 and account_id: 5 , adding to EOD report]
3011.75
[2023-06-07 00:37:32] [INFO] [Update on Existing Position, instrument_id: 4 and account_id: 5 , adding to EOD report]
net_qty is 1
net_value is -3007.25
308.37
[2023-06-07 00:37:32] [INFO] [Another New position opened on instrument_id: 3 and account_id: 4 , adding to EOD report]
309.15
[2023-06-07 00:37:33] [INFO] [Update on Existing Position, instrument_id: 3 and account_id: 4 , adding to EOD report]
net_qty is 1200
net_value is 370200.0
309.0125
[2023-06-07 00:37:33] [INFO] [Another New position opened on instrument_id: 3 and account_id: 1 , adding to EOD report]
[2023-06-07 00:37:34] [INFO] [EOD Positions report created successfully!]
[2023-06-07 00:37:34] [INFO] [New EOD Position Processing complete ]
[2023-06-07 00:37:34] [INFO] [Add unchanged positions into the EOD Positions Report.. ]
[2023-06-07 00:37:34] [INFO] [EOD Positions report with updated positions saved successfully!]
[2023-06-07 00:37:34] [INFO] [Generate Daily PnL Report..]
instr_list: [['1', 'TSLA', 'XNAS', '1.0', 'USD'], ['2', 'AAPL', 'XNAS', '1.0', 'USD'], ['3', 'SPY', 'ARCX', '1.0', 'USD'], ['4', 'BP LN', 'XLON', '1.0', 'GBP'], ['5', 'ESU0', 'XCME', '50', 'USD']]
acct_list: [['1', 'Ringo', 'Beatles'], ['2', 'John', 'Beatles'], ['3', 'Mick', 'Rolling Stones'], ['4', 'Keith', 'Rolling Stones'], ['5', 'Rivers', 'Weezer']]
[2023-06-07 00:37:34] [INFO] [Daily PnL Report generated]
PS E:\0 PyProjects\pyTest***> & C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe "e:/0 PyProjects/pyTest***/homework.py" -i instruments.csv -s sod_positions.csv -a accounts.csv -t trades.csv  
[2023-06-07 00:38:17] [INFO] [Instruments file: instruments.csv received]
[2023-06-07 00:38:17] [INFO] [SOD Positions file: sod_positions.csv received]
[2023-06-07 00:38:17] [INFO] [Accounts file: accounts.csv received]
[2023-06-07 00:38:17] [INFO] [Trades file: trades.csv received]
[2023-06-07 00:38:17] [INFO] [Input parameters validated]
[2023-06-07 00:38:17] [INFO] [before feeds injestion]
[2023-06-07 00:38:17] [INFO] [Feeds ingestion process complete]
[2023-06-07 00:38:17] [INFO] [Generate EOD position report based on new trades and store in object..]
3009.5
trade record side: -1
[2023-06-07 00:38:17] [INFO] [New position opened on instrument_id: 4 and account_id: 5 , adding to EOD report]
3011.75
[2023-06-07 00:38:18] [INFO] [Update on Existing Position, instrument_id: 4 and account_id: 5 , adding to EOD report]
net_qty is 1
net_value is -3007.25
308.37
[2023-06-07 00:38:18] [INFO] [Another New position opened on instrument_id: 3 and account_id: 4 , adding to EOD report]
309.15
[2023-06-07 00:38:19] [INFO] [Update on Existing Position, instrument_id: 3 and account_id: 4 , adding to EOD report]
net_qty is 1200
net_value is 370200.0
309.0125
[2023-06-07 00:38:19] [INFO] [Another New position opened on instrument_id: 3 and account_id: 1 , adding to EOD report]
[2023-06-07 00:38:20] [INFO] [EOD Positions report created successfully!]
[2023-06-07 00:38:20] [INFO] [New EOD Position Processing complete ]
[2023-06-07 00:38:20] [INFO] [Add unchanged positions into the EOD Positions Report.. ]
[2023-06-07 00:38:20] [INFO] [EOD Positions report with updated positions saved successfully!]
[2023-06-07 00:38:20] [INFO] [Generate Daily PnL Report..]
[2023-06-07 00:38:20] [INFO] [Daily PnL Report generated]
PS E:\0 PyProjects\pyTest***> 

