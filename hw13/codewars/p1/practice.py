import re
MORSE_CODE = {
    '.-': 'A',
    '-...': 'B',
    '-..': 'D',
    '-..-': 'X',
    '--..': 'Z',
    '--.': 'G',
    '..-.': 'F',
    '..': 'I',
    '.': 'E',
    '.--.': 'P',
    '.--': 'W',
    '-.-.': 'C',
    '-.-': 'K',
    '-..-.': '/',
}


def decode_morse(morse_code: str):
    words = morse_code.split('   ')
    
    decode_words = []
    for word in words:
        letters = word.split(' ')
        decode_letters = [(MORSE_CODE.get(letter, '')) for letter in letters]
        decode_words.append(''.join(decode_letters))    
    return ' '.join(decode_words)

print(decode_morse('.... . -.--   .--- ..- -.. .'))  # 'HEY JUDE'

