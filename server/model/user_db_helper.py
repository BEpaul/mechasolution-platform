from fastapi import APIRouter, HTTPException

from testconn.feat_db_conn import engine_user_db_conn, engine_feat_db_conn
from testconn.models import attentionTable, CategoryTable, KeywordTable, RawInfoTable, ProcessedInfoTable

feat_engine = engine_feat_db_conn()
feat_session = feat_engine.sessionmaker()

user_engine = engine_user_db_conn()
user_session = user_engine.sessionmaker()


class db_helper:
    def attention_list_query(self):
        attention_list = user_session.query(
            attentionTable
        ).limit(10).all()

        return attention_list

    def post_attention_list(self, influencer_id):
        check_size = user_session.query(attentionTable).count() + 1

        print(check_size)

        if check_size >= 5:
            raise HTTPException(status_code=202, detail="Attention list is full.")

        influencer = feat_session.query(
            RawInfoTable.Username,
            CategoryTable.Category,
            RawInfoTable.Followers,
            ProcessedInfoTable.Real_Influence
        ).outerjoin(
            ProcessedInfoTable,
            RawInfoTable.Username == ProcessedInfoTable.Username
        ).outerjoin(
            CategoryTable,
            CategoryTable.CategoryID == RawInfoTable.CategoryID
        ).filter(RawInfoTable.Username == influencer_id).first()

        if not influencer:
            raise HTTPException(status_code=202, detail="No such influencer exist.")

        add_influencer = attentionTable(
            Influencer_id=influencer.Username,
            Category = influencer.Category,
            Followers=influencer.Followers,
            Real_Influence=influencer.Real_Influence
        )

        check_influencer = user_session.get(attentionTable, add_influencer.Influencer_id)

        if check_influencer:
            raise HTTPException(status_code=202, detail="Already added.")

        user_session.add(add_influencer)

        try:
            user_session.commit()
        except:
            user_session.rollback()

    def delete_user(self, Influencer_id):

        influencer = user_session.get(attentionTable, Influencer_id)

        if not influencer:
            raise HTTPException(status_code=202, detail="Influencer not found")

        user_session.delete(influencer)

        try:
            user_session.commit()
        except:
            user_session.rollback()
