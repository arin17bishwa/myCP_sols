from collections import Counter
from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        word_counter = Counter()
        for msg, sender in zip(messages, senders):
            word_counter[sender] += msg.count(" ") + 1
        mx = max(word_counter.values())

        return max(sender for sender, cnt in word_counter.items() if cnt == mx)
