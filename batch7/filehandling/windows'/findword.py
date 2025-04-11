def buffer_specific_words(file_path, keywords):
    buffer = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word.lower() in keywords:
                    buffer.append(word)

    return buffer

# Example usage
keywords = []
filename=str(input("Enter path of file or file name: "))
numofkey=str(input("How many keyword to add: "))
for x in numofkey:
    data=str(input("Enter your keyword to find: "))
    keywords.append(data)
buffered_words = buffer_specific_words(filename, keywords)

print("Buffered Words:", buffered_words)
