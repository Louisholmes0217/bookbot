def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_book_words(text)
    letters = get_book_letters(text)
    sorted_letters = sorted(letters, key=letters.get, reverse=True)
    print(f"-- Book report for: '{book_path}' --")
    print(f"This book has {words} words")
    for c in sorted_letters:
        print(f"The '{c}' character appeared {letters[c]} times")

def get_book_text(book_path):
    with open(book_path, "r") as f:
        return f.read()
    
def get_book_words(text):
    return len(text.split())

def get_book_letters(text):
    text = text.lower()
    letters = {}
    for c in text:
        if c.isalpha():
            if c not in letters.keys():
                letters[c] = 1
            else:
                letters[c] += 1
    return letters



main()