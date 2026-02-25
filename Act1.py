import time

print("Greetings! Let us consult the great works of the Bard...")
time.sleep(1.5) 
print("Reading through the ancient texts. Pray, give me but a moment...\n")

line_count = 0

with open('t8.shakespeare.txt', 'r') as file:
    for line in file:
        line_count += 1

print("Huzzah! The counting is complete.")
print(f"By my troth, Shakespeare's total number of lines be exactly: {line_count}")