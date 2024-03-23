from fastapi import APIRouter

router = APIRouter(prefix='/predictions', tags=['Predictions'])

print('test')


@router.post('/')
async def predict_team1_win():
    return 0.5
