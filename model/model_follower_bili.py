from .base_model import ModelBase
from common.third_party_requests import get_data
from common.time import now
from database.bili_follower_handler import BLFollowerHandler


class ModelBLFollower(ModelBase):

    def __init__(self):
        self._meta_store = BLFollowerHandler()
        ModelBLFollower.counter = 0

    def connect(self):
        self._meta_store.connect()

    def disconnect(self, is_error=False):
        self._meta_store.disconnect()

    def generate_latest_count(self, vmid, record=False):
        data = get_data(vmid)
        followers_count = data['data']['follower']

        if record:
            return self._meta_store.insert_latest_count(count=followers_count).json
        else:
            return {
                "bili_follower_number": followers_count,
                "bili_record_time": now().strftime("%Y年%m月%d日 %H:%M:%S")
            }

    def get_latest_count(self, vmid):
        return self._meta_store.get_latest_count(vmid=vmid).json

    def get_yesterday_data(self, vmid):
        obj_record = self._meta_store.get_yesterday_data(vmid=vmid)
        if obj_record is None:
            print("No yesterday data")
            return {}
        return self._meta_store.get_yesterday_data(vmid=vmid).json

    def list_all_data(self, vmid):
        objs = self._meta_store.list_all_data(vmid=vmid)

        time_slots = [obj.record_time for obj in objs]
        followers = [obj.follower_number for obj in objs]
        return time_slots, followers

    def list_recent(self, number, vmid):
        objs = self._meta_store.list_recent(number=number, vmid=vmid)
        objs = [obj.json for obj in objs]

        # normalize data
        minimum = 10_000_000
        for obj in objs:
            minimum = min(obj['bili_follower_number'], minimum)
        for obj in objs:
            obj['bili_follower_number'] -= (minimum - 20)
        objs = list(reversed(objs))

        return objs
