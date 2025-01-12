import time

def liveCountDownTimer(duration):
  print(f"Coutdown started for duration {duration}")
  while duration > 0:
    minutes = duration // 60
    seconds = duration % 60
    print(f"Time: {minutes: 02d}:{seconds: 02d}")
    time.sleep(1)
    duration -= 1
  print("\n Times Up")