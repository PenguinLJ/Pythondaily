"""
给你一个字符串数组words，只返回可以使用在美式键盘同一行的字母打印出来的单词。
键盘如下图所示。美式键盘中：
第一行由字符"qwertyuiop”组成。
第二行由字符“asdfghjkl"组成。
第三行由字符“zxcvbnm"组成。

输入：words=["Hello","Alaska","Dad","Peace"]
输出：["Alaska"，"Dad"]
输入：words=["omk"]
输出：[]
"""

words = ["Hello", "Alaska", "Dad", "Peace"]
words2=["omk"]
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']


def isinkeyboard(words, keyboard):
    out_word = []  # 存放符合要求的单词
    for w in words:
        lower_w = w.lower()  # 将待查找的单词转换为小写
        lower_w_set = set(lower_w)  # 将小写单词从列表形式转换为集合形式
        for line in keyboard:
            if lower_w_set - set(line) == set():
                out_word.append(w)

    return out_word


print(isinkeyboard(words, keyboard))
print(isinkeyboard(words2, keyboard))


# gpt的答案
'''def find_words(words):
    keyboard_rows = [
        set("qwertyuiop"),
        set("asdfghjkl"),
        set("zxcvbnm")
    ]

    result = []

    for word in words:
        lower_word = word.lower()
        in_same_row = True

        for row in keyboard_rows:
            if all(char in row for char in lower_word):
                result.append(word)
                break

    return result

# 示例用法
words1 = ["Hello", "Alaska", "Dad", "Peace"]
print(find_words(words1))  # 输出: ["Alaska", "Dad"]

words2 = ["omk"]
print(find_words(words2))'''  # 输出: []







