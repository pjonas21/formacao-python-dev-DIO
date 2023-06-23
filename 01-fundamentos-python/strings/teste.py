T = input("Ler entrada: ")

if T.__len__() <= 140:
    print("TWEET")
else:
    print("MUTE")

month = 4

months_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

print(months_dict[4])

N = int(input())

for i in range(N):
  a,b = input().split()
  if a.endswith(b):
    print('encaixa')
  else:
    print('nao encaixa')

