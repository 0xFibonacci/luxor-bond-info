from data.bonds import AllBonds, BOND_ABI


class Bond:

    depositor_address = ''
    bonds = []

    def __init__(self, asset_name, term, contract, price=0, percent_vested=0, pending_payout=0):
        self.asset_name = asset_name
        self.term = term
        self.contract = contract
        self.price = price
        self.percent_vested = percent_vested
        self.pending_payout = pending_payout

    def update_bond(self, web3):
        self.price = self.contract.functions.bondPriceInUSD().call()
        self.price = self.round_price(web3, self.price)

        if Bond.depositor_address:
            self.percent_vested = self.contract.functions.percentVestedFor(Bond.depositor_address).call()
            self.pending_payout = self.contract.functions.pendingPayoutFor(Bond.depositor_address).call()

    def round_price(self, web3, price):
        return round(web3.fromWei(price, 'ether'), 2)

    def __repr__(self):
        return f'{self.asset_name}'.center(10) + f'{self.term}'.center(10) + f'{self.price}'.center(10) + \
               f'{self.percent_vested}'.center(12) + f'{self.pending_payout}'.center(12)

    @staticmethod
    def load_bond_contracts(client, depositor_address):
        Bond.depositor_address = depositor_address

        for bond in AllBonds:
            contract = client.get_contract(bond['bondAddress'], BOND_ABI)
            new_bond = Bond(bond['assetName'], bond['term'], contract)
            Bond.bonds.append(new_bond)

        Bond.update_bonds(client)

    @staticmethod
    def update_bonds(client):
        for bond in Bond.bonds:
            bond.update_bond(client.web3)
