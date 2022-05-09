from typing import List
import collections


def my_sol(strs: List[str]) -> List[List[str]]:
    result_dict = collections.defaultdict(list)

    for word in strs:
        key = tuple(sorted(collections.Counter(list(word)).items()))
        result_dict[key].append(word)

    return list(result_dict.values())


def sol1(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams["".join(sorted(word))].append(word)

    return list(anagrams.values())
