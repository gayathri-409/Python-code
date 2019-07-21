#input filename output only after extension
x=input('enter the file name:')
extension=(x.split('.'))
print(extension[1])


#pgrm to display first and last colour of list
colour=input('enter the colours: ')
list=colour.split(',')
print('first colour is ',list[0],"and last colour is ",list[-1])

#extract date and print in dd/mm/yyyy
examdate=(10,4,19)
print("examdate is: %i/%i/%i"%examdate)