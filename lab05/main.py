
from logstats import count_levels, top_errors, format_report


def main():
    filename = input().strip()

    with open(filename, "r", encoding="utf-8") as log:
        counts = count_levels(log)

    with open(filename, "r", encoding="utf-8") as log:
        errors = top_errors(log, 5)

    print(sum(counts.values()))
    print(counts["ERROR"])
    print(counts["BROKEN"])

    report = format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as file:
        file.write(report)


if __name__ == "__main__":
    main()