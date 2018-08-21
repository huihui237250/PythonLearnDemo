rec = {"name":{'first':'Bob','last':'Smith'},'job':['dev','mgr'],'age':40.5}
print('====rec===')
print(rec)
print('\n====rec.name===')
print(rec['name'])
rec['job'].append('janitor')
print('====new rec===')
print(rec)

x = 4
while x > 0:
	print('spam!' * x)
	x -=1
print('line')

squares = [x ** 2 for x in [1,2,3,4,5]]
print(squares)

if not 'sex' in rec:
	print('no sex key')

T = (1,2,3,4)
print(len(T))

T + (5,6)
print(T)
print(T[0])


f = open('data.txt','w')
f.write('Hello\n')
f.write('world\n')
f.close()

f2 = open('data.txt');
text = f2.read()
print(text)
f2.close

print(text.split())

x = set('spam')
for m in [1,2,3,4]:
	print(m)
	print(m ** 2)
Y = {n ** 2 for n in [1,2,3,4]}
print(Y)



































