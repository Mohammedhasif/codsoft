def W(b,p):return any(b[i]==b[j]==b[k]==p for i,j,k in[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])
def M(b,p):return max(((1 if W(b[:i]+['O']+b[i+1:],'O')else-1 if W(b[:i]+['X']+b[i+1:],'X')else 0,i)for i in range(9)if b[i]==' '),default=(0,-1))[1]if p=='O'else min(((1 if W(b[:i]+['O']+b[i+1:],'O')else-1 if W(b[:i]+['X']+b[i+1:],'X')else 0,i)for i in range(9)if b[i]==' '),default=(0,-1))[1]
b=[' ']*9
while' 'in b and not W(b,'X')and not W(b,'O'):print(b[:3],b[3:6],b[6:]);b[int(input("0-8:"))]='X';b[M(b,'O')]='O'if' 'in b and not W(b,'X')else b
print(b[:3],b[3:6],b[6:]);print("W:",'X'if W(b,'X')else'O'if W(b,'O')else'Draw')
