from typing import List, Dict

def count_by_extension(paths: List[str]) -> Dict[str, int]:
    counts = {}
    for path in paths:
        last_dot_index = path.rfind('.')
        if last_dot_index == -1 or last_dot_index == len(path) - 1:
            ext = ""
        else:
            ext = path[last_dot_index + 1:].lower()
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: List[str]) -> str:
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count('/'), p))


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size, unit_idx = n_bytes, 0
    while size >= 1024 and unit_idx < len(units) - 1:
        size /= 1024
        unit_idx += 1
    
    if unit_idx == 0:
        return f"{int(size)} Б"
    return f"{size:.1f} {units[unit_idx]}"
