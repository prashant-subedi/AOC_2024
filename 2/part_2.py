from parse_input import parse_input
from part_1 import report_is_safe

safe_count = 0
for report in parse_input():
    if report_is_safe(report):
        safe_count+=1
    else:
        for i in range(len(report)):
            if report_is_safe(report[:i] + report[i+1:]):
                safe_count+=1
                break

print(safe_count)

