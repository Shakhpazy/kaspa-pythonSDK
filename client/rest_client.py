import requests
from utils.converstions import Conversions
from utils.apierror import KaspaAPIError

class RestClient:

    def __init__(self):
        self.base_url = "https://api.kaspa.org/"
    

    # -------------------------------
    # Public REST API method calls
    # -------------------------------


    def get_balance(self, address: str):
        url = f"{self.base_url}/addresses/{address}/balance"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching balance ({response.status_code}): {response.text}"
            )

        data = response.json()
        
        return data


    def get_utxos(self, address: str):
        url = f"{self.base_url}/addresses/{address}/utxos"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching UTXOs ({response.status_code}): {response.text}"
            )

        return response.json()  # list of raw UTXO dicts

    def get_known_names(self):
        url = f"{self.base_url}/addresses/names"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching Names ({response.status_code}): {response.text}"
            )

        return response.json() # list of all known addresses with names
    
    #Experimental endpoint
    def get_top_wallets(self, limit: int | None = None):
        if limit and not 1 <= limit <= 9999:
            raise ValueError("limit must be in the inclusive range [1, 9999]")
        
        url = f"{self.base_url}/addresses/top"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching top wallets ({response.status_code}): {response.text}"
            )

        data = response.json()
        ranking = data[0]["ranking"]

        if limit is None:
            return ranking

        return ranking[:limit]


    def get_full_transactions_raw(self, address, limit: int = 500, offset: int = 0, resolve = None):
        if limit < 1 or limit > 500 or offset < 0:
            raise ValueError("limit must be in [1, 500] and offset must be >= 0")
        if resolve and resolve not in {"light", "full"}:
            raise ValueError("resolve must be one of: 'light', 'full', or None")

        params = {
            "limit": limit,
            "offset": offset,
        }

        if resolve and resolve in {"light", "full"}:
            params["resolve_previous_outpoints"] = resolve

        url = f"{self.base_url}/addresses/{address}/full-transactions"
    
        response = requests.get(url, params=params)
        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching transactions ({response.status_code}): {response.text}"
            )
        
        return response.json()

    def get_full_transactionpage_raw(self, address, limit: int = 500, before: int = 0, after : int = 0, resolve: str = "no", acceptance: str = ""):
        if limit < 1 or limit > 500 or before < 0 or after < 0:
            raise ValueError("limit must be in [1, 500] and before/after must be >= 0")
        
        if resolve not in {"no", "light", "full"}:
            raise ValueError("resolve must be one of: 'no', 'light', 'full'")

        url = f"{self.base_url}/addresses/{address}/full-transactionpage"
        params = {
            "limit": limit,
            "before": before,
            "after": after,
            "resolve_previous_outpoints": resolve
        }

        response = requests.get(url, params=params)
        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching transaction page ({response.status_code}): {response.text}"
            )
        
        return response.json()

    
    def get_transaction_count(self, address) -> int:
        url = f"{self.base_url}/addresses/{address}/transactions-count"
        response = requests.get(url)
        
        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching transaction count ({response.status_code}): {response.text}"
            )
        
        data = response.json()
        return data


    




