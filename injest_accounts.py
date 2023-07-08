class Accounts:
    def __init__(self,  account_id, account_name, team):
        self.account_id = account_id
        self.account_name = account_name
        self.team = team


class AccountsFileIngestion:
    def __init__(self, acct_file_path):
        self.acct_file_path = acct_file_path
        self.accounts = []

    def ingest_acct_file(self):
        with open(self.acct_file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            acct_data = line.strip().split(',')
            account_id = int(acct_data[0])
            
            account_name = str(acct_data[1])
            if len(account_name) > 32:
                account_name = account_name[:32]

            team = str(acct_data[2])
            if len(team) > 32:
                team = team[:32]

            accounts = Accounts(
                account_id, account_name, team)
            self.accounts.append(accounts)

    def display_accounts(self):
        for record in self.accounts:
            print(f"account_id: {record.account_id}")
            print(f"account_name: {record.account_name}")
            print(f"team: {record.team}")
            print()
