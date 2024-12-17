# NOTE Not solved. I'm probably making this way more complicated than it needs to be

from copy import copy


def test_decreasing(report: list[str]) -> bool:
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i + 1])
        if not 1 <= diff <= 3:
            return test_decreasing_removed(copy(report), i + 1)
    return True


def test_decreasing_removed(report: list[str], remove: int) -> bool:
    result1 = False
    if remove == 1:
        result1 = test_decreasing_removed(copy(report), 0)

    report.pop(remove)

    result2 = True
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i + 1])
        if not 1 <= diff <= 3:
            result2 = False

    return result1 or result2


def test_increasing(report: list[str]) -> bool:
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i + 1])
        if not -3 <= diff <= -1:
            return test_increasing_removed(copy(report), i + 1)
    return True


def test_increasing_removed(report: list[str], remove: int) -> bool:
    result1 = False
    if remove == 1:
        result1 = test_increasing_removed(copy(report), 0)

    report.pop(remove)

    result2 = True
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i + 1])
        if not -3 <= diff <= -1:
            result2 = False

    return result1 or result2


def validate_report(report: list[str]) -> bool:
    result1 = test_increasing(copy(report))
    result2 = test_decreasing(copy(report))
    return result1 or result2


def main():
    reports = []

    with open('input.txt', 'r') as input:
        for line in input:
            reports.append(line.split(' '))

    valid_reports = 0
    for report in reports:
        if validate_report(report):
            valid_reports += 1

    print(valid_reports)


if __name__ == '__main__':
    main()
