import csv


def generate_pnl(instr_file_path, acct_file_path):

    eod_positions_file = 'eod_positions_with_buyprice.csv'
    pnl_csv_file = 'DailyPnLReport.csv'
    instr_list = []
    acct_list = []
    posn_list = []

    # Read instruments.csv
    with open(instr_file_path, 'r', newline='') as instr_file:
        instr_list = list(csv.reader(instr_file))

    # Read accounts.csv
    with open(acct_file_path, 'r', newline='') as acct_file:
        acct_list = list(csv.reader(acct_file))

    # Read eod_positions_with_buyprice.csv
    with open(eod_positions_file, 'r', newline='') as eod_file:
        posn_list = list(csv.reader(eod_file))

    with open(pnl_csv_file, 'w', newline='') as pnl_file:
        writer = csv.writer(pnl_file)
        # Write header row
        writer.writerow(['instrument_name', 'account_name', 'pnl'])
        for instr in instr_list:
            for pos_instr_id in posn_list:
                for acct in acct_list:
                    if (instr[0] == pos_instr_id[0]) and (acct[0] == pos_instr_id[1]):
                        sod_quantity = float(pos_instr_id[2])
                        mtm_price = float(pos_instr_id[3])
                        buy_price = float(pos_instr_id[5])
                        pnl = (sod_quantity * mtm_price) - \
                            (sod_quantity * buy_price)
                        writer.writerow([instr[1], acct[1], pnl])
