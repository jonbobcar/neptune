import time
import schedule
import neptune

def job():

    change = neptune.nep_monitor()

    print("Did the game state change:", change)

    if change == True:
        neptune.nep_get()
        neptune.nep_plot()
        neptune.nep_html()
        # neptune.nep_copy()
        change = False
    
    print("Ran the job")
    
# schedule.every().hour.at(":54").do(job)
schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    