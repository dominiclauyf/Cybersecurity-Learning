letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
def encrypt(plain_text, key):
    cipher_text = ""
    for i in plain_text:
        num=(letter.find(i)+key)%len(letter)
        cipher_text+=letter[num]
        
    return cipher_text
    
def decrypt(cipher_text, key): 
    plain_text = ""
    for i in cipher_text:
        num=(letter.find(i)-key)%len(letter)
        plain_text+=letter[num]
        
    return plain_text 

if __name__ == "__main__":
    print(encrypt("COMPUTERSCIENCE",3))
    print(decrypt("FRPSXWHUVFLHQFH",3))