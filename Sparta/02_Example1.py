fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

print(fruits)
print('=====')
for i in fruits:
    print(i)
print('=====')
for i in range(len(fruits)):
    print(fruits[i])


people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

print(people[1]['name'])
print('=====')
for i in range(len(people)):
    print(people[i]['name'])
print('=====')
for person in people:
    if person['age'] > 20 :
        print(person['name'])

print('===================================')

# 주석처리를 위해서는 Ctrl + /
my_email = '@naver.com'
result1 = my_email.split('@')[1].split('.')[0]
print(result1)

result2 = my_email.replace('naver', 'gmail')
print(result2)

