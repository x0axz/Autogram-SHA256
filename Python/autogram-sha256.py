import hashlib
from itertools import permutations

def Autogram_SHA256SUM():

    numbers_dict = {'zero':'0',
                    'one':'1',
                    'two':'2',
                    'three':'3',
                    'four':'4',
                    'five':'5',
                    'six':'6',
                    'seven':'7',
                    'eight':'8',
                    'nine':'9'}
    
    hexdecimal = ['zero','one','two','three','four','five','six','seven','eight','nine','a','b','c','d','e','f']
    
    for n in range(7, 8):
        if n == 0:
            continue

        for perm in permutations(hexdecimal, n):
            autogram = []

            sentence = f"The SHA256 for this sentence begins with: {', '.join(perm[:-1])} and {''.join(perm[-1:])}."
            
            encoded_sentence = sentence.encode('utf-8')
            hash_value = hashlib.sha256(encoded_sentence)
            hexadecimal_hash = hash_value.hexdigest()

            for digit in perm:
                if digit in numbers_dict.keys():
                    autogram.append(numbers_dict[digit])
                else:
                    autogram.append(digit)

            if (''.join(autogram) == hexadecimal_hash[:len(autogram)]):
                print(sentence)
                print(hexadecimal_hash)

    '''
    alphabets = ['a','b','c','d','e','f']
    numbers_words = ['zero','one','two','three','four','five','six','seven','eight','nine']

    for a1 in alphabets:
        for a2 in alphabets:
            for n1 in numbers_words:
                for n2 in numbers_words:
                    for n3 in numbers_words:
                        for n4 in numbers_words:
                            for n5 in numbers_words:
                                
                                autogram = numbers_dict[n1] + numbers_dict[n2] + numbers_dict[n3] + a1 + numbers_dict[n4] + a2 + numbers_dict[n5]

                                sentence = f"The SHA256 for this sentence begins with: {n1}, {n2}, {n3}, {a1}, {n4}, {a2} and {n5}."
                                
                                encoded_sentence = sentence.encode('utf-8')
                                hash_value = hashlib.sha256(encoded_sentence)
                                hexadecimal_hash = hash_value.hexdigest()
                                
                                if (autogram == hexadecimal_hash[:7]):
                                    print(sentence)
                                    print(hexadecimal_hash)
    '''

if __name__ == '__main__':
    Autogram_SHA256SUM()
