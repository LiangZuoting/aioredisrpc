from enum import Enum

REDIS_PREFIX = 'aioredisrpc:'


class Error(Enum):
    OK = 0
    UNKNOWN_REMOTE_CALL = 1
