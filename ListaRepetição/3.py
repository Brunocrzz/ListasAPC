#Questão 3 OK

N = int(input())
first = map(int, input().split())
second = map(int, input().split())
final = map(lambda x, y: x*y, first, second)
summation = sum(final)
print('ortogonais' if not summation else summation)