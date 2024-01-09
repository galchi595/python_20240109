coffee=['아메리카노','에스프레소','카페라떼']
cookie=['화이트쿠키','오레오쿠키','녹차쿠키']
menu=coffee+cookie
print(menu)

double_menu=menu*2
print(double_menu)

print('에스프레소'in menu)

new_menu=menu[2:5]
print(new_menu)

print()

store=['cu','gs','seven','ministop']
print(len(store))

store.append('emart24')
print(store)

store.insert(2,'familymart')
print(store)

store.remove('cu')
print(store)

print(store.index('ministop'))

print(store.count('emart24'))

newstore=['storyway','buytheway']
store.extend(newstore)
print(store)

store.sort()
print(store)
store.sort(reverse=True)
print(store)