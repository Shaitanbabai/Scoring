from pydantic import BaseModel, constr, conint
from typing import List

class Owner(BaseModel):
    fio: str
    date_birth: str
    region: str
    passport: constr(regex=r'^\d{10}$')  # Регулярное выражение для валидации номера паспорта
    inn: constr(regex=r'^\d{12}$')  # Регулярное выражение для валидации ИНН

class Car(BaseModel):
    VIN: str
    gos_number: str

class ScoreRequest(BaseModel):
    owners: List[Owner]
    car: List[Car]