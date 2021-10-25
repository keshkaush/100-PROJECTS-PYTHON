#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as data:
    names = data.readlines()
    for name in range(len(names)):
        names[name] = names[name].strip("\n")
    print(names)

with open("Input/Letters/starting_letter.txt") as letter_data:
    letter = letter_data.read()

for name in names:
    ready = letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_to_{name}", mode="w") as new_letter:
        new_letter.write(ready)

