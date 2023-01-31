def resto(a,b,d):
  u = (a+b)%d
  print(u)
for i in range(3):
  a,b,d = input().split(); a=int(a);b=int(b);d=int(d)
  resto(a,b,d)