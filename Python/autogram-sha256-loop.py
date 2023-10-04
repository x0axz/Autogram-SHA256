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

    alphabets = {"a","b","c","d","e","f"}
    numbers_words = {"zero","one","two","three","four","five","six","seven","eight","nine"}

    for a1 in alphabets:
        for a2 in alphabets:
            for n1 in numbers_words:
                for n2 in numbers_words:
                    for n3 in numbers_words:
                        for n4 in numbers_words:
                            for n5 in numbers_words:
                                
                                autogram = numbers_dict[n1] + numbers_dict[n2] + numbers_dict[n3] + a1 + numbers_dict[n4] + a2 + numbers_dict[n5]

                                sentence = f"The SHA256 for this sentence begins with: {n1}, {n2}, {n3}, {a1}, {n4}, {a2} and {n5}."
                                
                                # Encode the sentence as bytes using UTF-8 encoding
                                sentence_encoded = sentence.encode('utf-8')

                                # Create a SHA-256 hash object
                                hash_value = hashlib.sha256(sentence_encoded)

                                # Get the hexadecimal representation of the hash
                                sentence_hash = hash_value.hexdigest()
                                
                                if (autogram == sentence_hash[:7]):
                                    print(sentence)
                                    print(sentence_hash)


if __name__ == '__main__':
    Autogram_SHA256SUM()
