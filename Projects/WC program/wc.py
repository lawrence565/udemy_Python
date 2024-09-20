from sys import argv
# This is the way we get terminal argument

if len(argv) < 2:
    print("Please provide a filename")
else:
    file = open(argv[1])
    lines = file.read() #資料輸入 lines

    lines = lines.split("\n") #把每行都拆開來
    if lines[-1] == "":
        lines.remove(lines[-1])    
    line_count = len(lines)
    word_count = 0
    char_count = 0
    for line in lines:
        words = line.split(" ")
        word_count += len(words)
        for word in words:
            char_count += len(word)



    print(f"The file has {line_count} lines.")
    print(f"The file has {word_count} words.")
    print(f"The file has {char_count} characters.")