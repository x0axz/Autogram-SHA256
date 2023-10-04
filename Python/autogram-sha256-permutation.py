import hashlib
from itertools import permutations

def Autogram_SHA256SUM():
    
    numbers_dict = {"zero":"0",
                    "one":"1",
                    "two":"2",
                    "three":"3",
                    "four":"4",
                    "five":"5",
                    "six":"6",
                    "seven":"7",
                    "eight":"8",
                    "nine":"9"}
    
    hexdecimal = {"zero","one","two","three","four","five","six","seven","eight","nine","a","b","c","d","e","f"}
    
    for n in range(7, 8):
        if n == 0:
            continue

        for perm in permutations(hexdecimal, n):
            autogram = []

            sentence = f"The SHA256 for this sentence begins with: {', '.join(perm[:-1])} and {''.join(perm[-1:])}."
            
            # Encode the sentence as bytes using UTF-8 encoding
            sentence_encoded = sentence.encode('utf-8')

            # Create a SHA-256 hash object
            hash_value = hashlib.sha256(sentence_encoded)

            # Get the hexadecimal representation of the hash
            sentence_hash = hash_value.hexdigest()

            for digit in perm:
                if digit in numbers_dict.keys():
                    autogram.append(numbers_dict[digit])
                else:
                    autogram.append(digit)

            if (''.join(autogram) == sentence_hash[:len(autogram)]):
                print(sentence)
                print(sentence_hash)


if __name__ == '__main__':
    Autogram_SHA256SUM()
