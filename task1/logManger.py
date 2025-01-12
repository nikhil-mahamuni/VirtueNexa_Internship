import os
from datetime import datetime

LOG_FILE = './timerLog.txt'

def ensureLogFileEXist():
  os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
  if not os.path.isfile(LOG_FILE):
    with open(LOG_FILE, 'w') as file:
      file.write('Times Log\n')
      file.write('='*20 + "\n")

def logTimerStart(duration):
  ensureLogFileEXist()
  startTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open(LOG_FILE, 'a') as file:
    file.write(f"Timer started at: {startTime}\n")
    file.write(f"Timer Duration: {duration} sec\n")

def logTimerEnd():
  endTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open(LOG_FILE, 'a') as file:
    file.write(f"Timer ended at: {endTime}\n")
    file.write('-'*50+ '\n')
