from fastapi import APIRouter

from app.api.v1.predictions import router as predictions_router
from app.settings import settings

router = APIRouter(prefix='/v1', include_in_schema=settings.app.develop)
router.include_router(predictions_router)
