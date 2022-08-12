from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CategoryTable(Base):
    __tablename__ = 'Category'
    CategoryID = Column(Integer, primary_key=True)
    Category = Column(String(58))

    def __repr__(self):
        return f"<Category {self.Category}"


class KeywordTable(Base):
    __tablename__ = 'Keyword'
    KeywordID = Column(Integer, primary_key=True)
    Keyword = Column(String(58))
    CategoryID = Column(Integer, ForeignKey('CategoryTable.CategoryID'))

    def __repr__(self):
        return f"<Keyword {self.Keyword}"


class RawInfoTable(Base):
    __tablename__ = 'RawInfo'
    Username = Column(String(58), primary_key=True)
    Followers = Column(Integer)
    Avg_Likes = Column(Float)
    Avg_Comments = Column(Float)
    KeywordID = Column(Integer, ForeignKey('KeywordTable.KeywordID'))
    CategoryID = Column(Integer, ForeignKey('CategoryTable.CategoryID'))

    def __repr__(self):
        return f"<Username {self.Username}"


class ProcessedInfoTable(Base):
    __tablename__ = 'ProcessedInfo'
    Username = Column(String(58), primary_key=True)
    Real_Followers = Column(Integer)
    Real_Like_Rate = Column(Float)
    Real_Comment_Rate = Column(Float)
    Real_Influence = Column(Integer)
    Real_Reach = Column(Integer)
    KeywordID = Column(Integer, ForeignKey('KeywordTable.KeywordID'))
    CategoryID = Column(Integer, ForeignKey('CategoryTable.CategoryID'))

    def __repr__(self):
        return f"<Username {self.Username}"


class attentionTable(Base):
    __tablename__ = 'attention'
    # target table name inside the accessed db
    influencer_id = Column(String(100), primary_key=True)
    followers = Column(Integer, nullable=False)
    real_influence = Column(Integer)

    #    choices = relationship('choice', back_populates='test')

    def __repr__(self):
        return f"<Influencer {self.influencer_id}"

class dummyTable(Base):
    __tablename__ = 'dummy'

    date_time = Column(String(20), primary_key = True)
    influence = Column(Integer)
