with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def text_to_lowered_characters(file_contents):
    lowered_text = ""
    lowered_text = file_contents.lower()
    return lowered_text

def text_to_count_characters_in_dictionary(text):
    dictionary ={}
    for char in text:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

def dictionary_to_report(dict): # function to sort the pre counted dictionary in descending order and creates a readable report for humans 
    sorted_dict = {}
    header = "--- Begin report of books/frankenstein.txt ---\n"
    print(f"{header}{count_words(file_contents)} words found in the document\n")
    sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True) if k.isalpha()} # sort method: sorts by key value and only if k is alphabetic
    for i in sorted_dict:
        print(f"The '{i}' character was found {sorted_dict[i]} times")
    print("--- End report ---")
    return sorted_dict

result_lower = text_to_lowered_characters(file_contents)
#print(result_lower)
result_character_count = text_to_count_characters_in_dictionary(result_lower)
#print(result_character_count)
pre = dictionary_to_report(result_character_count)
#print(pre)
