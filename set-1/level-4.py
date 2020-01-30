import string
most_common_letters = string.ascii_letters + " "
best_guesses = []
with open("4.txt", "r") as file:
    for hex_string in file.read().split("\n"):
        arr = []
        for i in range(0, len(hex_string), 2):
            arr.append(int(hex_string[i] + hex_string[i + 1], 16))
        answer = []
        strings = {}
        for i in range(32, 126):
            out_arr = []
            for j in arr:
                out_arr.append(i ^ j)
            strings[i] = "".join([chr(x) for x in out_arr])
            answer.append((sum([1 for x in out_arr if chr(x) in most_common_letters]), i))
        best_guesses.append(strings[max(answer)[1]])
answer = []
for guess in best_guesses:
    answer.append((sum([1 for x in guess if x in most_common_letters]), guess))
print(max(answer)[1])
