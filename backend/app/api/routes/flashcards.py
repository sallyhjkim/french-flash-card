from typing import List

from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED

from app.models.flashcards import FlashCardCreate, FlashCardPublic
from app.db.repositories.flashcards import FlashCardsRepository
from app.api.dependencies.database import get_repository


router = APIRouter()




@router.get("/")
async def get_all_flashcards(flashcards_repo: FlashCardsRepository = Depends(get_repository(FlashCardsRepository))) -> List[dict]:
    flashcards = await flashcards_repo.get_flashcards()

    return flashcards



@router.post("/", response_model=FlashCardPublic, name="flashcards:create-flashcard", status_code=HTTP_201_CREATED)
async def create_new_cleaning(
    new_flashcard: FlashCardCreate = Body(..., embed=True),
    flashcards_repo: FlashCardsRepository = Depends(get_repository(FlashCardsRepository)),
) -> FlashCardPublic:
    created_flashcard = await flashcards_repo.create_flashcards(new_flashcard=new_flashcard)

    return created_flashcard

