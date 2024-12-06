from typing import List


# a - 97
# A - 65
# ord()
# chr()
# upper()
# isupper()
class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + "#" + s
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        curr_word_length_str = ""
        curr_word_length = 0
        curr_word = ""
        word_ended = False
        for char in s:
            if word_ended:
                curr_word += char
                curr_word_length -= 1
                if curr_word_length <= 0:
                    word_ended = False
                    ret.append(curr_word)
                    curr_word_length_str = ""
                    curr_word = ""
            else:
                if char != "#":
                    curr_word_length_str += char
                else:
                    word_ended = True
                    curr_word_length = int(curr_word_length_str)
                    if curr_word_length == 0:
                        ret.append("")
                        word_ended = False
                        curr_word_length_str = ""
        return ret

    def decode2(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            str_length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + str_length])
            i = j + 1 + str_length
        return res

    def encode3(self, strs: List[str]) -> str:
        if len(strs) == 1:
            if not strs[0]:  # case [""]
                return "'"
            else:
                return strs[0]  # case one word
        return "'".join(strs)

    def decode3(self, s: str) -> List[str]:
        if not s:
            return []
        if s == "'":
            return [""]

        ret = []
        word = ""
        for char in s:
            if char == "'":
                ret.append(word)
                word = ""
            else:
                word += char
        ret.append(word)
        return ret
