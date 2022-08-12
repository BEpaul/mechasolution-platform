from controller import dto
from model.user_db_helper import db_helper

query = db_helper()


def get_attention_list():
    attention_list = query.attention_list_query()

    return dto.to_json(attention_list)


def add_to_attention_list(influencer_id):
    query.post_attention_list(influencer_id)

    response = {
        "influencer_id": influencer_id + " is added to the attention list."
    }

    return dto.to_json(response)


def delete_user(influencer_id):
    query.delete_user(influencer_id)

    response = {
        "influencer_id": influencer_id + " is deleted from the attention list."
    }

    return dto.to_json(response)
