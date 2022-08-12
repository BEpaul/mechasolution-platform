import json

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette import status

from controller import user_controller
from model.db_helper import user_session
from testconn.models import dummyTable

router = APIRouter(
    prefix="/attention",
    tags=['attention']
)

controller = user_controller


@router.get("/")
async def read_attention_list():
    response = controller.get_attention_list()

    return response


@router.post("/{influencer_id}", status_code=status.HTTP_201_CREATED)
async def add_to_attention_list(influencer_id: str):
    response = controller.add_to_attention_list(influencer_id)

    return response

@router.delete("/{influencer_id}")
async def delete_user(influencer_id: str):
    response = controller.delete_user(influencer_id)

    return response


@router.get("/test")
async def test():
    sample_data1 = '[{"key1": 1, "key2": "another key"}, {"key1": 2, "key2": "other key"}]'
    sample_data = (json.loads(sample_data1))
    jso = json.dumps(sample_data)
    print(jso)

    test = json.loads(jso)

    print(type(test[0]['key1']))
    print(type(test[0]['key2']))

    return jso
