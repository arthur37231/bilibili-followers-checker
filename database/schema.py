from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import BIGINT, TIMESTAMP, TEXT
from common.time import now

Base = declarative_base()


def generate_time():
    """Return a function"""
    return now


class BLCountRecord(Base):
    __tablename__ = 'BLCountRecord'

    count_id = Column(BIGINT, primary_key=True, autoincrement=True)
    record_time = Column(TIMESTAMP, nullable=False, default=generate_time())
    follower_number = Column(BIGINT, nullable=False)
    vmid = Column(TEXT, nullable=False)

    @property
    def json(self):
        return {
            'bili_count_id': self.count_id,
            'bili_vmid': self.vmid,
            'bili_record_time': self.record_time.strftime("%Y年%m月%d日 %H:%M:%S"),
            'bili_follower_number': self.follower_number
        }
