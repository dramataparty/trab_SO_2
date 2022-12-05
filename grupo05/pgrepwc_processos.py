### Grupo: SO-TI-05
### Aluno 1: Diogo Forte (fc56931)
### Aluno 2: Tiago Ramalho (fc58645)

import multiprocessing
import sys
import os
 # Mudanças a fazer :
 # remover a opçao "-t"
 #remover tudo pertinente a forks e meter multiprocessing.process
 #tentar não morrer
 #mudar a opçao "-e " para realizar o seguinte
 # -e k: opção que permite ativar o modo de paralelização especial, que agora funciona com múltiplos ficheiros. O parâmetro k
#define o número máximo de bytes que compõem um bloco de trabalho

#Garantir q os contadores funcionam corretamente
#Usar multiprocessing-process
#Ver guião mem. partilhada e seguintes
def main(Rword,Rfiles,Rc,Rl,Rpn,Re):
    linhas = []
    if Rc == True:
        ocorrencias = []           
    if Rl == True:                 
        nlinhas = []
    print('Programa: pgrepwc_processos.py')
    print('Argumentos: ',Rword,Rfiles,Rc,Rl,Rpn,Re)

#------------------------------------------------------------------------------------------

    def ler(Lword,Lfiles,Lc,Ll):
            for Lfile in Lfiles:
                with open(Lfile, 'r', encoding='utf_8') as file:
                    n = 0
                    nline = 0
                    lines = []
                    linhas = []
                    ocorrencias=[]
                    nlinhas=[]
                    for linha in file:
                        palavras = linha.split()
                        if Lword in palavras:                              
                            nline += 1                                      
                            lines = lines + [linha]                        
                            for palavra in palavras:                       
                                if palavra == Lword:
                                    n += 1
                    linhas = linhas + [lines]
                    if Lc == True:
                        ocorrencias = ocorrencias + [n]
                    if Ll == True:
                        nlinhas = nlinhas + [nline]
                    
   
    if Rpn == 1:                                   
            ler(Rword,Rfiles,Rc,Rl)
    else:
        ls = []                                   
        for _ in range(Rpn):                       
            ls = ls + [[]]                         
        nxt = 0                                    
        for f in Rfiles:                           
            ls[nxt] = ls[nxt] + [f]
            nxt = (nxt + 1) % Rpn
        for t in range(Rpn):
            newP = multiprocessing.Process(target = ler,args =(Rword,ls[t],Rc,Rl,))                  
            newP.start()
        for _ in range(Rpn):                                                        
            newP.join()
                
    for i2 in range(len(Rfiles)-1):
        i3 = i2 + 1
        print("o ficheiro nº " + str(i3) + " contem as seguintes linhas:")                                      
        print(linhas[i2])                                                                                    
        if Rc == True:                                                                                     
            print("o numero total de ocorrencias da palavra neste ficheiro foram " + str(ocorrencias[i2]))      
        if Rl == True:                                                                                     
            print("o numero total de linhas com esta palavra neste ficheiro foram " + str(nlinhas[i2]))



if __name__ == "__main__":
    tudo = list(sys.argv)
    c = False
    l = False
    pn = 1
    e = False
    pal = ""
    if "-c" in tudo:                                            
        c = True                                                
    if "-l" in tudo:                                            
        l = True                                                
    if "-p" in tudo:                                            
        for i in tudo:                                          
            if i == "-p":                                       
                pn = int(tudo[i+1])
    if "-e" in tudo:
        e = True
    ficheiros = []
    for x in tudo:                                              
        if ".txt" in x:
            ficheiros = ficheiros + x  
        for x1 in range(len(tudo)):
            if ".txt" in tudo[x1]:
                pal = tudo[x1-1]
    main(pal,ficheiros,c,l,pn,e)
