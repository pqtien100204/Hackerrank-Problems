import textwrap

def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

print(wrap("absujfudfifsuishiugiskjgrf", 5))
print(len("absujfudfifsuishiugiskjgrf"))