import requests
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.request import ScoreRequest
from models.database import SessionLocal, OwnerDB, CarDB

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_external_database(data):
    response = requests.post("https://external.api/check", json=data)  # Поменять на параметры релевантного API
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="External API error")


@router.post("/api/external-check")
async def external_check(request: ScoreRequest, db: Session = Depends(get_db)):
    # Обращаемся к внешней базе данных
    result = check_external_database(request.model_dump())

    if result.get("status") == "match":
        # Записываем положительный результат в базу данных
        for owner_data in request.owners:
            owner = OwnerDB(**owner_data.model_dump())
            db.add(owner)
            db.commit()
            db.refresh(owner)

            for car_data in request.car:
                car = CarDB(**car_data.model_dump(), owner_id=owner.id)
                db.add(car)
                db.commit()
                db.refresh(car)

    return {"message": "External check completed", "result": result}
