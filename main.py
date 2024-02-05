alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphaReverse = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
inputText = input("Please enter the message you wish to decode:\n").lower()
exitText = ""

def reverseDecoder(inputText):
    outputText = ""
    for char in inputText:
        if inputText == "end":
            print("Goodbye.")
            break
        elif char in alpha:
            alphaReverseIndex = alphaReverse.index(char)
            alphaChar = alpha[alphaReverseIndex]
            outputText += alphaChar
        else:
            outputText += char
    print(outputText)

while exitText != "end":
    reverseDecoder(inputText)
    exitText = input("Enter next message to decode. Type 'end' to stop.\n").lower()
    reverseDecoder(exitText)