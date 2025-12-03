import requests
from utils.converstions import Conversions
from utils.apierror import KaspaAPIError

class RestClient:

    def __init__(self):
        self.base_url = "https://api.kaspa.org/"
        pass
    

    
    # -------------------------------
    # Public REST API method calls
    # -------------------------------


    def get_balance(self, address: str):
        """
        Fetch the balance for a Kaspa address in KASPA
        Args:
            address (str): A Kaspa address.
        Returns:
            float: Balance in KAS.
        Raises:
            KaspaAPIError: If the REST API returns an error.
        """

        url = f"{self.base_url}/addresses/{address}/balance"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching balance ({response.status_code}): {response.text}"
            )

        data = response.json()
        
        return Conversions.sompi_to_kaspa(data["balance"])


    def get_utxos(self, address: str):
        """
        Fetch all unspent transaction outputs (UTXOs) associated with a Kaspa address.

        Args:
            address (str): A valid Kaspa address in bech32 format (e.g., 'kaspa:qr...').

        Returns:
            list[dict]: A list of UTXO objects returned by the Kaspa REST API.
            
            Each UTXO dictionary has the structure:
            
            {
                "address": str,
                "outpoint": {
                    "transactionId": str,
                    "index": int
                },
                "utxoEntry": {
                    "amount": str,  # value in sompi (1 KAS = 100,000,000 sompi)
                    "scriptPublicKey": {
                        "scriptPublicKey": str
                    },
                    "blockDaaScore": str,
                    "isCoinbase": bool
                }
            }

            Example:
                [
                    {
                        "address": "kaspa:qr2adz...",
                        "outpoint": {
                            "transactionId": "86c1f9de...655e",
                            "index": 0
                        },
                        "utxoEntry": {
                            "amount": "300000000",
                            "scriptPublicKey": {
                                "scriptPublicKey": "20d5d6..."
                            },
                            "blockDaaScore": "93802825",
                            "isCoinbase": false
                        }
                    }
                ]

        Raises:
            KaspaAPIError: If the REST API returns a non-200 response
                        (e.g., invalid address or server error).
        """

        url = f"{self.base_url}/addresses/{address}/utxos"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching UTXOs ({response.status_code}): {response.text}"
            )

        return response.json()  # list of raw UTXO dicts

    def get_known_names(self):
        """
        Fetch all Kaspa addresses that have registered public names.

        This endpoint returns a list of well-known or publicly labeled addresses
        (e.g., exchange hot wallets, community-recognized addresses, foundation
        wallets, mining pools, donation addresses, etc.). Only addresses that have
        an officially registered or explorer-recognized name appear in this list.

        Returns:
            list[dict]: A list of address-name mappings returned by the Kaspa REST API.
            
            Each entry in the list has the structure:

            {
                "address": str,   # full kaspa: bech32 address
                "name": str       # the registered or recognized name
            }

            Example:
                [
                    {
                        "address": "kaspa:qq1234...",
                        "name": "Kaspa Foundation"
                    },
                    {
                        "address": "kaspa:qp89ab...",
                        "name": "Exchange: MEXC"
                    }
                ]

        Raises:
            KaspaAPIError: If the REST API returns a non-200 status code
                        (e.g., server error, rate limit, unavailable endpoint).
        """
        url = f"{self.base_url}/addresses/names"
        response = requests.get(url)

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching Names ({response.status_code}): {response.text}"
            )

        return response.json() # list of all known addresses with names
    
    def get_top_wallets(self, limit: int | None = None):
        """
        Fetch the top Kaspa addresses (rich list). The API currently does not support
        server-side limiting, so the full list is retrieved and optionally sliced.

        Args:
            limit (int | None): Optional maximum number of ranked wallets to return.
                                Must be in the range [1, 9999] if provided.
                                If None, returns the full list.

        Returns:
            list[dict]: Rich-list entries with:
                {
                    "rank": int,
                    "address": str,
                    "amount": int
                }

        Raises:
            ValueError: If limit is outside the range [1, 9999].
            KaspaAPIError: If the REST API call fails.
        """

        url = f"{self.base_url}/addresses/top"
        response = requests.get(url)

        if limit and not 1 <= limit <= 9999:
            raise ValueError("limit must be in the inclusive range [1, 9999]")

        if not response.ok:
            raise KaspaAPIError(
                f"Error fetching top wallets ({response.status_code}): {response.text}"
            )

        data = response.json()
        ranking = data[0]["ranking"]

        if limit is None:
            return ranking

        return ranking[:limit]


    def get_transactions(self):
        pass
    
    def get_transaction_count(self):
        pass


    




