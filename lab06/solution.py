from typing import List, Dict

def count_by_extension(paths: List[str]) -> Dict[str, int]:
    result = {}
    for p in paths:
        ext = p.rsplit('.', 1)[-1].lower() if '.' in p else ""
        result[ext] = result.get(ext, 0) + 1
    return result

def deepest_path(paths: List[str]) -> str:
    if not paths:
        return ""

    return min(paths, key=lambda p: (-p.count('/'), p))

