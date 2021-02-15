from requests import get


request_url = 'http://api.bilibili.com/x/relation/stat'

def get_data(vmid):
    return get('%s?vmid=%s' % (request_url, vmid)).json()
