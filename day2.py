def generate_acronym(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

def main():
    user_input = input("Enter a phrase: ")
    acronym = generate_acronym(user_input)
    print(f"The acronym for '{user_input}' is: {acronym}")

if __name__ == "__main__":
    main()
