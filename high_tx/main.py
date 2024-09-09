"""this program search the transaction (tx) 
with the bigger Satoshis value on a specific block
and display (or print) his value on the stdo"""

from _helpers import convert_satoshis_to_btc, get_block_data, get_higher_txs, save_txs_to_json_file

if __name__ == "__main__":

    block_hash = "00000000000000000000fc7e5d1214672f23fc61b88e15617b16662af75bce98"
    
    print("getting block data...")
    block_data = get_block_data(block_hash)

    txs = get_higher_txs(block_data["tx"])

    # convert tuple (sat, tx) to dict {tx}
    txs_formatted = []
    for tx_tuple in txs:
        txs_formatted.append(tx_tuple[1])

    print("saving txs on json file...")
    save_txs_to_json_file(txs_formatted)

    print("the json file is ready. Open the index.html to visualize it.")