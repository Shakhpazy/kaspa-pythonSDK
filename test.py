from client.rest_client import RestClient

kaspa = RestClient()
address = "kaspa:qpz2vgvlxhmyhmt22h538pjzmvvd52nuut80y5zulgpvyerlskvvwm7n4uk5a"
balance = kaspa.get_balance(address)
print(f"Balance for address {address}: {balance}")