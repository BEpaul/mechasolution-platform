from fastapi import APIRouter, Query
from pydantic import json

from controller import influencer_controller

from typing import Optional

router = APIRouter(
    prefix="/influencers",
    tags=['influencers']
)

controller = influencer_controller


# 리스트 랭킹
@router.get("/rank/{followers}/{category}")
async def ranking_list(followers: str, category: str):

    response = controller.get_ranking(category, followers)

    return response


@router.get("/rank/search/user/{influencer_id}")
async def influencer_ranking(influencer_id: str):
    response = controller.get_influencer_ranking(influencer_id)

    return response


@router.get("/{influencer_id}")
async def detailed_info(influencer_id: str):
    response = controller.get_detailed_info(influencer_id)

    return response


@router.get("/rank/golf")
async def category_list_golf():

    response = controller.get_category_list("3")

    return response


@router.get("/rank/light")
async def category_list():
    response = controller.get_category_list("2")

    return response


@router.get("/search/user/{influencer_id}")
async def user_data(influencer_id: str):
    response = controller.get_user_data(influencer_id)

    return response


@router.get("/search/{keyword}")
async def find_keyword(keyword: str):
    response = controller.find_keyword_list(keyword)

    return response
