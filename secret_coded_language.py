def encoded_msg(message) :
    words = message.split() 

    def single_word(word):
            
             if not word or word.isspace():
                return word
            
             if len(word) == 1:
                return (hex(ord(word))[2:]).upper()
            

             mid = len(word) // 2
             first_half = word[:mid]
             second_half = word[mid:]
    

             reversed_1 = first_half[::-1]
             reversed_2 = second_half[::-1]
             combined = reversed_1 + reversed_2
             
             result = []
             for i , char in enumerate(combined) :
                if i%2==0:
                    final_value = (hex(ord(char))[2:]).upper()
                    result.append(final_value)
                else:
                    result.append(char)

             return''.join(result)
    
    
    return ' '.join(single_word(word) for word in words)



message = input("Enter your message: ")
original = message
print(f"Your original message is: {original}")
encoded = encoded_msg(message)
print(f"Encoded message is: {encoded} ")