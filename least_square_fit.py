# coding: utf-8
print('<<< this script gives the least-square-fit of a data file with 2 data coloumns spearated by a delimiter >>>\n')
x=input('enter the name of data file along with extension >> ')
d=input('enter the delimiter >> ')
l,t=loadtxt(x,unpack=True,delimiter=d)
tsq=t**2
inter_mat=array([l,ones_like(l)])
A=inter_mat.T
result=lstsq(A,tsq)
p=result[0]
m,c=p
tsq_fit=m*l+c
plot(l,tsq,'bo')
plot(l,tsq_fit,'r')
show()

