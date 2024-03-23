from fastapi import APIRouter

router = APIRouter(prefix='/predictions', tags=['Predictions'])


@router.post('/')
async def predict_team1_win():
    return 0.5
