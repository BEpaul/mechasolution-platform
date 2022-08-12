from sqlalchemy import func

from testconn.feat_db_conn import engine_user_db_conn, engine_feat_db_conn
from testconn.models import KeywordTable, RawInfoTable, ProcessedInfoTable, CategoryTable

feat_engine = engine_feat_db_conn()
feat_session = feat_engine.sessionmaker()

user_engine = engine_user_db_conn()
user_session = user_engine.sessionmaker()


class db_helper:
    def ranking_query(self, all_filters):
        ranking = feat_session.query(
            func.rank().over(order_by=ProcessedInfoTable.Real_Influence.desc()).label('Rank'),
            RawInfoTable.Username,
            CategoryTable.Category,
            RawInfoTable.Followers,
            ProcessedInfoTable.Real_Influence
        ).outerjoin(
            ProcessedInfoTable,
            ProcessedInfoTable.Username == RawInfoTable.Username
        ).outerjoin(
            CategoryTable,
            CategoryTable.CategoryID == RawInfoTable.CategoryID
        ).filter(*all_filters).limit(100).all()

        return ranking

    def influencer_rank_query(self):
        infuencer_rank = feat_session.query(
            func.rank().over(order_by=ProcessedInfoTable.Real_Influence.desc()).label('rank'),
            ProcessedInfoTable.Username
        ).all()

        return infuencer_rank

    def all_data_query(self, influencer_id):
        all_data = feat_session.query(
            RawInfoTable.Username,
            RawInfoTable.Followers,
            RawInfoTable.Avg_Likes,
            # ProcessedInfoTable.Real_Followers,
            # ProcessedInfoTable.Real_Like_Rate,
            # ProcessedInfoTable.Real_Comment_Rate,
            ProcessedInfoTable.Real_Influence
        ).outerjoin(
            ProcessedInfoTable,
            ProcessedInfoTable.Username == RawInfoTable.Username
        ).filter(RawInfoTable.Username == influencer_id).first()

        return all_data

    def category_list_query(self):

        category = str(feat_session.query(CategoryTable.CategoryID).order_by(func.rand()).limit(1).scalar())

        category_list = feat_session.query(
            CategoryTable.Category,
            RawInfoTable.Username,
            RawInfoTable.Followers,
            ProcessedInfoTable.Real_Influence
        ).outerjoin(
            ProcessedInfoTable,
            ProcessedInfoTable.Username == RawInfoTable.Username
        ).outerjoin(
            CategoryTable,
            CategoryTable.CategoryID == RawInfoTable.CategoryID
        ).filter(RawInfoTable.CategoryID == category).order_by(
            ProcessedInfoTable.Real_Influence.desc()
        ).limit(5).all()

        return category_list

    def user_query(self, influencer_id):
        user = feat_session.query(
            RawInfoTable.Username,
            RawInfoTable.Followers,
            ProcessedInfoTable.Real_Influence
        ).outerjoin(
            ProcessedInfoTable,
            ProcessedInfoTable.Username == RawInfoTable.Username
        ).filter(RawInfoTable.Username.like('%' + influencer_id + '%')).first()

        return user

    def keyword_list_query(self, keyword):
        keyword_list = feat_session.query(
            func.rank().over(order_by=ProcessedInfoTable.Real_Influence.desc()).label('rank'),
            RawInfoTable.Username,
            KeywordTable.Keyword,
            RawInfoTable.Followers,
            ProcessedInfoTable.Real_Influence
        ).outerjoin(
            ProcessedInfoTable,
            ProcessedInfoTable.Username == RawInfoTable.Username
        ).outerjoin(
            KeywordTable,
            KeywordTable.KeywordID == RawInfoTable.KeywordID
        ).filter(KeywordTable.Keyword.like('%' + keyword + '%')).limit(100).all()

        return keyword_list