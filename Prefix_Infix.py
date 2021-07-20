def prefix_infix(prefix):
    n=len(prefix)
    infix=['']*n#infix stack
    t=-1
    op=('+','-','*','/')
    for ch in prefix[::-1]:
        if ch in op:
            op1=infix[t]
            infix[t]=''
            t-=1
            op2=infix[t]
            infix[t]=''
            t-=1
            ch='('+op1+ch+op2+')'
        t+=1
        infix[t]=ch
    return infix[0]
prefix=input()
infix=prefix_infix(prefix)
print(infix)
            


'''
prefix:*-A/BC-/AKL
infix:((A-(B/C))*((A/K)-L))
'''
