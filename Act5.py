import time

Str = ''

print("Hark! Please wait while I unfurl the scroll...")
time.sleep(1)

with open("t8.shakespeare.txt", 'r', encoding='utf-8') as f_var:
    # Adding .lower() ensures accurate counting and alphabetical sorting
    Str = Str + f_var.read().lower()

def replaceSymbol(text_string):
    symbols_and_numbers = "\n\r\t,:;.~|_@?!\"'()[]{}<>*-0123456789"
    
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

print("Inscribing the final counts into a new tome...")
time.sleep(1)

# --- NEW FILE WRITING SECTION ---
# Open (or create) "wordcount.txt" in 'w' (write) mode
with open("wordcount.txt", "w", encoding="utf-8") as out_file:
    for mem in alphabetically_sorted_list: 
        # Write the string to the file. 
        # \n is required at the end so each word gets its own line!
        out_file.write(f'{mem} : {new_dictionary[mem]}\n')

print("\nSuccess! Open 'wordcount.txt' to view the full alphabetical ledger.")