
class Instruments:
    def __init__(self, instrument_id, display_symbol, primary_exchange, handle_value, currency):
        self.instrument_id = instrument_id
        self.display_symbol = display_symbol
        self.primary_exchange = primary_exchange
        self.handle_value = handle_value
        self.currency = currency


class InstrFileIngestion:
    def __init__(self, instr_file_path):
        self.instr_file_path = instr_file_path
        self.instruments = []

    def ingest_instr_file(self):
        with open(self.instr_file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            instr_data = line.strip().split(',')
            instrument_id = int(instr_data[0])
            display_symbol = instr_data[1]
            primary_exchange = instr_data[2]
            handle_value = float(instr_data[3])
            currency = instr_data[4]

            instruments = Instruments(
                instrument_id, display_symbol, primary_exchange, handle_value, currency)
            self.instruments.append(instruments)

    def display_instruments(self):
        for record in self.instruments:
            print(f"instrument_id: {record.instrument_id}")
            print(f"display_symbol: {record.display_symbol}")
            print(f"primary_exchange: {record.primary_exchange}")
            print(f"handle_value: {record.handle_value}")
            print(f"currency: {record.currency}")
            print()
