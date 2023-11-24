import datetime
laiks = datetime.datetime.now().hour
if 6 <=laiks< 12:
    vards= "Labrīt!"
eliif 12 <=laiks< 18:
    vards="Labdin!"
else:
    vards="Labvakar!"
    print(vards)