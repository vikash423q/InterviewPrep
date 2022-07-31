from typing import List

#   https://leetcode.com/problems/encode-and-decode-strings


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "#F@F#".join([s for s in strs])

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return [ss for ss in s.split("#F@F#")]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
