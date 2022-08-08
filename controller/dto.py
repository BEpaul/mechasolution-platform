from fastapi.encoders import jsonable_encoder


def to_json(raw_data):
    return jsonable_encoder(raw_data)
