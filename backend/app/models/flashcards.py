from typing import Optional
from enum import Enum

from app.models.core import IDModelMixin, CoreModel


class FlashCardBase(CoreModel):
    """
    All common characteristics of our Flashcard resource
    """
    english: Optional[str]
    french: Optional[str]
    description: Optional[str]


class FlashCardCreate(FlashCardBase):
    english: str
    french: str

class FlashCardUpdate(FlashCardBase):
    description: Optional[str]


class FlashCardInDB(IDModelMixin, FlashCardBase):
    english: str
    french: str
    description: Optional[str]


class FlashCardPublic(IDModelMixin, FlashCardBase):
    pass