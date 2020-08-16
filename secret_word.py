from collections import Counter
import string


class SecretWord:
    def __init__(self):
        self.alpha_dict = dict.fromkeys(string.ascii_lowercase, None)
        self.character_count = 0

    def find_secret_word(self, input_word, key_value_set):
        """
        :param input_word: Given input word "load"
        :param key_value_set: key pair "{(app,lol),(odd,itt)}"
        :return: secret word
        """
        if input_word is None or len(input_word) == 0:
            return None

        while self.character_count != len(input_word):
            for key_value in key_value_set:
                match_list = self.check_mutual_characters_matching(key_value[0], key_value[1])
                for match in match_list:
                    self.update_alpha_dictionary(match, key_value_set, input_word)

        secret_key = ""
        for ch in input_word:
            secret_key = secret_key + self.alpha_dict[ch] if self.alpha_dict[ch] is not None else ""
        return secret_key

    def check_mutual_characters_matching(self, word_str, key_str):
        """
        Method to find the secret key
        :param word_str:
        :param key_str:
        :return:
        """
        c1 = Counter(word_str)
        c2 = Counter(key_str)

        for key, val in self.alpha_dict.items():
            if (val is not None) and (key in c1):
                del c1[key]
                del c2[val]

        char, key = None, None
        if len(c1) == 1 and len(c2) == 1:
            for ch in c1:
                char = ch
                break
            for ch in c2:
                key = ch
                break
            return [[char, key]]
        return self.find_hidden_patterns(word_str, key_str)

    @staticmethod
    def find_hidden_patterns(word_str, key_str):
        """
        Finds the hidden pattern of key value pairs which has more combination
        :param word_str:
        :param key_str:
        :return:
        """
        c1 = Counter(word_str)
        c2 = Counter(key_str)
        c1 = c1.most_common()
        c2 = c2.most_common()
        i = 0
        result = []
        while i < len(c1) - 1:
            if c1[i][1] != c1[i + 1][1]:
                result.append([c1[i][0], c2[i][0]])
                i += 1
            else:
                i += 2
        return result

    def update_alpha_dictionary(self, match, key_value_set, input_word):
        """
        Update the alpha dictionary and other key value set
        :param match:
        :param key_value_set:
        :param input_word:
        :return:
        """
        if self.alpha_dict[match[0]] is None:
            self.alpha_dict[match[0]] = match[1]
            if match[0] in input_word:
                self.character_count += 1
        for key_val in key_value_set:
            key_val = list(key_val)
            key_val[0] = key_val[0].replace(match[0], '')
            key_val[1] = key_val[1].replace(match[1], '')
            key_val = tuple(key_val)


if __name__ == "__main__":
    word = "load"
    key_set = {("app", "lol"), ("old", "tip"), ("odd", "itt")}
    sw = SecretWord()
    print("Input word = {} \nSecret key = {}".format(word, sw.find_secret_word(word, key_set)))
