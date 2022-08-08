from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette import status

from controller import user_controller

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