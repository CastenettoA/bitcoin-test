from flask import Flask, jsonify, render_template, request
from _helpers import get_higher_txs_from_block, get_txs_from_tx_tuple

app = Flask(__name__)
default_block_hash = "00000000000000000000fc7e5d1214672f23fc61b88e15617b16662af75bce98"

@app.route("/", methods=["GET"])
def home():
    # return render_template("index.html")
    return """hello. <br /> <a href='/high_txs_from_block_hash' >/high_txs_from_block_hash api</a>"""

@app.route("/high_txs_from_block_hash", methods=["GET"])
def return_higher_tx():
    hash = request.args.get("block_hash", default=default_block_hash)
    n_tx = request.args.get("n_tx", default=10)

    print("endpoint /high_txs_from_block_hash")
    print(hash)
    print(n_tx)
    print("call to get_higher_txs_from_block() ...")

    txs = get_higher_txs_from_block(hash, n_tx)
    txs_formatted = get_txs_from_tx_tuple(txs)

    return jsonify(txs_formatted)

if __name__ == '__main__':
    app.run(debug=True)