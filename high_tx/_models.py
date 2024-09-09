from typing import Literal

# Previous transaction output
class PreviousOutput:
    type: int
    spent: bool
    value: int
    spending_outpoints: list
    n: int
    tx_index: int
    script: str
    addr: str

# Transaction input
class Input:
    sequence: int
    witness: str
    script: str
    index: int
    prev_out: PreviousOutput

# Transaction output
class Output:
    type: int
    spent: bool
    value: int # the value in satoshis
    spending_outpoints: list
    n: int
    tx_index: int
    script: str
    addr: str 


# A bitcoin transaction
class Transaction:
    hash: str 
    ver: Literal[1, 2] # version of tx
    vin_sz: int
    vout_sz: int
    size: int
    weight: int
    fee: int
    relayed_by: str
    tx_index: int
    double_spend: bool
    time: int
    block_index: int
    block_height: int
    inputs: list[Input] # all tx inputs
    out: list[Output]

    """ if is 0 the tx can be included in any block. 
        if is a number < 500.000.000 will be included not before this block number
        if the value is > 500.000.000 will be parset like a epoch time and included in a block with
        a 'median past time' (MPT) > than the lock time."""
    lock_time: int