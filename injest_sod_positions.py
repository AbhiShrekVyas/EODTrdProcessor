from datetime import datetime


class SODPositions:
    def __init__(self, instrument_id, account_id, sod_quantity, mtm_price, value, time_stamp):
        self.instrument_id = instrument_id
        self.account_id = account_id
        self.sod_quantity = sod_quantity
        self.mtm_price = mtm_price
        self.value = value
        self.time_stamp = time_stamp
    time_stamp = datetime.now()


class SODPosnFileIngestion:
    def __init__(self, posn_file_path):
        self.posn_file_path = posn_file_path
        self.sod_positions = []

    def ingest_posn_file(self):
        with open(self.posn_file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            posn_data = line.strip().split(',')
            instrument_id = int(posn_data[0])
            account_id = int(posn_data[1])
            sod_quantity = int(posn_data[2])
            mtm_price = float(posn_data[3])
            value = float(posn_data[4])
            time_stamp = datetime.now()

            positions = SODPositions(
                instrument_id, account_id, sod_quantity, mtm_price, value, time_stamp)
            self.sod_positions.append(positions)

    def display_sod_positions(self):
        for record in self.sod_positions:
            print(f"instrument_id: {record.instrument_id}")
            print(f"account_id: {record.account_id}")
            print(f"sod_quantity: {record.sod_quantity}")
            print(f"mtm_price: {record.mtm_price}")
            print(f"value: {record.value}")
            print(f"value: {record.time_stamp}")
            print()
    