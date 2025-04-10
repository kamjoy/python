from stacks import Stack

my_stack = Stack()

print("""
     Welcome to the word reversal program.
     Please type a word followed by Enter or type
     999 to quit.
      """)

while True:
    random_word = input("Enter a word: ")
    my_stack.push(random_word)

    if random_word:
        random_word = my_stack.pop()
        print(f"{random_word} : {random_word}")
    
    if random_word == "999":
        print("Quitting program")
        break

print("""
 Welcome to the word reversal program.
 Please type a word followed by Enter or type
 999 to quit.
      """)
