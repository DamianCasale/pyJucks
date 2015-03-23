from app import celery

from app.data import my_data

@celery.task
def my_logic():
    # get data
    data = my_data.delay()
    # do something with the data
    print "I am logic"
    return data.get()