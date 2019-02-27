from app import app
import time
import datetime

@app.route('/')
@app.route('/index')
def index():
    ts = time.ctime()
    now = str(datetime.datetime.utcnow())
    res = ts + "-NOW serg tit UTC-" + now
    return res
