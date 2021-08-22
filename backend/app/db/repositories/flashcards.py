from app.db.repositories.base import BaseRepository
from app.models.flashcards import FlashCardCreate, FlashCardUpdate, FlashCardInDB


"""
One of the benefits of using the Repository pattern isq
that we get the flexibility of pure SQL, with the clean interface of an ORM.
"""

GET_FLASHCARDS_QUERY = """
    SELECT * FROM flashcards
"""


CREATE_FLASHCARDS_QUERY = """
    INSERT INTO flashcards (english, french, description)
    VALUES (:english, :french, :description)
    RETURNING id, english, french, description;
"""


class FlashCardsRepository(BaseRepository):
    """
    All database actions associated with the flashcards resource
    """
    async def get_flashcards(self) -> FlashCardInDB:
        flashcards = await self.db.fetch_one(query=GET_FLASHCARDS_QUERY)
        print(">>>>>flashcards", flashcards)
        return FlashCardInDB(**flashcards)

    async def create_flashcards(self, *, new_flashcard: FlashCardCreate) -> FlashCardInDB:
        query_values = new_flashcard.dict()
        print(">>>>", query_values)
        flashcards = await self.db.fetch_one(query=CREATE_FLASHCARDS_QUERY, values=query_values)

        return FlashCardInDB(**flashcards)

