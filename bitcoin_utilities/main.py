# convert satoshi to citcoin
import sys


def convert_from_sat(satoshis: float):
    return float(satoshis) / 100_000_000.00

# convert bitcoin to satoshi
def convert_from_btc(bitcoin: float):
    return float(bitcoin) * 100_000_000.00

# get argv from console
def get_argv():
    if len(sys.argv) > 1:
        fn_name = sys.argv[1]
        value = sys.argv[2]
        return fn_name, value
    else:
        print("your expression is invalid")
        print("for eg. 'python3 bitcoin_utilities/main.py convert_from_sat 8400000'")
        

# the main process
def main():
    fn_name, value = get_argv()
    res = 0

    match fn_name:
        case "convert_from_sat":
            res = convert_from_sat(value)
        case "convert_from_btc":
            res = convert_from_btc(value)
        case _:
            print("the function name you have inserted is not supported")
            print("you can use only: convert_from_sat and convert_from_btc ")
            print("for eg. 'python3 bitcoin_utilities/main.py convert_from_sat 8400000'")

    print(res)
               


if __name__ == "__main__":
    main()
