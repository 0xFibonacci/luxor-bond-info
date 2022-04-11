
DAI = '0x8D11eC38a3EB5E956B052f67Da8Bdc9bef8Abf3E'
LUX = '0x6671E20b83Ba463F270c8c75dAe57e3Cc246cB2b'
FTM = '0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83'
LUX_DAI = '0x46729c2AeeabE7774a0E710867df80a6E19Ef851'
LUX_FTM = '0x951BBB838e49F7081072895947735b0892cCcbCD'


BOND_ABI = '[{"inputs":[{"internalType":"address","name":"_Luxor","type":"address"},{"internalType":"address","name":"_principle","type":"address"},{"internalType":"address","name":"_treasury","type":"address"},{"internalType":"address","name":"_DAO","type":"address"},{"internalType":"address","name":"_bondCalculator","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"deposit","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"payout","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"expires","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"priceInUSD","type":"uint256"}],"name":"BondCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"priceInUSD","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"internalPrice","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"debtRatio","type":"uint256"}],"name":"BondPriceChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"payout","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"remaining","type":"uint256"}],"name":"BondRedeemed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"initialBCV","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newBCV","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"adjustment","type":"uint256"},{"indexed":false,"internalType":"bool","name":"addition","type":"bool"}],"name":"ControlVariableAdjustment","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipPulled","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipPushed","type":"event"},{"inputs":[],"name":"DAO","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Luxor","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"adjustment","outputs":[{"internalType":"bool","name":"add","type":"bool"},{"internalType":"uint256","name":"rate","type":"uint256"},{"internalType":"uint256","name":"target","type":"uint256"},{"internalType":"uint32","name":"buffer","type":"uint32"},{"internalType":"uint32","name":"lastTime","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bondCalculator","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"bondInfo","outputs":[{"internalType":"uint256","name":"payout","type":"uint256"},{"internalType":"uint256","name":"pricePaid","type":"uint256"},{"internalType":"uint32","name":"lastTime","type":"uint32"},{"internalType":"uint32","name":"vesting","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bondPrice","outputs":[{"internalType":"uint256","name":"price_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bondPriceInUSD","outputs":[{"internalType":"uint256","name":"price_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"currentDebt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"debtDecay","outputs":[{"internalType":"uint256","name":"decay_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"debtRatio","outputs":[{"internalType":"uint256","name":"debtRatio_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_maxPrice","type":"uint256"},{"internalType":"address","name":"_depositor","type":"address"}],"name":"deposit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_controlVariable","type":"uint256"},{"internalType":"uint256","name":"_minimumPrice","type":"uint256"},{"internalType":"uint256","name":"_maxPayout","type":"uint256"},{"internalType":"uint256","name":"_fee","type":"uint256"},{"internalType":"uint256","name":"_maxDebt","type":"uint256"},{"internalType":"uint256","name":"_initialDebt","type":"uint256"},{"internalType":"uint32","name":"_vestingTerm","type":"uint32"}],"name":"initializeBondTerms","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isLiquidityBond","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lastDecay","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxPayout","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"payoutFor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_depositor","type":"address"}],"name":"pendingPayoutFor","outputs":[{"internalType":"uint256","name":"pendingPayout_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_depositor","type":"address"}],"name":"percentVestedFor","outputs":[{"internalType":"uint256","name":"percentVested_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"policy","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"principle","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pullManagement","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner_","type":"address"}],"name":"pushManagement","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"recoverLostToken","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"bool","name":"_stake","type":"bool"}],"name":"redeem","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceManagement","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_addition","type":"bool"},{"internalType":"uint256","name":"_increment","type":"uint256"},{"internalType":"uint256","name":"_target","type":"uint256"},{"internalType":"uint32","name":"_buffer","type":"uint32"}],"name":"setAdjustment","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"enum DaiBondDepository.PARAMETER","name":"_parameter","type":"uint8"},{"internalType":"uint256","name":"_input","type":"uint256"}],"name":"setBondTerms","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_staking","type":"address"},{"internalType":"bool","name":"_helper","type":"bool"}],"name":"setStaking","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"staking","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stakingHelper","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"standardizedDebtRatio","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"terms","outputs":[{"internalType":"uint256","name":"controlVariable","type":"uint256"},{"internalType":"uint256","name":"minimumPrice","type":"uint256"},{"internalType":"uint256","name":"maxPayout","type":"uint256"},{"internalType":"uint256","name":"fee","type":"uint256"},{"internalType":"uint256","name":"maxDebt","type":"uint256"},{"internalType":"uint32","name":"vestingTerm","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalDebt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"treasury","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"useHelper","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'

AllBonds = [
  # 5 DAYS
  {
    'pid': 0,
    'id': 0,
    'bondAddress': '0xCf994423b39A6991e82443a8011Bf6749e19434b',
    'assetName': 'DAI',
    'assetAddress': DAI,
    'token1Address': DAI,
    'term': '5D',
  },
  {
    'pid': 4,
    'id': 3,
    'bondAddress': '0x13729e99A7b77469f7FD204495a7b49e25e8444a',
    'assetName': 'WFTM',
    'assetAddress': FTM,
    'token1Address': FTM,
    'term': '5D',
  },
  {
    'pid': 8,
    'id': 6,
    'bondAddress': '0xaC64DC47A1fe52458D3418AC7C568Edc3306130a',
    'assetName': 'LUX-DAI',
    'assetAddress': LUX_DAI,
    'token1Address': LUX,
    'token2Address': DAI,
    'term': '5D',
  },
  {
    'pid': 12,
    'id': 8,
    'bondAddress': '0xaBAD60240f1a39fce0d828eecf54d790FFF92cec',
    'assetName': 'LUX-FTM',
    'assetAddress': LUX_FTM,
    'token1Address': LUX,
    'token2Address': FTM,
    'term': '5D',
  },

  # 1 WEEK
  {
    'pid': 1,
    'id': 1,
    'bondAddress': '0x80C61168e1F02e1835b541e9Ca6Bb3416a36Af6F',
    'assetName': 'DAI',
    'assetAddress': DAI,
    'token1Address': DAI,
    'term': '1W',
  },
  {
    'pid': 5,
    'id': 4,
    'bondAddress': '0x376969e00621Ebf685fC3D1F216C00d19B162923',
    'assetName': 'WFTM',
    'assetAddress': FTM,
    'token1Address': FTM,
    'term': '1W',
  },
  {
    'pid': 9,
    'id': 7,
    'bondAddress': '0x5612d83dfED9B387c925Ac4D19ED3aeDd71004A8',
    'assetName': 'LUX-DAI',
    'assetAddress': LUX_DAI,
    'token1Address': LUX,
    'token2Address': DAI,
    'term': '1W',
  },
  {
    'pid': 13,
    'id': 9,
    'bondAddress': '0x8dF4f6e20C64DA8DAFC8c43E434f2cFda9C3FCAE',
    'assetName': 'LUX-FTM',
    'assetAddress': LUX_FTM,
    'token1Address': LUX,
    'token2Address': FTM,
    'term': '1W',
  },

  # 2 WEEKS
  {
    'pid': 2,
    'id': 2,
    'bondAddress': '0x73eE5Fcd1336246C74f6448B1d528aeacF5404f2',
    'assetName': 'DAI',
    'assetAddress': DAI,
    'token1Address': DAI,
    'term': '2W',
  },
  {
    'pid': 6,
    'id': 5,
    'bondAddress': '0xc421072646C51FF8983714F28e4253ad8B44bb1E',
    'assetName': 'WFTM',
    'assetAddress': FTM,
    'token1Address': FTM,
    'term': '2W',
  },
  {
    'pid': 10,
    'id': 15,
    'bondAddress': '0xaFADcDca5Aa1F187B357499f2e3BA94D3Cc32ad1',
    'assetName': 'LUX-DAI',
    'assetAddress': LUX_DAI,
    'token1Address': LUX,
    'token2Address': DAI,
    'term': '2W',
  },
  {
    'pid': 14,
    'id': 10,
    'bondAddress': '0x0A98e728f0537f40e8dC261D633fe4a00E1aFA72',
    'assetName': 'LUX-FTM',
    'assetAddress': LUX_FTM,
    'token1Address': LUX,
    'token2Address': FTM,
    'term': '2W'
  },


]