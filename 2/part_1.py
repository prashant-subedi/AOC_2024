from parse_input import parse_input

def report_is_safe(report):
    direction = None
    for prev_level, level in zip(report, report[1:]):
        diff = prev_level - level
        if direction is None:
            direction = 1 if diff > 0 else -1

        if diff * direction <= 0:
            return False
        if  abs(diff) < 1 or abs(diff) > 3:
            return False
    return True

if __name__ == "__main__":

    safe_count = 0
    for report in parse_input():
        if report_is_safe(report):
            safe_count+=1

    print(safe_count)