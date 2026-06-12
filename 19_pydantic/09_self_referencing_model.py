from pydantic import BaseModel, field_validator, model_validator
from typing import List, Optional


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None


Comment.model_rebuild()

comment = Comment(
    id=2,
    content="Some content",
    replies=[
        Comment(id=2, content="reply 1"),
        Comment(
            id=3,
            content="reply 2",
            replies=[
                Comment(id=5, content="nested reply"),
            ],
        ),
        Comment(id=4, content="reply 5"),
    ],
)
