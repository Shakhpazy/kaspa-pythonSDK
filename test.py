from client.rest_client import RestClient

kaspa = RestClient()
address = "kaspa:qr2adzl6vl69thdss2parxcyctlmwa979xfswxafzl9lh9y8pnja6pcceswpr"
transactioncount = kaspa.get_transaction_count(address)
print(f"Transaction Count: {transactioncount}")
print("\n-----\n")