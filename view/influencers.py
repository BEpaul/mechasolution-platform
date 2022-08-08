from fastapi import APIRouter, Query
from controller import influencer_controller

from typing import Optional

router = APIRouter(
    prefix="/influencers",
    tags=['influencers']
)

controller = influencer_controller

# 리스트 랭킹
@router.get("/rank")
async def ranking_list(*,
                       keyword: Optional[str] = None,
                       category: Optional[str] = Query(
                           default="",
                           enum=["캠핑", "골프", "조명"]),
                       choice: str = Query(
                           default="all",
                           enum=["all", "nano", "micro", "mid", "macro", "mega"])):
    response = controller.get_ranking(keyword, category, choice)

    return response


@router.get("/rank/search/user/{influencer_id}")
async def influencer_ranking(influencer_id: str):
    response = controller.get_influencer_ranking(influencer_id)

    return response


@router.get("/rank/{category}")
async def category_list(category: str):
    response = controller.get_category_list(category)

    return response


@router.get("/{influencer_id}", tags=["detail"])
async def detailed_info(influencer_id: str):
    response = controller.get_detailed_info(influencer_id)

    return response


@router.get("/search/user/{influencer_id}")
async def user_data(influencer_id: str):
    response = controller.get_user_data(influencer_id)

    return response


@router.get("/search/{keyword}")
async def find_keyword(keyword: str):
    response = controller.find_keyword_list(keyword)

    return response

