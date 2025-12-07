from client.rest_client import RestClient

class KaspaClient():

    def __init__(self):
        self.rest_client = RestClient()
        














# This method should be in my other class that uses RestClient, not here directly
    # def get_transactions(self, address, limit: int = 100):
    #     transactions = self.get_full_transactions_raw(address, limit=limit, offset=0, resolve="light")
    #     simplified_transactions = []
    #     for tx in transactions:
    #         # Extract inputs
    #         input_utxo = []
    #         for utxo_in in tx["inputs"]:
    #             input_utxo.append({
    #                 "address": utxo_in.get("previous_outpoint_address"),
    #                 "amount": utxo_in.get("previous_outpoint_amount")
    #             })

    #         # Extract outputs
    #         output_utxo = []
    #         for utxo_out in tx["outputs"]:
    #             output_utxo.append({
    #                 "address": utxo_out.get("script_public_key_address"),
    #                 "amount": utxo_out.get("amount")
    #             })

    #         simplified_tx = {
    #             "transaction_id": tx.get("transaction_id"),
    #             "timestamp": tx.get("block_time"),
    #             "is_accepted": tx.get("is_accepted"),
    #             "inputs": input_utxo,
    #             "outputs": output_utxo
    #         }
    #         simplified_transactions.append(simplified_tx)
        
    #     return simplified_transactions