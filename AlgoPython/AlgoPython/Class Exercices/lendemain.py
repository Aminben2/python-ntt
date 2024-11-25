day = int(input("Entrer le Jour: "))
month = int(input("Entrer le Mois: "))
year = int(input("Enter l'Année: "))
if day == 31:
    if month == 12:
        print(f"La date de lendemain est: 1/1/{year+1}")
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
        print(f"La date de lendemain est: 1/{month+1}/{year}")

elif day == 30 and (month == 4 or month == 6 or month == 9 or month == 11):
    print(f"La date de lendemain est: 1/{month + 1}/{year}")

elif day == 28 and month == 2:
    print(f"La date de lendemain est: 1/3/{year}")

elif day < 31 and day >= 1 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
    print(f"La date de lendemain est: {day + 1}/{month}/{year}")

elif day < 30 and day >= 1 and (month == 4 or month == 6 or month == 9 or month == 11):
    print(f"La date de lendemain est: {day + 1}/{month}/{year}")

else:
    print("Date unvalide")