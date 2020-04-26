#Assignment-3
#Ashish Goyal
#2016ucp1100
#16 April 2020
# See ReadMe.docx for more info 

#########################################
#Input preprocessing

from Helper import Split 
file1 = open("Input-File.txt","r+") 
lst=[]
lst=file1.readlines()
#print(type(lst[0]))
expression = lst[0]
file2 = open("Output-File.txt","w+")

#########################################

Expression_Dictionary={}    
Dependency_Dictionary ={}  # Dependency list
Equivalent_Expression ={}  # All Equivalent expressions list
Expression_Dictionary,original = Split(expression) # Split complete expression into smaller expressions
file2.write("Given Expression: ")
file2.write(original)
file2.write("\n")
for i in Expression_Dictionary:
  temp = Expression_Dictionary[i].split()
  emp_list=[]
  for j in temp:
    if 'Expr' in j:
      emp_list.append(j)

  Dependency_Dictionary[i]=emp_list  
#print("Expression_Dictionary \n",Expression_Dictionary)
#print("Dependency_Dictionary \n",Dependency_Dictionary)
##########################################
#Function Defination
  
def Rule1(query):
  Splitted_Query = query.split()
  Output_Expression = [query]
  Rule_Output = Splitted_Query[0]+" "+Splitted_Query[1]+" ( "+"Sigma "+Splitted_Query[3]+" ( "+Splitted_Query[5]+" )"+" )"
  Output_Expression.append(Rule_Output)
  return Output_Expression


def Rule2(query):
  Splitted_Query = query.split()
  Output_Expression = [query]
  Rule_Output = Splitted_Query[0]+" "+Splitted_Query[4]+" ("+" Sigma "+Splitted_Query[1]+" ( "+Splitted_Query[6]+" )"+" )"
  Output_Expression.append(Rule_Output)
  return Output_Expression


def Rule3(query):
  Splitted_Query = query.split()
  Output_Expression = [query]
  for i in range(len(Splitted_Query)-1,-1,-1):
    if(Splitted_Query[i]!=')'):
      expression = Splitted_Query[i]
      break
  Rule_Output = Splitted_Query[0]+" "+Splitted_Query[1]+" ( "+expression+" )"
  Output_Expression.append(Rule_Output)
  return Output_Expression


def Rule4(query):
  Splitted_Query = query.split()
  Output_Expression = [query]
  if('*' in Splitted_Query):     
      file2.write("Rule 4(i) \n")
      Rule_Output = Splitted_Query[3]+' Join '+Splitted_Query[1]+" "+Splitted_Query[5]
  elif('Join' in Splitted_Query):  
      file2.write("Rule 4(ii) \n")
      Rule_Output = Splitted_Query[3]+' Join '+Splitted_Query[1]+" ^ "+Splitted_Query[5]+Splitted_Query[6]
  Output_Expression.append(Rule_Output)
  return Output_Expression

def Rule5(query):
  Splitted_Query = query.split()
  Output_Expression = [query]
  Splitted_Query[len(Splitted_Query)-1],Splitted_Query[0]=Splitted_Query[0],Splitted_Query[len(Splitted_Query)-1]
  Rule_Output = ""
  for i in Splitted_Query:
      Rule_Output+=i+" "
  Rule_Output=Rule_Output[:len(Rule_Output)-1]
  Output_Expression.append(Rule_Output)
  return Output_Expression

def Rule6(query):
  Splitted_Query = query.split()
  Output_Expression = [query]
  if('^' not in Splitted_Query):    
      file2.write("Rule 6(i) \n")
      if(Splitted_Query[1]=='Join'):
          Rule_Output="( "+Splitted_Query[0]+" Join "+Splitted_Query[3]+" ) "+"Join "+Splitted_Query[5]
      elif(Splitted_Query[2]=='Join'):
          Rule_Output=Splitted_Query[1]+" Join "+"( "+Splitted_Query[3]+" Join "+Splitted_Query[6]+" )"
      
  else:                   
      file2.write("Rule 6(ii) \n")
      Rule_Output=Splitted_Query[1]+" Join "+Splitted_Query[3]+" ^ "+Splitted_Query[9]+" ( "+Splitted_Query[4]+" Join "+Splitted_Query[7]+" "+Splitted_Query[10]+" )"
  Output_Expression.append(Rule_Output)
  return Output_Expression

def Rule7(query):
  Splitted_Query = query.split()
  Output_Expression = [query]
  Rule_Output="("+" Sigma "+Splitted_Query[1]+" ( "+Splitted_Query[5]+" ) )"+" Join "+Splitted_Query[7]+" ( Sigma "+Splitted_Query[3]+" ( "+Splitted_Query[8]+" ) )"
  Output_Expression.append(Rule_Output)
  return Output_Expression

def Rule8(query):
  Splitted_Query = query.split()
  Output_Expression = [query]
  Rule_Output= "( Project "+Splitted_Query[1]+" ( "+Splitted_Query[5]+" ) ) Join "+Splitted_Query[7]+" ( Project "+Splitted_Query[3]+" ( "+Splitted_Query[8]+" ) )"
  Output_Expression.append(Rule_Output)
  return Output_Expression

def Rule9(query):
  Splitted_Query = query.split()
  Output_Expression = [query]
  if('-' not in Splitted_Query):
      Rule_Output= Splitted_Query[2]+" "+Splitted_Query[1]+" "+Splitted_Query[0]
      Output_Expression.append(Rule_Output)
  return Output_Expression

def Rule10(query):
  Splitted_Query = query.split()
  Output_Expression = [query]
  if('-' not in Splitted_Query):
      if(Splitted_Query[1]=='Union' or Splitted_Query[1]=='Intersect'):
          Rule_Output="( "+Splitted_Query[0]+" "+Splitted_Query[1]+" "+Splitted_Query[3]+" ) "+Splitted_Query[1]+" "+Splitted_Query[5]
      elif(Splitted_Query[2]=='Union' or Splitted_Query[2]=='Intersect'):
          Rule_Output=Splitted_Query[1]+" "+Splitted_Query[2]+" ( "+Splitted_Query[3]+" "+Splitted_Query[2]+" "+Splitted_Query[6]+" )"
      Output_Expression.append(Rule_Output)
  return Output_Expression

def Rule11(query):
  Splitted_Query = query.split()
  Output_Expression = [query]
  Rule_Output= "Sigma "+Splitted_Query[1]+" ( "+Splitted_Query[3]+" ) Union "+"Sigma "+Splitted_Query[1]+" ( "+Splitted_Query[5]+" )"
  Output_Expression.append(Rule_Output)
  return Output_Expression

def Rule12(query):
  Splitted_Query = query.split()
  Output_Expression = [query]
  if('Union' in Splitted_Query):
      Rule_Output= "Project "+Splitted_Query[1]+" ( "+Splitted_Query[3]+" ) Union "+"Project "+Splitted_Query[1]+" ( "+Splitted_Query[5]+" )"
      Output_Expression.append(Rule_Output)
  return Output_Expression

file2.write("Equivalence Rules used are:\n")
for i in Expression_Dictionary:
  query = Expression_Dictionary[i]
  Splitted_Query = query.split()
  if('Sigma' in Splitted_Query and '^' in Splitted_Query and 'Join' in Splitted_Query):
    file2.write("Rule 7 \n")
    temp_out = Rule7(query)
    Equivalent_Expression[i]=temp_out
  elif('Project' in Splitted_Query and 'Union' in Splitted_Query and 'Join' in Splitted_Query):
    file2.write("Rule 8 \n")
    temp_out = Rule8(query)
    Equivalent_Expression[i]=temp_out
  elif(Splitted_Query[0]=='Sigma' and Splitted_Query[2]=='^'):
    file2.write("Rule 1 \n")
    temp_out = Rule1(query)
    Equivalent_Expression[i]=temp_out
  elif(Splitted_Query[0]=='Sigma' and Splitted_Query[3]=='Sigma'):
    file2.write("Rule 2 \n")
    temp_out = Rule2(query)
    Equivalent_Expression[i]=temp_out
  elif(Splitted_Query[0]=='Project' and Splitted_Query[3]=='Project'):
    file2.write("Rule 3 \n")
    temp_out = Rule3(query)
    Equivalent_Expression[i]=temp_out
  elif(Splitted_Query[0]=='Sigma' and (Splitted_Query[4]=='*' or Splitted_Query[4]=='Join')):
    temp_out = Rule4(query)
    Equivalent_Expression[i]=temp_out
  elif(Splitted_Query[1]=='Join' and Splitted_Query.count('Join')==1):
    file2.write("Rule 5 \n")
    temp_out = Rule5(query)
    Equivalent_Expression[i]=temp_out
  elif(Splitted_Query.count('Join') > 1):
    temp_out = Rule6(query)
    Equivalent_Expression[i]=temp_out
  elif(('Union' in Splitted_Query and Splitted_Query.count('Union')>1) or ('Intersect' in Splitted_Query and Splitted_Query.count('Intersect')>1) or ('-' in Splitted_Query and Splitted_Query.count('-')>1)):
    file2.write("Rule 10 \n")
    temp_out = Rule10(query)
    Equivalent_Expression[i]=temp_out
  elif(Splitted_Query[0]=='Sigma' and ('Union' in Splitted_Query or 'Intersect' in Splitted_Query or '-' in Splitted_Query)):
    file2.write("Rule 11 \n")
    temp_out = Rule11(query)
    Equivalent_Expression[i]=temp_out
  elif(Splitted_Query[0]=='Project' and ('Union' in Splitted_Query or 'Intersect' in Splitted_Query or '-' in Splitted_Query)):
    file2.write("Rule 12 \n")
    temp_out = Rule12(query)
    Equivalent_Expression[i]=temp_out
  elif(('Union' in Splitted_Query and Splitted_Query.count('Union')==1) or ('Intersect' in Splitted_Query and Splitted_Query.count('Intersect')==1) or ('-' in Splitted_Query and Splitted_Query.count('-')==1)):
    file2.write("Rule 9 \n")
    temp_out = Rule9(query)
    Equivalent_Expression[i]=temp_out

  
def checkConvergable(LHS):
  if(len(Dependency_Dictionary[LHS])==0):
    return 0
  else:
    return 1
  
def converge(LHS):
  for i in Dependency_Dictionary[LHS]:
    if(checkConvergable(i)):
      converge(i)
    lis_updated=[]
    for j in Equivalent_Expression[LHS]:
      for k in Equivalent_Expression[i]:
        lis_updated.append(j.replace(i,k))
    Equivalent_Expression[LHS]=lis_updated

converge('Expr'+str(len(Expression_Dictionary)-1))

file2.write("There are total "+str(len(Equivalent_Expression['Expr'+str(len(Expression_Dictionary)-1)]))+" possible Equivalent expressions for the given expression :")
file2.write("\n")
for j in Equivalent_Expression['Expr'+str(len(Expression_Dictionary)-1)]:
  file2.write(j)
  file2.write("\n")

file1.close()
file2.close()

