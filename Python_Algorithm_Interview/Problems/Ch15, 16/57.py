from typing import List
import collections


class TrieNode:
    def __init__(self) -> None:
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def insert(self, index: int, word: str) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0 : len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index, word: str) -> bool:
        result = []
        node = self.root

        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


class Solution:
    def my_sol(self, words: List[str]) -> List[List[int]]:
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue

                temp = words[i] + words[j]
                if temp == temp[::-1]:
                    result.append([i, j])

        return result

    def sol2(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        result = []
        for i, word in enumerate(words):
            result.extend(trie.search(i, word))

        return result
