sesli = ['A','E','I','O','U']
def minion_game(string):
    # your code goes here
    l = substrings(s)
    l_puan = puan(l,s)
    for sayac in range(len(l)):
        sayac += 1
    kevin,stuart= o_puan(l,l_puan)
    
    
    if stuart > kevin:
        print("Stuart",stuart)
    elif kevin > stuart:
        print("Kevin",kevin)
    else:
        print("Draw")
        
def o_puan(l,l_puan):
    sayac = 0
    sonuc_k = 0
    sonuc_s = 0
    for st in l:
        if st[0] in sesli:
            sonuc_k += l_puan[sayac]
        else:
            sonuc_s += l_puan[sayac]
        sayac+=1
    return sonuc_k , sonuc_s
    
def puan(l,s):
    
    sayac = 0
    l_p =[]
    for st in l:
        st_len = len(st)
        point = 0
        sayac2 = 0
        sayac3 = sayac2 + st_len
        for sayac3 in range(len(s)):
            st2 = s[sayac2:sayac2+st_len]
            if len(st2) < len(st):
                break
            if st2 == st:
                point += 1
            sayac2 += 1
            sayac3 += sayac2 + st_len
        l_p.append(point)
        sayac += 1
    return l_p
    
def substrings(s):
    liste = []
    sayac1 = 0
    sayac2 = 0
    for sayac1 in range(len(s)+1):
        sayac2 = 0
        for sayac2 in range(len(s)+1):
            st = s[sayac1:sayac2]
            if sayac1 != sayac2 and st != '' and not(st in liste):
                liste.append(st)
            sayac2 += 1            
        sayac1 += 1
    
    return liste

if __name__ == '__main__':
    s = input()
    minion_game(s)




