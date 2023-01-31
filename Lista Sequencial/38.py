def ritmoMedio(h,m,s,k):
  tempoSeg = (h*3600)+(m*60)+(s)
  Mediaseg = tempoSeg/k
  Mediaseg = int(Mediaseg)
  print('%.2d:%.2d min/km' % ((Mediaseg//60), (Mediaseg%60)))