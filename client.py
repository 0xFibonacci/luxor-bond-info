from web3 import Web3


class Client:

    def __init__(self, rpc):
        self.rpc = rpc
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        self.check_connection()

    def check_connection(self):
        print(f'Is connected: {self.web3.isConnected()}')

    def get_contract(self, address, abi):
        return self.web3.eth.contract(address=address, abi=abi)