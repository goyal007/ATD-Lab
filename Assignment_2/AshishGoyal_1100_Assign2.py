#Assignment-2
#Ashish Goyal
#2016ucp1100
#1 April 2020

from collections import defaultdict
from helper import print_cycles

class Graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices
        #print(self.graph)
  
    def addEdge(self,u,v): 
        #print(type(self.graph[u]))
        if v not in self.graph[u]: #condition to remove duplicate edges
            self.graph[u].append(v) 
  
    def isCyclicHelper(self, v, visited, recStack): # helper function for check cycle or not
        visited[v] = True
        recStack[v] = True
        
        #print(self.graph)
        
        for neighbour in self.graph[v]: 
            if visited[neighbour] == False: 
                if self.isCyclicHelper(neighbour, visited, recStack) == True: 
                    return True
            elif recStack[neighbour] == True: 
                return True 
        recStack[v] = False
        return False

    def isCyclic(self): # function to check cycle present or not
        visited = [False] * self.V 
        recStack = [False] * self.V 
        for node in range(self.V): 
            if visited[node] == False: 
                if self.isCyclicHelper(node,visited,recStack) == True: 
                    return True
        return False
    
    def generate_edges(self): # print edges of the graph
        edges = [] 
        for node in self.graph: 
            for neighbour in self.graph[node]: 
                edges.append((map1[node], map1[neighbour] ))  ### use map1 to print nodes as Transaction_number specified in ques
        return edges

    def topologicalSortHelper(self,v,visited,stack): # helper function for topological sort
        visited[v] = True
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortHelper(i,visited,stack) 
        stack.insert(0,map1[v]) ### use map1 to print nodes as Transaction_number specified in ques
  
    def topologicalSort(self): #If graph is acyclic, the serializability order can be obtained by a topological sorting of the graph
        visited = [False]*self.V 
        stack =[] 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortHelper(i,visited,stack)
        file2.write('< ')
        for a in stack:
            file2.write(a+" ")
        file2.write('>')
        file2.write('\n')
        #print (stack )

    def cycles(self):  # Function to print cycles
        t=tuple(print_cycles(self.graph))
        #print(t)
        ans=[]
        for x in t:
            #print(x)  
            u=[map1[y] for y in x] ### use map1 to print nodes as Transaction_number specified in ques
            ans.append(u)
            #print(ans)
        #print(type(ans))
        for cyc in ans:
            c=0
            temp=""
            for edg in cyc:
                if (c==0):
                    temp=edg
                    c=c+1
                file2.write(edg+"->")
            file2.write(temp+" ")
            file2.write('\n')
#########################################
#Input preprocessing

file1 = open("Input-File.txt","r+") 
lst=[]
lst=file1.readlines()

file2 = open("Output-File.txt","w+") 

for k in range(len(lst)):
    lst[k]=lst[k].strip('\n')               #remove new line character
#print(lst)
trans=[]
data=[]
schedule=[]

temp=lst[0].split(':')
trans=temp[1].split(',')
#print(trans)

map1={} # map integer_values as key to Transaction_number as value
map2={} # map Transaction_number as key to integer_values as value
for i in range(len(trans)):
    map1[i]=trans[i]
    map2[trans[i]]=i
#print(map2)


temp=lst[1].split(':')
data=temp[1].split(',')
#print(data)

c=0

for k in range(3,len(lst)):
    inp=[]
    data=lst[k].split(':')
    inp.append(data[0])
    a=data[1][0]
    b=data[1][2:-2]
    c=map2[data[0]]   ### use map2 for better processing as (integers are used as nodes internally)
    inp.append(a)
    inp.append(b)
    inp.append(c)
    schedule.append(inp)

'''
print("processed schedule")    
for i in schedule:
    print(i)
'''

#######################################
#graph making
nodes=len(trans)
g = Graph(nodes) 
for i in range(len(schedule)-1):
    x=schedule[i]
    for j in range(i+1,len(schedule)):
        y=schedule[j]
        #print("y=",y)
        if(x[2]==y[2] and x[0]!=y[0]):
            if(x[1]=='R' and y[1]=='W'):   #conflicting instruction-1
                g.addEdge(x[3], y[3]) 
            elif(x[1]=='W' and y[1]=='R'): #conflicting instruction-2
                g.addEdge(x[3], y[3]) 
            elif(x[1]=='W' and y[1]=='W'): #conflicting instruction-3
                g.addEdge(x[3], y[3])

#######################################
#print edges
file2.write("edges of the graph::\n")
#print("edges of the graph::")
#print(g.generate_edges())
edges_of_graph=g.generate_edges()
for a in edges_of_graph:
    c=0
    for b in a:
        if(c==0):
            file2.write(b+"->")
            c=c+1
        else:
            file2.write(b)
    file2.write('\n')
file2.write('\n')

#######################################
#cycle_checking
if g.isCyclic()==1:
    file2.write("It is non-serializable schedule\n\n")
    #print("It is non-serializable schedule")
    file2.write("Cycles in the graph:\n\n")
    #print ("Cycles in the graph:")
    g.cycles()
else:
    file2.write("It is conflict serializable schedule\n\n")
    #print("It is conflict serializable schedule")
    file2.write("Corresponding Serializability order for given concurrent schedule:\n\n")
    #print("Corresponding Serializability order for given concurrent schedule:")
    g.topologicalSort() 
print("See 'Output-File.txt' for output")
file1.close()
file2.close() 
