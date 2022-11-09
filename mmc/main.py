def is_primo(numero):
    n_divisores=0
    
    for i in range(1,numero+1):
        if numero%i==0:
            n_divisores+=1
    return n_divisores==2


def primo_posicao(posicao):
    primo = 2
    cont = 1
    
    while cont<posicao:
        primo+=1
        if is_primo(primo):
            cont+=1
        
    
    return primo

def calcular_mmc(n1,n2):
    pos = 1
    mmc = 1
    while n1!=1 or n2!=1:
        primo = primo_posicao(pos)
        
        while n1%primo==0 or n2%primo==0:
            mmc = mmc*primo
            
            if n1%primo==0:
                n1 = int(n1/primo)
                
            if n2%primo==0:
                n2 = int(n2/primo)
            pos +=1
    return mmc
            

print(calcular_mmc(16,8))