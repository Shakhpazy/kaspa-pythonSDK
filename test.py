from client.rest_client import RestClient

kaspa = RestClient()
address = "kaspa:qr2adzl6vl69thdss2parxcyctlmwa979xfswxafzl9lh9y8pnja6pcceswpr"
top = kaspa.get_top_wallets(limit=9999)
print(len(top))