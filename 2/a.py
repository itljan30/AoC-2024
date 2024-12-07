def test_decreasing(report: list[str]) -> bool:
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i + 1])
        if not 1 <= diff <= 3:
            return False
    return True


def test_increasing(report: list[str]) -> bool:
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i + 1])
        if not -3 <= diff <= -1:
            return False
    return True


def validate_report(report: list[str]) -> bool:
    if int(report[0]) - int(report[1]) < 0:
        return test_increasing(report)
    else:
        return test_decreasing(report)


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
