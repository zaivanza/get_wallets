import json

types = {1: "evm", 2: "aptos", 3: "starknet"}
type_wallets = types[int(input('\n1. evm\n2. aptos\n3. starknet\n\n1 / 2 / 3 : '))]

types = {1: "key", 2: "address", 3: "seed"}
from_wallet = types[int(input('\nчто вставил в from_wallets.txt\n1. key\n2. address\n3. seed\n\n1 / 2 / 3 : '))]

types = {1: "key", 2: "address", 3: "seed"}
to_wallet = types[int(input('\nчто хочешь получить\n1. key\n2. address\n3. seed\n\n1 / 2 / 3 : '))]

with open(f"from_wallets.txt", "r") as f:
    from_wallets = [row.strip() for row in f]

def create_data():

    def call_json(result, outfile):
        with open(f"{outfile}.json", "w") as file:
            json.dump(result, file, indent=4, ensure_ascii=False)

    with open(f"data/{type_wallets}/key.txt", "r") as f:
        key = [row.strip() for row in f]

    with open(f"data/{type_wallets}/address.txt", "r") as f:
        address = [row.strip() for row in f]

    with open(f"data/{type_wallets}/seed.txt", "r") as f:
        seed = [row.strip() for row in f]

    result = []

    zero = -1
    for items in key:
        zero += 1

        result.append(
            {"key": items, "address": address[zero], "seed": seed[zero]}
        )

    call_json(result, f'data/{type_wallets}/data')

def get_data():

    create_data()
    
    with open(f"data/{type_wallets}/data.json", "r") as file:
        DATA = json.load(file)

    file = open(f'result.txt', 'w', encoding='utf-8')

    for wallet in from_wallets:

        for items in DATA:

            if wallet.lower() == items[from_wallet].lower():
                print(items[to_wallet])
                file.write(f'{items[to_wallet]}\n')

    print(f'\nРезультат записан в result.txt\n')

get_data()

