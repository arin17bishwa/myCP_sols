from typing import List


def func(s: str, characters: List[str]) -> str:
    required_indices = [ord(i) - 97 for i in characters]
    curr_freq = [0] * 26

    def is_valid_substring():
        return all(curr_freq[i] > 0 for i in required_indices)

    def get_index(ch: str) -> int:
        return ord(ch) - 97

    n = len(s)
    mn_length = n
    start = 0
    ans_idx = [0, n - 1]
    for end in range(len(characters)):
        curr_freq[get_index(s[end])] += 1

    if is_valid_substring():
        return s[: len(characters)]

    for end in range(len(characters), n):
        curr_freq[get_index(s[end])] += 1
        while is_valid_substring():
            mn_length = min(mn_length, end - start + 1)
            if end - start + 1 < mn_length:
                ans_idx = [start, end]
                mn_length = end - start + 1
            curr_freq[get_index(s[start])] -= 1
            start += 1
    return s[ans_idx[0] : ans_idx[-1] + 1]


def main():
    s: str = "figehaeci"
    characters: List[str] = list("aei")
    ans = func(s, characters)
    print(ans)


if __name__ == "__main__":
    main()
