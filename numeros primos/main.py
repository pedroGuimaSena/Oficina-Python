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



print(primo_posicao(3))