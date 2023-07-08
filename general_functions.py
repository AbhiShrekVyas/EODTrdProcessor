import sys
from datetime import datetime


def get_time():
    return f"[{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}]"


def validate_params():
    # Check if all parameters are provided

    if len(sys.argv) != 9:
        print(
            "Please provide input files in the sequence: -i [instruments CSV] -f [sod_positions CSV] -a [accounts CSV] -t [trades CSV]")
        print("Example: python homework.py -i instruments.csv -s sod_positions.csv -a accounts.csv -t trades.csv")
        print("Exiting..")
        sys.exit(1)
    else:
        if sys.argv[1] == "-i":
            print(get_time(), '[INFO] [Instruments file:',
                  sys.argv[2], 'received]')
        else:
            print("please provide paramenters in sequence. Exiting..")
            sys.exit(1)
        if sys.argv[3] == "-s":
            print(get_time(), '[INFO] [SOD Positions file:',
                  sys.argv[4], 'received]')
        else:
            print("please provide paramenters in sequence. Exiting..")
            sys.exit(1)
        if sys.argv[5] == "-a":
            print(get_time(), '[INFO] [Accounts file:',
                  sys.argv[6], 'received]')
        else:
            print("please provide paramenters in sequence. Exiting..")
            sys.exit(1)
        if sys.argv[7] == "-t":
            print(get_time(), '[INFO] [Trades file:', sys.argv[8], 'received]')
        else:
            print("please provide paramenters in sequence. Exiting..")
            sys.exit(1)


def get_latest_timestamp_records(csv_file_path, output_file_path):
    latest_records = {}

    with open(csv_file_path, 'r') as file:
        # Read the header line
        header = file.readline().strip().split(',')

        # Find the indices of columns one, two, and the timestamp
        col1_index = header.index('instrument_id')
        col2_index = header.index('account_id')
        timestamp_index = header.index('timestamp')

        # Iterate over the remaining lines
        for line in file:
            # Split the line into fields
            fields = line.strip().split(',')

            # Extract the relevant values
            col1_value = fields[col1_index]
            col2_value = fields[col2_index]
            timestamp_value = fields[timestamp_index]

            # Check if a record already exists with the same column one and two values
            if (col1_value, col2_value) in latest_records:
                # If the current timestamp is greater, update the latest record
                if timestamp_value > latest_records[(col1_value, col2_value)][timestamp_index]:
                    latest_records[(col1_value, col2_value)] = fields
            else:
                # Create a new record
                latest_records[(col1_value, col2_value)] = fields

    # Write the latest records to the output CSV file
    with open(output_file_path, 'w') as output_file:
        output_file.write(','.join(header) + '\n')  # Write the header line

        for record in latest_records.values():
            output_file.write(','.join(record) + '\n')
