import sys

import re

if __name__ == '__main__':
    hour = None
    minute = None

    parser_regex = r'([0-9]+)[:]?([0-9]+)?([AaPp][mM])?'
    # input_time = sys.argv[1]
    input_time = '4:36'
    matches = re.match(parser_regex, input_time)

    print(matches.groups())

    print('Hour ' + str(hour))
    print('Minute ' + str(minute))
