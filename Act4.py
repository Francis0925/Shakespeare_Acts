import time

Str = ''

print("Hark! Please wait while I unfurl the scroll...")
time.sleep(1)

with open("t8.shakespeare.txt", 'r', encoding='utf-8') as f_var:

    Str = Str + f_var.read().lower()

def replaceSymbol(text_string):

    symbols_and_numbers = "\n\r\t,:;.~|_@?!\"'+=^#&$()[]{}<>*-0123456789"
    
    for char in symbols_and_numbers:
        text_string = text_string.replace(char, ' ')
        
    return text_string

def strToList(text_string):
  
    new_list = text_string.split() 
    return new_list

print("Banishing all numbers and symbols to the void...")
time.sleep(1)
Str = replaceSymbol(Str)

print("Slicing the text into individual words...")
new_list = strToList(Str)
new_dictionary = {}

print("Tallying the words... I beg thy patience!")
time.sleep(1)

for mem in new_list:
    new_dictionary.setdefault(mem, 0)
    new_dictionary[mem] = new_dictionary[mem] + 1

alphabetically_sorted_list = sorted(new_dictionary)

print('\n-------- Sort Alphabetically --------')
time.sleep(1)

for mem in alphabetically_sorted_list: 
    print(f'{mem} : {new_dictionary[mem]}')

print('\n-------- Final Tally --------')
time.sleep(1)

total_unique_words = len(new_dictionary)

print(f"Behold! The Bard hath penned exactly {total_unique_words} unique words in this great tome!")