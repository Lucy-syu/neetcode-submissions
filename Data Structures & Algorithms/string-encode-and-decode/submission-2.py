class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for st in strs:
            encoded_string += st + "ñ"

        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_string = []
        temp = ""

        for i in range(len(s)):
            if s[i] == "ñ":
                decoded_string.append(temp)
                temp = ""
            else:
                temp += s[i]

        return decoded_string