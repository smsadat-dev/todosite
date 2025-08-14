import datetime

def showTIme():
    currTime = datetime.datetime.now()
    formattedTime = currTime.strftime('%H:%M:%S , %d/%m/%Y')
    return formattedTime