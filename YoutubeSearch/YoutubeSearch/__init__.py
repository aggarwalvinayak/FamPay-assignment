
import django
django.setup()
from .views import async_fetch
import time
import multiprocessing 

def updateDB():
	time.sleep(10)
async_fetch()

# asyncUpdate= multiprocessing.Process(target=updateDB)
# asyncUpdate.start()
# asyncUpdate.join()