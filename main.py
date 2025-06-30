import sys
from stats import get_number_of_words, count_characters, sort_a_dict

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

else:
    path_to_book = sys.argv[1]

def main():
    word_count = get_number_of_words(path_to_book)

    print(f"""============ BOOKBOT ============
Analyzing book found at {path_to_book}... 
--------------Word Count -----------------
Found {word_count} total words
-------------Character Count--------------""")

    character_count = count_characters(path_to_book)
    sorted_list = sort_a_dict(character_count)
    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
    print("-------------END---------------")


main()

