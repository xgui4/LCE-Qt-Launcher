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
    f"{MONTH.APRIL.value}-2": "Celebrate Autism Accetance Day Today! 🎉🌈♾️",
    f"{MONTH.APRIL.value}": "Happy Autism Accetance Month! 🎉🌈♾️",
    f"{MONTH.MAY.value}-4": "Star Wars Day 🌟",
    f"{MONTH.MAY.value}-17": "Minecraft Anniversary 🎂",
    f"{MONTH.OCTOBER.value}-31": "Halloween 🎃",
    f"{MONTH.DECEMBER.value}-24": "Xmas Eve 🎄",
    f"{MONTH.DECEMBER.value}-25": "Xmas 🎅",
    f"{MONTH.DECEMBER.value}-31": "New Year Eve 🎆"
}

NO_HOLYDAY = "No holiday"

def get_holyday() -> str:
    today = datetime.now()
    month_key = str(today.month) 
    day_key = f"{month_key}-{today.day}"
    return HOLIDAYS.get(day_key, HOLIDAYS.get(month_key, NO_HOLYDAY))