text = input("Input text : ")
text = text.lower()
print('Reverse: ',text)
if text == text[::-1]:
    print("Output: Palindrome")
else:
    print("Output: Not a Palindrome")