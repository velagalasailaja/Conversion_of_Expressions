def prefix_postfix(prefix):
    n=len(prefix)
    postfix=['']*n#postfix stack
    t=-1
    op=('+','-','*','/')
    for ch in prefix[::-1]:
        if ch in op:
            op1=postfix[t]
            postfix[t]=''
            t-=1
            op2=postfix[t]
            postfix[t]=''
            t-=1
            ch=op1+op2+ch
        t+=1
        postfix[t]=ch
    return postfix[0]
prefix=input()
postfix=prefix_postfix(prefix)
print(postfix)

