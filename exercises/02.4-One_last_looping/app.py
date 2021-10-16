my_sample_list = ['Ruth','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
my_sample_list[1]='Steven'
my_sample_list[-1]='Pepe'
my_sample_list[0]=my_sample_list[0]+my_sample_list[4]
ultimo=len(my_sample_list)-1
for i in range(ultimo,-1,-1):
    print(my_sample_list[i])

