from datetime import datetime
import json
import http.client as http

""" This program visualize the last n. blocks 
confirmed from a specified unix epoch timestamp.
It also search for all transactions (aka tx) and calculate the
total Bitcoin value of a Block. 
"""

# function used to connect to a host and get response and data from the endpoint
def get(host: str, endpoint: str) -> tuple:
    """connect to a specified host and return the resp and data"""
    conn = http.HTTPSConnection(host)
    conn.request("GET", endpoint)
    resp = conn.getresponse()
    data = resp.read()
    return resp, data

# get the last blocks from a specific timestamp epoch time
def get_blocks_data(timestamp: int, number_of_blocks: int):
    resp, data = get("blockchain.info", f"/blocks/{timestamp}?format=json")
    if resp.status == 200: 
        blocks = data.decode("utf-8") # this is a str
        blocks = json.loads(blocks) # convert the str to a list of dict
        
        # create an list with only n- blocks
        blocks_filtered = [] # the filtered blocks list

        for n in range(number_of_blocks):
            blocks_filtered.append(blocks[n]) # add block to the list
            current_block_hash = blocks[n]["hash"] # get block hash
            n_tx, sat = get_block_data(current_block_hash) # get the full block data

            # add n_tx, sat infos to the current block
            blocks_filtered[n]["n_tx"] = n_tx
            blocks_filtered[n]["total_sat_val"] = sat # the total value in satoshis 
            blocks_filtered[n]["total_bitc_val"] = sat/100_000_000 # the total value in bitcoin (there is 100 million satoshi per bitcoin)

        return blocks_filtered
    else:
        return False

# get the number of tx and the total satoshi value of a single block
def get_block_data(block_hash: str):
    resp, data = get("blockchain.info", f"/rawblock/{block_hash}?format=json") # call the api endpoint to get the full block data
    if resp.status == 200: 
        block = data.decode("utf-8") # this is a str
        block = json.loads(block) # convert the str to a list of dict           
        n_tx: str = block["n_tx"] # save the number of tx in the block
        sat = get_satoshis_from_txs(block["tx"]) # get the total bitcoin value of all tx in satoshis
        return n_tx, sat
    else:
        return False

# get the total values in Satoshis from a list of transactions
# warn: this is no perfect because we need to remove also the miner fees
def get_satoshis_from_txs(txs) -> float:
    sat = 0.0 # the total number of Satoshis start from zero

    for tx in txs: # loop every tx
        for output in tx["out"]: # lopp on every tx output
            if output["spent"]: # if the output is spent
                sat += output["value"] # add the value to the sat local variable

    return sat

# print some infos of given blocks
def print_blocks_infos(blocks):
    # check for error (eventualy make better error handling)
    if blocks == False:
        print("error happened.")
        return

    for b in blocks: 
        print("block number", b["height"])
        print("block hash  ", b["hash"])    
        print("block tx count", b["n_tx"])
        print("block total bitcoin sent  ", b["total_bitc_val"]) 
        print("^\n^\n^")

# save a list of blocks like an object in a json file
def save_blocks_to_json_file(block_list, filename):
    with open(f"./files/{filename}.json", "w") as file:
        json.dump(block_list, file, indent=4)

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

# ---- the program start here ---- 

if __name__ == "__main__":

    # get the last 2 block with timestamp 1720346046000
    timestamp = 1720346046000 #this is a millis timestamp of 7/7/2024 ...
    num_of_blocks_to_return = 3
    blocks = get_blocks_data(timestamp, num_of_blocks_to_return)

    # print the info for every block
    print_blocks_infos(blocks)

    # get a formatted file name
    filename = get_formatted_file_name(timestamp, num_of_blocks_to_return)

    # save the blocks in a json file
    save_blocks_to_json_file(blocks, filename)