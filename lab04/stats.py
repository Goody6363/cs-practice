def parse_record(line: str) -> dict:
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("Неверный формат строки")

    city = parts[0].strip()
    temp = parts[1].strip()
    date = parts[2].strip()

    if city == "" or date == "":
        raise ValueError("Город или дата пустые")

    temperature = float(temp)

    return {
        "city": city,
        "temperature": temperature,
        "date": date
    }


def read_valid(lines: list[str]) -> list[dict]:
    records = []

    for line in lines:
        if line.strip() == "":
            continue

        try:
            record = parse_record(line)
            records.append(record)
        except ValueError:
            continue

    return records


def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        temperature = record["temperature"]

        totals[city] = totals.get(city, 0) + temperature
        counts[city] = counts.get(city, 0) + 1

    averages = {}

    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)

    return averages


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)

    best_city = None

    for city in averages:
        if best_city is None:
            best_city = city
        elif averages[city] > averages[best_city]:
            best_city = city
        elif averages[city] == averages[best_city] and city < best_city:
            best_city = city

    return best_city