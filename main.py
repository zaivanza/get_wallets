types = {1: "evm", 2: "aptos", 3: "starknet"}
type_wallets = types[int(input('\n1. evm\n2. aptos\n3. starknet\n\n1 / 2 / 3 : '))]

types = {1: "key", 2: "address", 3: "seed"}
type_element = types[int(input('\n1. key\n2. address\n3. seed\n\n1 / 2 / 3 : '))]

print()
min_elem = int(input('from wallet : '))
max_elem = int(input('to wallet   : '))

with open(f"data/{type_wallets}/{type_element}.txt", "r") as f:
    data = [row.strip() for row in f]

file = open(f"result.txt", "w")
print(f'\nSTART ({type_wallets}): {min_elem} - {max_elem}\n')
for x in data[min_elem-1 : max_elem]:
    # cprint(f'{x}', 'white')
    file.write(f'{x}\n')

print(f'\nРезультат записан в result.txt\n')