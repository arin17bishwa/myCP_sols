from typing import List


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        def get_new_node() -> dict[str, tuple[int, dict]]:
            return dict()

        trie = get_new_node()
        smallest_word_idx: int = 0

        def add(s: str, idx: int):
            nonlocal trie, smallest_word_idx
            node = trie

            if len(wordsContainer[smallest_word_idx]) > len(s):
                smallest_word_idx = idx

            for ch in s:
                if ch not in node:
                    node[ch] = (idx, get_new_node())
                else:
                    prev_idx = node[ch][0]

                    if len(wordsContainer[prev_idx]) > len(s):
                        node[ch] = (idx, node[ch][1])
                    elif len(wordsContainer[prev_idx]) == len(s):
                        node[ch] = (min(node[ch][0], idx), node[ch][1])
                node = node[ch][1]
            return

        def calculate_nearest(s: str) -> int:
            nonlocal trie, smallest_word_idx

            node = trie
            prev = smallest_word_idx
            for ch in s:
                if ch not in node:
                    return prev
                else:
                    prev = node[ch][0]
                    node = node[ch][1]
            return prev

        for _idx, word in enumerate(wordsContainer):
            add(word[::-1], _idx)

        return [calculate_nearest(word[::-1]) for word in wordsQuery]


def main():
    obj = Solution()

    l1 = ["dggjjdvdb", "dgdjvjjg"]
    l2 = [
        "bdddv",
        "bbggdbvv",
        "vdvvv",
        "djgvb",
        "dbdgjddd",
        "vvjbd",
        "bdjdjjvb",
        "gdbvjdbdvb",
        "jvvgbbb",
        "vgvbd",
        "gbjjbb",
        "dvvgvjd",
        "gdgbddgjd",
        "vvjbgdbjdv",
        "vdbjbgbd",
    ]

    ans = obj.stringIndices(l1, l2)

    print(ans)


if __name__ == "__main__":
    main()
