import requests
from utils.converstions import Conversions
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
        response = response.json()
        balance = Conversions.sompi_to_kaspa(response['balance'])
        return balance 


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


    




