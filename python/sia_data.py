import json, requests, datetime, pytz, pandas as pd

def query(URL):
	r = requests.get(URL)
	if r.status_code != 200:
		return False
	return r.json()

def readableTimestamp(self, unix, utc = True):
	''' pass unix timestamp from data | returns human-readable timestamp as type datetime '''
	if utc:
		return pd.to_datetime(unix, unit="ms").replace(tzinfo=pytz.utc)
	return pd.to_datetime(unix, unit="ms")


class SiaDB(object):

	# More information available @ https://siastats.info/api
	# Github/Source: https://github.com/hakkane84/navigator-sia

	def __init__(self):
		self.ROOT = "https://siastats.info"

	################################# General Endpoints #################################

	def currentStatus(self, endpoint = ":3500/navigator-api/status"):
		''' Current status ( consensus ) | <class 'list'>
		ex:	[{"consensusblock":282682,"lastblock":282682,"mempool":97,"coinsupply":44930512992,"totalTx":"14332509","heartbeat":1603223359984,"peers":8,"version":"1.4.10"}]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def skynetData(self, endpoint = "/dbs/skynet_evo.json"):
		''' File count and file size on skynet sorted by address | <class 'list'>
		ex:	[
			 {"date":1584835200000,
				"files":{"SiaSky.net":45117,"SiaCDN.com":8,"SkynetHub.io":0,"SiaLoop.net":26701,"total":71826},
				"size":{"SiaSky.net":0.86,"SiaCDN.com":0,"SkynetHub.io":0,"SiaLoop.net":0.11,"total":0.97}}....,
			]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def blockchainHistory(self, endpoint = "/dbs/blockchainsize.json"):
		''' Consensus.db file size (GB), real blockchain size (bytes) and average block size (kB) evolution | <class 'list'>
		ex:	[
			 {"time":1513555200000,"consensussize":8},...,
			 {"time":1603065600000,"consensussize":22,"blockchainsize":20918912218,"averageblocksize":353}
			]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	################################# Contract Data #################################

	def activeContractHistory(self, ENDPOINT = "/dbs/activecontracts.json"):
		''' Contract history | <class 'list'> | size units in TBs, cost units in millions (of Siacoins)
		ex:	[
			 {"time":1433548800000,"activecontractcount":0,"activecontractsize":0,"activecontractcost":0},...,
			 {"time":1603065600000,"activecontractcount":160266,"activecontractsize":417.72384256,"activecontractcost":4.6016143886286285}
			]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def cumulativeContractHistory(self, ENDPOINT = "/dbs/historiccontracts.json"):
		''' Cumulative (total) contract history | <class 'list'> | size units in TBs, cost units in millions (of Siacoins)
		ex:	[
			 {"time":1433548800000,"contractcount":"0","contractcost":0,"contractsize":0}...,
			 {"time":1603065600000,"contractcount":"1611349","contractcost":86.49296159330096,"contractsize":8110.335506782746}
			]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def newContractHistory(self, ENDPOINT = "/dbs/newcontractsdb.json"):
		''' Cost, size and count of newly formed contracts (daily and 7d avgs) | <class 'list'> | size units ???, cost units ???
		ex:	[
			 {"time":1433548800000,"newcontractcount":0,"newcontractcost":0,"newcontractsize":0},...,
			 {"time":1603065600000,"newcontractcount":1549,"newcontractcost":41751.073904569865,
			  "newcontractsize":-1990.44890624,"count7d":3078,"size7d":550.3454131931428,"cost7d":50481.348179157605}
			]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	################################# Host & User Data #################################

	def activeHostHistory(self, endpoint = "/dbs/activehosts.json"):
		''' Host history | <class 'list'>
		ex:	[{"date":1506384000000,"hosts":630},...,{"date":1603152000000,"hosts":256,"hostsonline":310}]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def bandwidthPriceHistory(self, endpoint = "/dbs/bandwidthpricesdb.json"):
		''' Avg. upload and download price history | <class 'list'> | price units in SC and USD
		ex:	[{"date":1505001600000,"up":31.1,"down":23.14},...,{"date":1603152000000,"up":236.86,"down":405.52,"upusd":0.66,"downusd":1.14}]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def storageHistory(self, endpoint = "/dbs/storage.json"):
		''' Historical available and utilized storage data | <class 'list'> | units in TBs
		ex:	[{"date":1505088000000,"total":3131.175,"used":73.92},...,{"date":1603152000000,"total":2152.53,"used":718.93}]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def storagePriceHistory(self, endpoint = "/dbs/storagepricesdb.json"):
		''' Avg price, contract fees, siafunds fees | <class 'list'> | price, newcontractformation units in SC/TB/mo, usd units in USD/TB/mo, sfperfee units in ???
		ex:	[{"date":1505001600000,"price":209.44,"sfperfees":11.75},...,{"date":1603152000000,"price":1120.7,"newcontractformation":55.69,"usd":3.14,"sfperfees":7.56}]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def usageHistory(self, endpoint = "/dbs/ussage.json"):
		''' Percentage of network storage (available v. used) | <class 'list'>
		ex:	[{"date":1505088000000,"used":2.36,"free":97.64},...,{"date":1603152000000,"used":33.4,"free":66.6}]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	################################# Supply Data #################################

	def currentSupply(self, ENDPOINT = ":3500/navigator-api/totalcoins"):
		''' Current supply | <class 'int'> | supply units in Siacoins '''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def supplySchedule(self, endpoint = "/dbs/coinsupplydb.json"):
		''' Historical and predicted coin supply | <class 'list'> | units in billions (of Siacoins)
		ex:	[{"time":1433548800000,"coinsupply":0.005999810000000001},...,{"time":1792195200000,"coinsupply":54.31376299194149}]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def inflationSchedule(self, endpoint = "/dbs/inflationdb.json"):
		''' Historical and predicted inflation metrics | <class 'list'> | units in ?
		ex:	[{"time":1433548800000,"coinsupply":0.005999810000000001},...,{"time":1792195200000,"coinsupply":54.31376299194149}]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def burnHistory(self, endpoint = "/dbs/burn.json"):
		''' Historical (cumulative) burned Siacoins from failed contracts | <class 'list'> | units in Siacoins
		ex:	[{"time":1433548800,"burnt":0},...,{"time":1792108800000,"inflation":2.88},{"time":1792195200000,"inflation":2.88}]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def blockRewardHistory(self, endpoint = "/dbs/blockrewarddb.json"):
		''' Historical block rewards | <class 'list'> | units in Siacoins
		ex:	[{"time":1436313600000,"inflation":571.27},...,{"time":1823731200000,"blockreward":30000}]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	################################# Transaction Data #################################
	def txnHistory(self, endpoint = "/dbs/transactionsdb.json"):
		''' Historical cumlative and daily transaction data | <class 'list'>
		ex:	[{"time":1433548800000,"totaltx":"20","daytx":18},...,{"time":1603065600000,"totaltx":"14316540","daytx":26760}]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	def txnFeeHistory(self, endpoint = "/dbs/txfeesdb.json"):
		''' Fees per txn, avg fees per block and cumulative fees | <class 'list'>
		ex:	[
			 {"time":1433548800000,"txfee":0,"feeperblock":0,"feecount":"0"},...,
			 {"time":1603065600000,"txfee":0.02092675635276532,"feeperblock":4.2748091603053435,"feecount":"8801099"}
			]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)

	################################# Siafunds Data #################################

	def siafundsMetrics(self, endpoint = "/dbs/sfdb.json"):
		''' Siafunds profitability (daily, 7d-avg [daily, monthly, historic]) | <class 'list'> | units in Siacoins
		ex:	[
			 {"time":1433548800000,"historicSF":0,"SF24h":0,"SF30d":0},...,
			 {"time":1603065600000,"historicSF":337.32255021387374,"SF24h":0.16282918822782247,"SF30d":5.916540940738047,"SF7d":0.1968772578987147}
			]
		'''
		URL = self.ROOT + ENDPOINT
		return query(URL)





if __name__ == "__main__":
	client = SiaDB()
	supply = client.totalSupply()
	