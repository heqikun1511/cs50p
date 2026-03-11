import sys
def main():
    time=input('what time?').strip()
    hour,min=time.split(":")
    hour_int=int(hour)
    min_int=int(min)
    meal_time=convert(hour_int,min_int)
    if meal_time>=7 and meal_time<=8:
        print('breakfast time')


def convert(hour,min):
    return float(hour+float(min/60))

main()