from flask import Blueprint, request, jsonify

from common.tools import get_request_params
from constants import DEFAULT_VMID
from model.model_follower_bili import ModelBLFollower

bili_follower = Blueprint('bilibili', __name__)


@bili_follower.route('/generate', methods=['POST'])
def generate_latest_count():
    params = get_request_params()
    is_record = params.get('is_record', False)
    vmid = params.get('vmid', DEFAULT_VMID)

    meta_store = ModelBLFollower()
    with meta_store:
        count = meta_store.generate_latest_count(vmid=vmid, record=is_record)
        return count


@bili_follower.route('/latest', methods=['GET'])
def get_latest_count():
    params = get_request_params()
    vmid = params.get('vmid', DEFAULT_VMID)

    meta_store = ModelBLFollower()
    with meta_store:
        count = meta_store.get_latest_count(vmid=vmid)
        return count


@bili_follower.route('/yesterday', methods=['GET'])
def get_yesterday():
    params = get_request_params()
    vmid = params.get('vmid', DEFAULT_VMID)

    meta_store = ModelBLFollower()
    with meta_store:
        return meta_store.get_yesterday_data(vmid=vmid)


@bili_follower.route('/all', methods=['GET'])
def list_all_data():
    params = get_request_params()
    vmid = params.get('vmid', DEFAULT_VMID)

    meta_store = ModelBLFollower()
    with meta_store:
        time_slots, followers = meta_store.list_all_data(vmid=vmid)
        return {
            'time_slots': time_slots,
            'followers': followers
        }


@bili_follower.route('/recent', methods=['GET'])
def list_recent():
    params = get_request_params()
    number = params.get('number', 10)
    vmid = params.get('vmid', DEFAULT_VMID)

    meta_store = ModelBLFollower()
    with meta_store:
        data = meta_store.list_recent(number=number, vmid=vmid)
        return jsonify(data)
