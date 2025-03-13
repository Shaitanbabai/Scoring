from fastapi import APIRouter, HTTPException
from models.request import ScoreRequest


router = APIRouter()


@router.post("/api/score-calculate")
async def calculate_score(request: ScoreRequest):
    # Здесь можно добавить логику для обработки данных и расчета рейтинга
    # Например, вызывать функции из /services/rating.py

    response_data = {
        "message": "Score calculated successfully",
        # Здесь можно вернуть рассчитанный рейтинг или другую информацию
    }

    return response_data