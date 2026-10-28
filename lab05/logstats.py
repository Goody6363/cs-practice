
LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    """Разбирает строку журнала и возвращает словарь."""
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
    """Подсчитывает количество строк каждого уровня."""
    counts = {
        "BROKEN": 0,
        "DEBUG": 0,
        "ERROR": 0,
        "INFO": 0,
        "WARNING": 0
    }

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1

    return counts


def top_errors(lines: list[str], n: int) -> list[list]:
    """Возвращает n самых частых сообщений уровня ERROR."""
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
    """Формирует текстовый отчёт."""
    report = ["Отчёт по журналу", ""]

    for level in sorted(counts):
        report.append(f"{level}: {counts[level]}")

    report.extend(["", "Частые ошибки:"])

    for message, count in errors:
        report.append(f"- {message} — {count}")

    return "\n".join(report) + "\n"