import time

def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)   #işlemi 1 saniye geciktirecek
    print("GERI SAYIM BITTI")

seconds = input("How many seconds to count down? Enter an integer: ")
while not seconds.isdigit():
    seconds = input("Please enter int number: ")
seconds = int(seconds)
countdown(seconds)