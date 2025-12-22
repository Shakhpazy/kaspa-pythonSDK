import requests
from utils.converstions import Conversions
from utils.apierror import KaspaAPIError

VALID_RESOLVES = {"light", "full"}
VALID_ACCEPTANCE = {"accepted", "rejected"}

class RestClient:

    def __init__(self):
        self.base_url = "https://api.kaspa.org"
    

    # -------------------------------
    # Public REST API method calls for addresses
    # -------------------------------

<<<<<<< HEAD
=======

    # -------------------------------
    # Kaspa addresses API
    # -------------------------------
>>>>>>> a280ff5081f58b7fbe8f32966602aa14875934bb
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
    def get_top_wallets(self):
        url = f"{self.base_url}/addresses/top"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching top wallets ({response.status_code}): {response.text}"
            )

        return response.json() # list of top wallets


    def get_full_transactions_raw(self, address, limit: int = 500, offset: int = 0, resolve = None):
        if limit < 1 or limit > 500 or offset < 0:
            raise ValueError("limit must be in [1, 500] and offset must be >= 0")
        if resolve and resolve not in VALID_RESOLVES:
            raise ValueError("resolve must be one of: 'light', 'full', or None")

        params = {
            "limit": limit,
            "offset": offset,
        }

        if resolve in VALID_RESOLVES:
            params["resolve_previous_outpoints"] = resolve

        url = f"{self.base_url}/addresses/{address}/full-transactions"
    
        response = requests.get(url, params=params)
        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching transactions ({response.status_code}): {response.text}"
            )
        
        return response.json()

    def get_full_transactionpage_raw(self, address, limit: int = 500, before: int = 0, after : int = 0, resolve = None, acceptance = None):

        if limit < 1 or limit > 500 or before < 0 or after < 0:
            raise ValueError("limit must be in [1, 500] and before/after must be >= 0")
        
        if resolve and resolve not in VALID_RESOLVES:
            raise ValueError("resolve must be one of: 'light', 'full', 'None'")
        
        if acceptance and acceptance not in VALID_ACCEPTANCE:
            raise ValueError("acceptance must be one of: 'accepted', 'rejected', 'None'")

        url = f"{self.base_url}/addresses/{address}/full-transactions-page"
        params = {
            "limit": limit,
            "before": before,
            "after": after,
        }

        if resolve in VALID_RESOLVES:
            params["resolve_previous_outpoints"] = resolve
        if acceptance in VALID_ACCEPTANCE:
            params["acceptance"] = acceptance

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
    
    # -------------------------------
    # Kaspa network api
    # -------------------------------
    def __error(response):
        raise KaspaAPIError(
                f"Error fetching the kaspa REST API ({response.status_code}) : {response.text}" 
            )

    def get_blue_score_info(self):
        url = f"{self.base_url}/info/virtual-chain-blue-score"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)
            
        data = response.json()
        return data
    
    def get_blockdag_info(self):
        url = f"{self.base_url}/info/blockdag"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)
        
        data = response.json()
        return data

    def get_coinsupply_info(self):
        url = f"{self.base_url}/info/coinsupply"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)

        data = response.json()
        return data
    
    def get_coinsupply_circulating_info(self):
        url = f"{self.base_url}/info/coinsupply/circulating"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)

        data = response.json()
        return data
    
    def get_coinsupply_total_info(self):
        url = f"{self.base_url}/info/coinsupply/total"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)

        data = response.json()
        return data
    
    def get_kaspad_info(self):
        url = f"{self.base_url}/info/kaspad"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)

        data = response.json()
        return data
    
    def get_kaspa_fee_estimate(self):
        url = f"{self.base_url}/info/fee-estimate"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)

        data = response.json()
        return data

    def get_kaspa_price(self):
        url = f"{self.base_url}/info/price"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)

        data = response.json()
        return data
    
    def get_blockreward_info(self):
        url = f"{self.base_url}/info/blockreward"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)

        data = response.json()
        return data

    def get_halving_info(self):
        url = f"{self.base_url}/info/halving"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)

        data = response.json()
        return data
    
    def get_hashrate_info(self):
        url = f"{self.base_url}/info/hashrate"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)

        data = response.json()
        return data
    
    def get_max_hashrate_info(self):
        url = f"{self.base_url}/info/hashrate/max"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)

        data = response.json()
        return data

    def get_kaspa_health(self):
        url = f"{self.base_url}/info/health"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)

        data = response.json()
        return data

    def get_kaspa_marketcap(self):
        url = f"{self.base_url}/info/marketcap"
        response = requests.get(url)

        if not response.ok:
            self.__error(response)

        data = response.json()
        return data


    def get_hashrate_history(self):
        pass

    # -------------------------------
    # Public REST API method calls for Kaspa network information
    # -------------------------------
    def get_virtual_blue_score(self):
        url = f"{self.base_url}/info/virtual-chain-blue-score"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching virtual blue score ({response.status_code}): {response.text}"
            )
        
        return response.json()
    
    def get_blockdag_info(self):
        url = f"{self.base_url}/info/blockdag"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching blockdag info ({response.status_code}): {response.text}"
            )
        
        return response.json()
    
    def get_info_coinsupply(self):
        url = f"{self.base_url}/info/coinsupply"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching coin supply ({response.status_code}): {response.text}"
            )
        
        return response.json()
    
    def get_info_kaspad(self):
        url = f"{self.base_url}/info/kaspad"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching kaspad info ({response.status_code}): {response.text}"
            )
        
        return response.json()

    def get_info_fee_estimate(self):
        url = f"{self.base_url}/info/fee-estimate"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching fee estimates ({response.status_code}): {response.text}"
            )
        
        return response.json()
    
    def get_info_price(self):
        url = f"{self.base_url}/info/price"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching price info ({response.status_code}): {response.text}"
            )
        
        return response.json()

    def get_info_blockreward(self):
        url = f"{self.base_url}/info/blockreward"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching block reward info ({response.status_code}): {response.text}"
            )
        
        return response.json()

    def get_info_halving(self):
        url = f"{self.base_url}/info/halving"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching halving info ({response.status_code}): {response.text}"
            )
        
        return response.json()
    
    def get_info_hashrate(self):
        url = f"{self.base_url}/info/hashrate"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching hashrate info ({response.status_code}): {response.text}"
            )
        
        return response.json()
    
    def get_info_hashrate_max(self):
        url = f"{self.base_url}/info/hashrate/max"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching max hashrate info ({response.status_code}): {response.text}"
            )
        
        return response.json()
    
    #TODO implemetn hashtrate history endpoints

    def get_info_marketcap(self):
        url = f"{self.base_url}/info/marketcap"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching marketcap info ({response.status_code}): {response.text}"
            )
        
        return response.json()
    




