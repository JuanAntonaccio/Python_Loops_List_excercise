par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"
letters="abcdefghijklmnopqrstuvxyz"
counts = {}
#your code go here:
for i in par:
    a=i.lower()
    if a in letters:
      
       if a in counts.keys():
             counts[a]=counts[a]+1
             
       else:
           counts[a]=1    

print(counts)

