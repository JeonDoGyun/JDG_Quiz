# redis 활용 snapshot 저장 및 조회

from django.core.cache import cache
import json

SNAPSHOT_EXPIRE_SECONDS = 1800  # 30분은 임시로


def save_snapshot_to_cache(submission_id: str, snapshot: list[dict]):
    key = f"snapshot:{submission_id}"
    cache.set(key, json.dumps(snapshot), timeout=SNAPSHOT_EXPIRE_SECONDS)


def get_snapshot_from_cache(submission_id: str):
    key = f"snapshot:{submission_id}"
    data = cache.get(key)
    return json.loads(data) if data else None


def clear_snapshot_cache(submission_id: str):
    cache.delete(f"snapshot:{submission_id}")
