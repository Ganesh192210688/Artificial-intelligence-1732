import itertools

def solve_cryptarithm(words, result):
    letters = set(''.join(words) + result)
    assert len(letters) <= 10, "Too many unique letters" 

    for perm in itertools.permutations('0123456789', len(letters)):
        table = str.maketrans(''.join(letters), ''.join(perm))
        
        translated_words = [word.translate(table) for word in words]
        translated_result = result.translate(table)
        
        if any(word[0] == '0' for word in translated_words + [translated_result]):
            continue 
        
        if sum(map(int, translated_words)) == int(translated_result):
            return {letter: digit for letter, digit in zip(letters, perm)}

    return None

# Example usage:
words = ['SCOOBY', 'DOOO']
result = 'BLINKS'

solution = solve_cryptarithm(words, result)
if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter} -> {digit}")
else:
    print("No solution found")

OUTPUT:
Solution found:
L -> 0
D -> 5
N -> 3
K -> 4
Y -> 1
C -> 9
O -> 6
S -> 7
B -> 8
I -> 2
