from sqlalchemy import desc, extract

from .base_handler import BaseHandler
from .schema import BLCountRecord
from common.time import now


class BLFollowerHandler(BaseHandler):

    def insert_latest_count(self, count, vmid):
        record_obj = BLCountRecord(follower_number=count, vmid=vmid)
        self._session.add(record_obj)
        self._session.flush()
        return record_obj

    def get_latest_count(self, vmid):
        return self._session.query(BLCountRecord).filter(BLCountRecord.vmid == vmid)\
            .order_by(desc(BLCountRecord.record_time)).first()

    def get_yesterday_data(self, vmid):
        return self._session.query(BLCountRecord)\
            .filter(extract('day', BLCountRecord.record_time) == now().day - 1, BLCountRecord.vmid == vmid)\
            .order_by(desc(BLCountRecord.record_time))\
            .first()

    def list_all_data(self, vmid):
        return self._session.query(BLCountRecord).filter(BLCountRecord.vmid == vmid).all()

    def list_recent(self, vmid, number=10):
        return self._session.query(BLCountRecord).filter(BLCountRecord.vmid == vmid)\
            .order_by(desc(BLCountRecord.record_time)).limit(number)
