from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue
from api import redis_db as conn
from api.blockchain import storeLatestBlockInDB, getBlockCount, blockchain_db, storeBlockInDB, checkSeeds, get_highest_node

blockheight = 21916

for i in range(0,blockheight):
  storeBlockInDB(i)