import json
import random

from fastapi import HTTPException

from testconn.models import RawInfoTable, CategoryTable, KeywordTable
from model.db_helper import db_helper

from controller import dto

query = db_helper()


def get_ranking(category, choice):
    all_filters = [RawInfoTable.Followers > 0]

    if choice == "nano":
        all_filters.append(RawInfoTable.Followers < 10000)
        all_filters.append(RawInfoTable.Followers >= 1000)
    if choice == "micro":
        all_filters.append(RawInfoTable.Followers < 50000)
        all_filters.append(RawInfoTable.Followers >= 10000)
    if choice == "mid":
        all_filters.append(RawInfoTable.Followers < 100000)
        all_filters.append(RawInfoTable.Followers >= 50000)
    if choice == "macro":
        all_filters.append(RawInfoTable.Followers < 500000)
        all_filters.append(RawInfoTable.Followers >= 100000)
    if choice == "mega":
        all_filters.append(RawInfoTable.Followers >= 500000)

    if category:
        all_filters.append(CategoryTable.Category.like('%' + category + '%'))

    influencers = query.ranking_query(all_filters)

    response = dto.to_json(influencers)

    if not response:
        raise HTTPException(status_code=202, detail="no data")

    return response


def get_influencer_ranking(influencer_id):
    influencer_list = query.influencer_rank_query()

    for influencer in influencer_list:
        if influencer[1] == influencer_id:
            response = dto.to_json(influencer)
            return response

    raise HTTPException(status_code=202, detail='Not found.')


def get_detailed_info(influencer_id):
    target_influencer = query.all_data_query(influencer_id)

    if not target_influencer:
        raise HTTPException(status_code=202, detail='No such influencer')

    response = dto.to_json(target_influencer)

    return response


def get_category_list(category):
    category_list = query.category_list_query(category)

    response = dto.to_json(category_list)

    return response


def get_user_data(influencer_id):
    influencer = query.user_query(influencer_id)

    if not influencer:
        raise HTTPException(status_code=202, detail='No such influencer')

    response = dto.to_json(influencer)

    return response


def find_keyword_list(keyword):
    keyword_list = query.keyword_list_query(keyword)

    if not keyword_list:
        raise HTTPException(status_code=202, detail='No such keyword')

    response = dto.to_json(keyword_list)

    return response


