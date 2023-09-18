class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


def insert_word(root, word):
    current = root
    for char in word:
        if char not in current.children:
            current.children[char] = TrieNode()
        current = current.children[char]
    current.is_end_of_word = True


def find_review_score(review, prohibited_words):
    root = TrieNode()
    max_score = 0

    # Convert the review to lowercase for case-insensitive comparison
    review = review.lower()

    # Build the Trie using the prohibited words
    for word in prohibited_words:
        insert_word(root, word.lower())

    i = 0
    while i < len(review):
        current = root
        current_score = 0
        j = i

        while j < len(review) and review[j] in current.children:
            current = current.children[review[j]]
            if current.is_end_of_word:
                break
            current_score += 1
            j += 1

        if j == len(review) or review[j] not in current.children:
            max_score = max(max_score, current_score)

        i += 1

    return max_score


# Example usage
review = "FastDeliveryOkayProduct"
prohibited_words = ["eryoka", "yo", "eli"]
score = find_review_score(review, prohibited_words)
print("Review Score: ", score)


review = "GoodProductButScrapAfterWash"
prohibited_words = ["crap","odpro"]
score = find_review_score(review, prohibited_words)
print("Review Score: ", score)
