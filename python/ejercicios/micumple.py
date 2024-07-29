#Mi cumple
f = open('micumple.txt','wb')
f.write('Luis M ')
f.close()
m = open('micumple.txt','r')
message = m.read()
print(message)
m.close()
f = open('micumple.txt','a')
f.write('\n' + 'Cumple en')
f.close()
m = open('micumple.txt','r')
message = m.read()
print(message)
m.close()
f = open('micumple.txt','a') 
f.write('\n' + 'el 20 de abril')
f.close()
m = open('micumple.txt','r')
message = m.read()
print(message)
m.close()
print
print "Y ahora en una sola"
m = open('micumple.txt', 'r')
message = m.read()
print(message)
m.close()
print "FIN"
print

