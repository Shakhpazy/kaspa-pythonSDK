import unittest
import requests
from client.rest_client import RestClient

class TestRestClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = RestClient()
        cls.base_address = "https://api.kaspa.org/"
    
    # def test_get_balance(self):
    #     address = "kaspa:qr2adzl6vl69thdss2parxcyctlmwa979xfswxafzl9lh9y8pnja6pcceswpr"
    #     result = self.client.get_balance(address)
    #     self.assertIsInstance(result, dict)
    #     #Manual verification required for dynamic data 
    #     response = requests.get(f"{self.base_address}/addresses/{address}/balance")
    #     direct_api_result = response.json()
    #     self.assertEqual(result, direct_api_result)
    
    # def test_get_utxos(self):
    #     address = "kaspa:qr2adzl6vl69thdss2parxcyctlmwa979xfswxafzl9lh9y8pnja6pcceswpr"
    #     result = self.client.get_utxos(address)
    #     self.assertIsInstance(result, list)
    #     #Manual verification required for dynamic data 
    #     response = requests.get(f"{self.base_address}/addresses/{address}/utxos")
    #     direct_api_result = response.json()
    #     self.assertEqual(result, direct_api_result)
    
    # def test_get_known_names(self):
    #     result = self.client.get_known_names()
    #     self.assertIsInstance(result, list)
    #     #Manual verification required for dynamic data 
    #     response = requests.get(f"{self.base_address}/addresses/names")
    #     direct_api_result = response.json()
    #     self.assertEqual(result, direct_api_result)
    
    # def test_get_top_wallets(self):
    #     result = self.client.get_top_wallets()
    #     self.assertIsInstance(result, list)
    #     self.assertEqual(len(result[0]["ranking"]), 10000)

    # def test_get_full_transactions_raw_basic(self):
    #     address = "kaspa:qr2adzl6vl69thdss2parxcyctlmwa979xfswxafzl9lh9y8pnja6pcceswpr"
    #     result = self.client.get_full_transactions_raw(address)
    #     self.assertIsInstance(result, list)
    #     # Manual verification required for dynamic data 
    #     response = requests.get(f"{self.base_address}/addresses/{address}/full-transactions", 
    #                           params={"limit": 500, "offset": 0})
    #     direct_api_result = response.json()
    #     self.assertEqual(result, direct_api_result)

    # def test_get_full_transactions_raw_with_params(self):
    #     address = "kaspa:qr2adzl6vl69thdss2parxcyctlmwa979xfswxafzl9lh9y8pnja6pcceswpr"
    #     result = self.client.get_full_transactions_raw(address, limit=100, offset=10)
    #     self.assertIsInstance(result, list)
    #     # Manual verification required for dynamic data 
    #     response = requests.get(f"{self.base_address}/addresses/{address}/full-transactions", 
    #                           params={"limit": 100, "offset": 10})
    #     direct_api_result = response.json()
    #     self.assertEqual(result, direct_api_result)

    # def test_get_full_transactions_raw_invalid_limit(self):
    #     address = "kaspa:qr2adzl6vl69thdss2parxcyctlmwa979xfswxafzl9lh9y8pnja6pcceswpr"
    #     with self.assertRaises(ValueError):
    #         self.client.get_full_transactions_raw(address, limit=0)
        
    #     with self.assertRaises(ValueError):
    #         self.client.get_full_transactions_raw(address, limit=501)

    # def test_get_full_transactions_raw_invalid_offset(self):
    #     address = "kaspa:qr2adzl6vl69thdss2parxcyctlmwa979xfswxafzl9lh9y8pnja6pcceswpr"
    #     with self.assertRaises(ValueError):
    #         self.client.get_full_transactions_raw(address, offset=-1)

    # def test_get_full_transactions_raw_invalid_resolve(self):
    #     address = "kaspa:qr2adzl6vl69thdss2parxcyctlmwa979xfswxafzl9lh9y8pnja6pcceswpr"
    #     with self.assertRaises(ValueError):
    #         self.client.get_full_transactions_raw(address, resolve="invalid")
        




if __name__ == "__main__":
    unittest.main()






