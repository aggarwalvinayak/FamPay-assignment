from .views import async_fetch
import schedule

schedule.every(1).minutes.do(async_fetch)


