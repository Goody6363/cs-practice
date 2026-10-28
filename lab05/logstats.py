
LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("Некорректная строка журнала")

    time, level, message = parts

    if level not in LEVELS:
        raise ValueError("Неизвестный уровень журнала")

    if not time or not message:
        raise ValueError("Некорректная строка журнала")

    return {
        "time": time,
        "level": level,
        "message": message
    }


def count_levels(lines: list[str]) -> dict:
    counts = {}
    
    for line in lines:
        if not line.strip():
            continue
        
        try:
            event = parse_event(line)
            level = event["level"]
        except ValueError:
            level = "BROKEN"
            
        counts[level] = counts.get(level, 0) + 1
    
    return counts


def top_errors(lines: list[str], n: int) -> list[list]:
    errors = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            continue

        if event["level"] == "ERROR":
            message = event["message"]
            errors[message] = errors.get(message, 0) + 1

    result = [[message, count] for message, count in errors.items()]
    result.sort(key=lambda item: (-item[1], item[0]))

    return result[:max(0, n)]


def format_report(counts: dict, errors: list[list]) -> str:
    report = ["Отчёт по журналу", ""]

    for level in sorted(counts):
        report.append(f"{level}: {counts[level]}")

    report.extend(["", "Частые ошибки:"])

    for message, count in errors:
        report.append(f"- {message} — {count}")

    return "\n".join(report) + "\n"