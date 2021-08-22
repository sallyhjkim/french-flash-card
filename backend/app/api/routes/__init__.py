from fastapi import APIRouter

from app.api.routes.flashcards import router as flashcards_router


router = APIRouter()


router.include_router(flashcards_router, prefix="/flashcards", tags=["flashcards"])

