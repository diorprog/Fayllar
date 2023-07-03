import time
from datetime  import date
import datetime



# now = datetime.datetime.now()
# now_date = now.strftime("%Y-%m-%d")
#
# print(date.today())
# print(date.fromisoformat(now_date) - date.fromisoformat("2014-02-28"))
#
# print(date.fromtimestamp(0))


#

sec=234352
print(date.today()-date.fromtimestamp(sec))