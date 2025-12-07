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
    
    # def test_get_top_wallets_no_params(self):
    #     result = self.client.get_top_wallets()
    #     self.assertIsInstance(result, list)
    #     self.assertEqual(len(result), 10000)
    
    # def test_get_top_wallets_with_limit(self):
    #     limit = 50
    #     result = self.client.get_top_wallets(limit=limit)
    #     self.assertIsInstance(result, list)
    #     self.assertEqual(len(result), limit)

    def test_get_full_transactions_raw_bad_inputs(self):
        pass
        




if __name__ == "__main__":
    unittest.main()






