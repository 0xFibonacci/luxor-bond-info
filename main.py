from client import Client
from models import Bond


def main():
    ### Setup
    rpc = ""    # Insert your rpc url here
    depositor_address = ''      # Insert your address used to bond here
    client = Client(rpc=rpc)

    Bond.load_bond_contracts(client, depositor_address)

    ### Main Program
    while True:
        print(f'Name'.center(10) + f'Term'.center(10) + f'Price'.center(10) + \
               f'Prc Vested'.center(12) + f'Pen. Payout'.center(12))
        for bond in Bond.bonds:
            print(bond)

        key = input("Press any key to update ('e' to exit): ")

        if key == 'e':
            break
        else:
            Bond.update_bonds(client)


if __name__ == "__main__":
    main()
