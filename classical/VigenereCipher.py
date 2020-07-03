letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
def encrypt(plain_text, key):
    cipher_text = []
    key_index=0
    for i in plain_text:
        num=letter.find(i)
        if(num!=-1):
            num += letter.find(key[key_index])
            num %= len(letter)
            cipher_text.append(letter[num])
            
            
            key_index+=1
            if key_index==len(key):
                key_index=0
        else:
            cipher_text.append(i)
        
    return("" . join(cipher_text)) 
    
def decrypt(cipher_text, key): 
    plain_text = []
    key_index=0
    for i in cipher_text:
        num=letter.find(i)
        if(num!=-1):
            num -= letter.find(key[key_index])
            num %= len(letter)
            plain_text.append(letter[num])
            key_index+=1
            if key_index==len(key):
                key_index=0
        else:
            plain_text.append(i)
        
    return("" . join(plain_text)) 

if __name__ == "__main__":
    print(encrypt("COMPUTERSCIENCE","TEST"))
    print(decrypt("VSEINXWKLGAXGGW","TEST"))
