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
    
    alphanumerics = ['zero','one','two','three','four','five','six','seven','eight','nine','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for n in range(7, 8):
        if n == 0:
            continue

        for perm in permutations(alphanumerics, n):
            autogram = []

            sentence = f"The SHA256 for this sentence begins with: {', '.join(perm[:-1])} and {''.join(perm[-1:])}."
            sentence_hash = hashlib.sha256(sentence.encode('utf-8')).hexdigest()

            for digit in perm:
                if digit in numbers_dict.keys():
                    autogram.append(numbers_dict[digit])
                else:
                    autogram.append(digit)

            if (''.join(autogram) == sentence_hash[:len(autogram)]):
                print(sentence)
                print(sentence_hash)

    '''
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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
                                sentence_hash = hashlib.sha256(sentence.encode('utf-8')).hexdigest()
                                
                                if (autogram == sentence_hash[:7]):
                                    print(sentence)
                                    print(sentence_hash)
    '''

if __name__ == '__main__':
    Autogram_SHA256SUM()
