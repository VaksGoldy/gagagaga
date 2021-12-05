duration = input('Введи длительность промежутка времени в секундах ')
if int(duration) < 60:
    print(duration + ' сек')
elif int(duration) < 3600:
    min = int(duration) // 60
    sec = int(duration) % (min * 60)
    print(min, " минут", sec, " секунд")
elif int(duration) < 86400:
    hours = int(duration) // 3600
    min = (int(duration) - (hours * 3600)) // 60
    sec = (int(duration) % (hours * 3600)) - min * 60
    print(hours, " часов", min, " минут", sec, " секунд")
else:
    days = int(duration) // 86400
    hours = (int(duration) - (days * 86400)) // 3600
    min = (int(duration) - (days * 86400) - (hours * 3600)) // 60
    sec = int(duration) - (days * 86400) - (hours * 3600) - (min * 60)
    print(days, "дней,", hours, "часов,", min, "минут,", sec, "секунд.")




