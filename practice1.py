#use /n/t
print('Happy brithday\n\n\thave a nice day')

#python version pgrm
import sys
print('python version')
print(sys.version)
print(sys.version_info)

#Current date time
import datetime
now=datetime.datetime.now()
print(now)
print(now.strftime('%Y-%m-%d %H:%M:%S'))

#area of circle
r=int(input('enter radius of circle: '))
pi=3.141
area = pi*r**2
print(area)

#name in reverse order
name=input('enter first and last name')
for i in name[::-1]:
    print(i,end='')

#generate list n tuple with user inputing nos separated by comma
values = input('enter comma separated nos: ')
list = values.split(',')
tuple=tuple(list)
print(list)
print(tuple)