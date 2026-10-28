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

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size, unit_idx = n_bytes, 0
    while size >= 1024 and unit_idx < len(units) - 1:
        size, unit_idx = size / 1024, unit_idx + 1
    return f"{size:.1f} {units[unit_idx]}" if unit_idx > 0 else f"{int(size)} Б"
