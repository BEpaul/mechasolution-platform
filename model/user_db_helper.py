from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette import status

from testconn.feat_db_conn import engine_user_db_conn, engine_feat_db_conn
from testconn.models import attentionTable, keywordTable, rawInfoTable, processedInfoTable

feat_engine = engine_feat_db_conn()
feat_session = feat_engine.sessionmaker()

user_engine = engine_user_db_conn()
user_session = user_engine.sessionmaker()


class db_helper:
    def attention_list_query(self):
        attention_list = user_session.query(attentionTable).limit(100).all()

        return attention_list

    def post_attention_list(self, influencer_id):
        influencer = feat_session.query(
            keywordTable.Username,
            rawInfoTable.Followers,
            processedInfoTable.Real_Influence
        ).outerjoin(
            rawInfoTable,
            keywordTable.Username == rawInfoTable.Keyword_Username
        ).outerjoin(
            processedInfoTable,
            keywordTable.Username == processedInfoTable.RawInfo_Keyword_Username
        ).filter(keywordTable.Username == influencer_id).first()

        if not influencer:
            raise HTTPException(status_code=404, detail="No such influencer exist.")

        add_influencer = attentionTable(
            influencer_id=influencer.Username,
            followers=influencer.Followers,
            real_influence=influencer.Real_Influence
        )

        check_influencer = user_session.get(attentionTable, add_influencer.influencer_id)

        if check_influencer:
            raise HTTPException(status_code=404, detail="Already added.")

        user_session.add(add_influencer)

        try:
            user_session.commit()
        except:
            user_session.rollback()

    def delete_user(self, influencer_id):

        influencer = user_session.get(attentionTable, influencer_id)

        if not influencer:
            raise HTTPException(status_code=404, detail="Influencer not found")

        user_session.delete(influencer)

        try:
            user_session.commit()
        except:
            user_session.rollback()