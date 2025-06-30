# where text is the file path
# returns the number of words in the text file

def get_number_of_words(file_path):
    with open(file_path) as f:
        text = f.read()
    count_of_words = text.split()
    return len(count_of_words)

def count_characters(file_path):
    with open(file_path) as f:
        text = f.read().lower()

        dict_of_characters = {}
        for character in text:
            dict_of_characters[character] = dict_of_characters.get(character, 0) + 1 
        return dict_of_characters

#sorts the amount of chars in a given dict in descending order
def sort_on(items):
    return items["num"]

def sort_a_dict (dict):
    list_to_sort = []
    for char in dict:
        if char.isalpha():
            num_of_chars = dict[char]

            current_dict = {"char":char, "num":num_of_chars}
            list_to_sort.append(current_dict)

    list_to_sort.sort(reverse=True, key=sort_on)
    return list_to_sort



    

     

    
    
    

            
        

        