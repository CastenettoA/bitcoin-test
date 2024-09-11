"""this module contain shared code"""

from datetime import datetime
import http.client as http
import json

from _models import Transaction

# function used to connect to a host and get response and data from the endpoint
def get(host: str, endpoint: str) -> tuple:
    """connect to a specified host and return the resp and data"""
    conn = http.HTTPSConnection(host)
    conn.request("GET", endpoint)
    resp = conn.getresponse()
    data = resp.read()
    return resp, data

# get the total values in Satoshis from a list of transactions
def get_satoshis_from_txs(txs) -> float:
    sat = 0.0 # the total number of Satoshis start from zero

    for tx in txs: # loop every tx
        for output in tx["out"]: # loop on every tx output
            if output["spent"]: # if the output is spent
                sat += output["value"] # add the value to the sat local variable

    return sat

# return the higher txs from a list of txs
def get_higher_txs(txs: list, number_of_txs= 10) -> tuple :
    high_txs = [] # this will be [(sat, tx), ...]

    for tx in txs: 
        # sum all output value of the current tx
        sat = 0.0
        for output in tx["out"]:
            if output["spent"]:
                sat += output["value"]

        high_txs.append((sat, tx)) # add a tuple (sat, tx)

    # order the tx by value, from hight to low
    high_txs.sort(reverse=True, key=lambda x: x[0])

    return high_txs[:number_of_txs]

# return the higher txs from block number
def get_higher_txs_from_block(block_hash: str, n_tx: int):
    block_data = get_block_data(block_hash)

    if not block_data:
        print("error: block data is void")

    high_txs = get_higher_txs(block_data["tx"], n_tx)

    if not high_txs:
        print("error: error retriving high_txs")

    return high_txs

# get a list of dict of tx from a txs list of tuple
def get_txs_from_tx_tuple(txs_tuple):
    txs_formatted = []
    for tx_tuple in txs_tuple:
        txs_formatted.append(tx_tuple[1])
    return txs_formatted

# convert a value in satoshis to a btc value
def convert_satoshis_to_btc(satoshis: float):
    return satoshis / 100_000_000

# get all the block data linked to a block by the block hash unique id
def get_block_data(block_hash: str|int):
    resp, data = get("blockchain.info", f"/rawblock/{block_hash}?format=json") # call the api endpoint to get the full block data
    if resp.status == 200: 
        block = data.decode("utf-8") # this is a str
        block = json.loads(block) # convert the str to a list of dict    
        return block  
    else:
        return False

# get the number of tx and the total satoshi value of a single block
def get_txs_number_and_satoshi_value(block_hash: str):
    block = get_block_data(block_hash)
    if block:         
        n_tx: str = block["n_tx"] # save the number of tx in the block
        sat = get_satoshis_from_txs(block["tx"]) # get the total bitcoin value of all tx in satoshis
        return n_tx, sat
    else:
        return False

# # visualize tx infos
# def visualize_tx_info(tx: Transaction):
#     if tx:
#         print(tx)

# save a list of blocks like an object in a json file
def save_blocks_to_json_file(block_list, filename = "_blocks"):
    with open(f"./files/{filename}.json", "w") as file:
        json.dump(block_list, file, indent=4)


# save a list of tx like an object in a json file
def save_txs_to_json_file(tx_list, limit = 0, filename = "_transactions"):
    """limit: if set like a integer > 0 for eg. 9 or 12 the function limits
    the number of tx saved on the file by the specified number.
    Default behavior is to save all txs."""

    if not tx_list:
        print("error: the tx list is void. Can't save nothing to the file")
        return False

    txs = []
    if limit > 0 :
        for n in range(0, limit):
            txs.append(tx_list[n])
    else:
        txs = tx_list # no limit specified so i add all the tx 

    with open(f"./{filename}.json", "w") as file:
        json.dump(txs, file, indent=4)

# return a readable date from a timestamp in millisecond
def get_readable_date_from_timestamp(timestamp: int):
    timestamp_in_sec = timestamp / 1000
    date = datetime.fromtimestamp(timestamp_in_sec)
    date_formatted = date.strftime('%d-%m-%Y')
    return date_formatted

# get the formatted file name
def get_formatted_file_name(timestamp, num_of_blocks):
    date = get_readable_date_from_timestamp(timestamp)
    second_part = ""

    if num_of_blocks == 1:
        second_part = "1_block"
    else:
        second_part = f"{num_of_blocks}_blocks"

    return f"{date}_{second_part}"
