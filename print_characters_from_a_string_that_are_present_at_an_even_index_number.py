# Print characters from a string that are present at an even index number

def display_even_index_chars():
    user_string = input("String Entry:")
    print("Characters at Even Index: ", end="")
    for i in range(len(user_string)):
        if i % 2 == 0:
            print(user_string[i], end="")
        print()

display_even_index_chars()