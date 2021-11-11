from typing import List


def my_sol(logs: List[str]) -> List[str]:
    letter_logs = []
    number_logs = []

    for log in logs:  # divide logs into letter_logs and number_logs
        log_list = log.split(" ")
        if log_list[1].isdecimal():
            number_logs.append(log)
        else:
            letter_logs.append(log)

    # sort letter_logs
    letter_logs.sort(key=lambda log: log[: log.find(" ")])
    letter_logs.sort(key=lambda log: log[log.find(" ") :])

    return letter_logs + number_logs
