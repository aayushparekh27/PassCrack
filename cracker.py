import hashlib
import argparse
import itertools
import string

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def dictionary_attack(hashfile, wordlist):
    with open(hashfile, 'r') as hf:
        target_hash = hf.read().strip()
    with open(wordlist, 'r') as wf:
        for word in wf:
            word = word.strip()
            if hash_password(word) == target_hash:
                print(f"[+] Password found: {word}")
                return
    print("[-] Password not found.")

def brute_force(target_password, charset, max_length):
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess_word = ''.join(guess)
            if guess_word == target_password:
                print(f"[+] Password found: {guess_word}")
                return
    print("[-] Password not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['dict', 'brute'], required=True)
    parser.add_argument('--hashfile', help='File containing the hashed password')
    parser.add_argument('--wordlist', help='Path to dictionary file')
    parser.add_argument('--charset', help='Charset to use (letters, digits, etc.)')
    parser.add_argument('--length', type=int, help='Max length for brute force')
    parser.add_argument('--target', help='Target password for brute-force (plaintext)')

    args = parser.parse_args()

    if args.mode == 'dict':
        dictionary_attack(args.hashfile, args.wordlist)
    elif args.mode == 'brute':
        charsets = {
            "digits": string.digits,
            "letters": string.ascii_letters,
            "all": string.ascii_letters + string.digits + string.punctuation
        }
        charset = charsets.get(args.charset, string.digits)
        brute_force(args.target, charset, args.length)
