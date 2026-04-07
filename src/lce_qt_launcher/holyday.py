from datetime import datetime
from enum import Enum

class MONTH(Enum):
    JANUARY = 1
    FEBRURAY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6 
    JULY = 7 
    AUGUST = 8
    SEPTEMBER = 9 
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

HOLIDAYS = {
    f"{MONTH.JANUARY.value}-1": "Happy New Years Day! 🎇",
    f"{MONTH.FEBRURAY.value}-14": "Happy Valentine Day! 💘",
    f"{MONTH.APRIL.value}-1": "April Fool Day 🐟",
    f"{MONTH.APRIL.value}-2": "Celebrate Autism Acceptance Day Today! 🎉🌈♾️",
    f"{MONTH.APRIL.value}": "Happy Autism Acceptance Month! 🎉🌈♾️",
    f"{MONTH.MAY.value}-4": "Star Wars Day 🌟",
    f"{MONTH.MAY.value}-17": "Minecraft Anniversary 🎂",
    f"{MONTH.OCTOBER.value}-31": "Halloween 🎃",
    f"{MONTH.DECEMBER.value}-24": "Xmas Eve 🎄",
    f"{MONTH.DECEMBER.value}-25": "Xmas 🎅",
    f"{MONTH.DECEMBER.value}-31": "New Year Eve 🎆"
}

HOLIDAYS_FRENCH = {
f"{MONTH.JANUARY.value}-1": "Bonne année ! 🎇",
f"{MONTH.FEBRURAY.value}-14": "Bonne Saint-Valentin ! 💘",
f"{MONTH.APRIL.value}-1": "Poisson d'avril 🐟",
f"{MONTH.APRIL.value}-2": "Célébrons la Journée de sensibilisation à l'autisme aujourd'hui ! 🎉🌈♾️",
f"{MONTH.APRIL.value}": "Joyeux mois de sensibilisation à l'autisme ! 🎉🌈♾️",
f"{MONTH.MAY.value}-4": "Journée Star Wars 🌟",
f"{MONTH.MAY.value}-17": "Anniversaire de Minecraft 🎂",
f"{MONTH.OCTOBER.value}-31": "Halloween 🎃",
f"{MONTH.DECEMBER.value}-24": "Veille de Noël 🎄",
f"{MONTH.DECEMBER.value}-25": "Noël 🎅",
f"{MONTH.DECEMBER.value}-31": "Veille du Nouvel An 🎆"
}

NO_HOLYDAY = ""

def get_holyday() -> str:
    today = datetime.now()
    month_key = str(today.month) 
    day_key = f"{month_key}-{today.day}"
    return HOLIDAYS.get(day_key, HOLIDAYS.get(month_key, NO_HOLYDAY))