from typing import ChainMap, List


def my_sol(logs: List[str]) -> List[str]:
    character_log = list(filter(lambda log: log.split(" ")[1].isalpha(), logs))
    number_log = list(filter(lambda log: log.split(" ")[1].isdecimal(), logs))

    character_log.sort(key=lambda log: log.split(" ")[0])
    character_log.sort(key=lambda log: log.split(" ")[1:])

    return character_log + number_log


def sol1(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda log: (log.split()[1:], log.split()[0]))

    return letters + digits
