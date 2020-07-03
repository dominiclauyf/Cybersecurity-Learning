def encrypt(data,key):
    result=''
    rail = [['_' for i in range(len(data))] 
                for j in range(key)] 
    down=True
    row=0
    for i in range(len(data)):
        
        rail[row][i]=data[i]
        if(row==key-1):
            down=False
        if(row==0):
            down=True 
        if(down):
            row+=1
        else:
            row-=1
    for i in range(len(rail)):
        for j in range(len(rail[0])):
            if(rail[i][j]!='_'):
                result+=rail[i][j]
    return result
        
    
def decrypt(data,key):
    result=''
    rail = [['_' for i in range(len(data))] 
                for j in range(key)] 
    down=True
    row=0
    for i in range(len(data)):
        
        rail[row][i]='*'
        if row==0 :
            down=True
        if row==key-1 :
            down=False
        if(down):
            row+=1
        else:
            row-=1
    index = 0
    for i in range(len(rail)):
        for j in range(len(rail[0])):
            if(rail[i][j]=='*'):
                rail[i][j]=data[index]
                index += 1
    row = 0
    for i in range(len(data)):
        result+=rail[row][i]
        if row == 0: 
            down = True
        if row == key-1: 
            down = False 
        if(down):
            row+=1
        else:
            row-=1
        
    return result

if __name__ == "__main__":
    print(encrypt("COMPUTER*SCIENCE",3))
    print(decrypt("CU*EOPTRSINEMECC",3))
