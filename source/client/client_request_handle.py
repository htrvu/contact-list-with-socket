
from common.request import RequestType

def create_block_request(block_id):
    return {
        'dtype': RequestType.BLOCK,
        'block_id': block_id
    }

def create_single_id_request(id):
    return {
        'dtype': RequestType.SINGLE_ID,
        'block_id': id
    }
