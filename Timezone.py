import pytz
import datetime
import random
from colorama import Fore, init, deinit

init()

def display_time(city_name:str) -> str:

    time_get = pytz.timezone(city_name)
    local_time = datetime.datetime.now(time_get)
    local_time = local_time.strftime("%d %b %Y  %I:%M:%S %p") 
    print (f"{Fore.BLUE} The current date and time in {Fore.GREEN}{city_name}{Fore.BLUE} is {Fore.GREEN} {local_time}.")


output = None

var = list(pytz.all_timezones)


while True:
    print(Fore.YELLOW + "Timexones: ")
    print(Fore.YELLOW + "-" * 20)

    var_new = []

#Generation of random Timezones
    for i in range(0, 10):
        no = random.randint(0,len(var))

        if var[no] in var_new:
            pass

        print(i + 1, var[no])
        var_new.append(var[no])

    print()
    choosen = int(input(Fore.BLUE + "Choose your Location: "))
    if choosen <= 10:
        print(Fore.BLUE + "-" * 50)
        display_time(var_new[choosen - 1])
        break

deinit()


