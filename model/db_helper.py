from sqlalchemy import func

from testconn.feat_db_conn import engine_user_db_conn, engine_feat_db_conn
from testconn.models import keywordTable, rawInfoTable, processedInfoTable

feat_engine = engine_feat_db_conn()
feat_session = feat_engine.sessionmaker()

user_engine = engine_user_db_conn()
user_session = user_engine.sessionmaker()


class db_helper:
    def ranking_query(self, all_filters):
        ranking = feat_session.query(
            func.rank().over(order_by=processedInfoTable.Real_Influence.desc()).label('Rank'),
            keywordTable.Username,
            keywordTable.Keyword,
            rawInfoTable.Followers,
            processedInfoTable.Real_Influence
        ).outerjoin(
            rawInfoTable,
            keywordTable.Username == rawInfoTable.Keyword_Username
        ).outerjoin(
            processedInfoTable,
            keywordTable.Username == processedInfoTable.RawInfo_Keyword_Username
        ).filter(*all_filters).all()

        return ranking

    def influencer_rank_query(self):
        infuencer_rank = feat_session.query(
            func.rank().over(order_by=processedInfoTable.Real_Influence.desc()).label('rank'),
            processedInfoTable.RawInfo_Keyword_Username
        ).all()

        return infuencer_rank

    def all_data_query(self, influencer_id):
        all_data = feat_session.query(
            rawInfoTable.Keyword_Username,
            rawInfoTable.Followers,
            rawInfoTable.Avg_Likes,
            processedInfoTable.Real_Followers,
            processedInfoTable.Real_Like_Rate,
            processedInfoTable.Real_Comment_Rate,
            processedInfoTable.Real_Influence
        ).outerjoin(
            processedInfoTable,
            processedInfoTable.RawInfo_Keyword_Username
            == rawInfoTable.Keyword_Username
        ).filter(rawInfoTable.Keyword_Username == influencer_id).first()

        return all_data

    def category_list_query(self, category):
        category_list = feat_session.query(
            keywordTable.Username,
            rawInfoTable.Followers,
            processedInfoTable.Real_Influence
        ).outerjoin(
            rawInfoTable,
            rawInfoTable.Keyword_Username == keywordTable.Username
        ).outerjoin(
            processedInfoTable,
            processedInfoTable.RawInfo_Keyword_Username == keywordTable.Username
        ).filter(keywordTable.Keyword.like("%"+category+"%")).order_by(
            processedInfoTable.Real_Influence.desc()
        ).limit(5).all()

        return category_list

    def user_query(self, influencer_id):
        user = feat_session.query(
            keywordTable.Username,
            rawInfoTable.Followers,
            processedInfoTable.Real_Influence
        ).outerjoin(
            rawInfoTable,
            rawInfoTable.Keyword_Username == keywordTable.Username
        ).outerjoin(
            processedInfoTable,
            processedInfoTable.RawInfo_Keyword_Username == keywordTable.Username
        ).filter(keywordTable.Username.like('%' + influencer_id + '%')).first()

        return user

    def keyword_list_query(self, keyword):
        keyword_list = feat_session.query(
            func.rank().over(order_by=processedInfoTable.Real_Influence.desc()).label('rank'),
            keywordTable.Username,
            rawInfoTable.Followers,
            processedInfoTable.Real_Influence
        ).outerjoin(
            rawInfoTable,
            rawInfoTable.Keyword_Username == keywordTable.Username
        ).outerjoin(
            processedInfoTable,
            processedInfoTable.RawInfo_Keyword_Username == keywordTable.Username
        ).filter(keywordTable.Keyword.like('%' + keyword + '%')).all()

        return keyword_list