import re


def print_res(hour, minute):
    res = str(hour)

    if minute_str:
        res += ':' + minute_str
    else:
        res += ':00'

    print(res)


if __name__ == '__main__':
    hour = None
    minute = None

    input_times = [
        '4pm',
        '7:38pm',
        '23:42',
        '3:16',
        '3:16am'
    ]

    parser_regex = r'([0-9]+)[:]?([0-9]+)?([AaPp][mM])?'

    for time in input_times:
        matches = re.match(parser_regex, time)

        hour_str = matches.group(1)
        minute_str = matches.group(2)
        am_pm = matches.group(3)
        hour = int(hour_str)

        if minute_str:
            minute = int(minute_str)

        am_pm_regex = r'([AaPp][mM])?'

        if am_pm and re.fullmatch(am_pm_regex, am_pm):
            hour += 12

        print_res(hour, minute)
