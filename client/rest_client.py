import requests

class RestClient:

    def __init__(self):
        self.base_url = "https://api.kaspa.org/"
        pass
    

    
    # -------------------------------
    # Public REST API method calls
    # -------------------------------
    def get_balance(self, address):
        ulr = f"{self.base_url}/addresses/{address}/balance"
        response = (requests.get(ulr))

        if response.status_code == 404:
            raise Exception(f"Error fetching balance: {response.status_code} - {"The address is invalid"}")
        result = response.json()
        return result['balance'] / 100000000  # Convert from sompi to KASPA


    def get_utxos(self, address):
        pass

    def get_names(self):
        pass
    
    def get_name(self):
        pass

    def get_transactions(self):
        pass
    
    def get_transaction_count(self):
        pass


kaspa = RestClient()
address = "kaspa:qr2adzl6vl69thdss2parxcyctlmwa979xfswxafzl9lh9y8pnja6pcceswpr"
balance = kaspa.get_balance(address)
print(balance)


    




