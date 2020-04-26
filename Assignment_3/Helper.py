#Assignment-2
#Ashish Goyal
#2016ucp1100
#16 April 2020

def Split(expression_in):
    original = expression_in
    expression_in=expression_in.split()
    Expression_Dictionary={}
    flag=0
    st=[]
    length = len(expression_in)
    #print(length)
    for i in range(length):
        if(expression_in[i]==']'):
            Small_expression=""
            #if(flag==0):
                #print(st)
            while(st[len(st)-1]!='['):
                Small_expression=st.pop()+" "+Small_expression
            st.pop() # to remove '['
            st.append("Expr"+str(flag))
            Expression_Dictionary["Expr"+str(flag)]=Small_expression[:-1]
            flag+=1         
        else:
            st.append(expression_in[i])
    #print(Expression_Dictionary)
    return Expression_Dictionary , original
