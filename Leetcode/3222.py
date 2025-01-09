class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        total_turns: int = min(x, y >> 2)
        return "Alice" if total_turns & 1 else "Bob"
