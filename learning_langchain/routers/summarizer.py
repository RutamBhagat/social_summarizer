from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder

from learning_langchain.social_summarizer import social_summarizer
from learning_langchain.utils.type_classes import Person_Request

router = APIRouter()


@router.post("/process", status_code=status.HTTP_201_CREATED)
async def create_new_todo(person_request: Person_Request):
    person_info, profile_pic_url = social_summarizer(name=person_request.name)
    response = {
        "summary": person_info.summary,
        "interesting_facts": person_info.interesting_facts,
        "topics_of_interest": person_info.topics_of_interest,
        "ice_breakers": person_info.ice_breakers,
        "profile_picture": profile_pic_url,
    }
    return response
