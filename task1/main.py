import time 
import threading
from timerUtils import liveCountDownTimer
from logManger import logTimerEnd, logTimerStart


def startTimer():
  print("="*20 + " " + "CountDown Timer" +" "+ "="*20)
  try:
    timingUnit = input("Enter 'm' for minutes and 's' for seconds: ").strip().lower()
    duration = float(input('Enter the Time Duration: '))

    if duration <= 0:
      raise ValueError('Duration must be greater than Zero')

    durationInSeconds = int(duration * 60) if timingUnit == 'm' else int(duration)
    logTimerStart(durationInSeconds)

    timerThread = threading.Thread(target=liveCountDownTimer, args=(durationInSeconds,))
    timerThread.start()
    timerThread.join()

    logTimerEnd()
  except ValueError as e:
    print(f"Invalid Input Application Exit: {e}")

if __name__ == '__main__':
  startTimer()
