def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")
count_words('example.txt')
