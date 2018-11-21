medida = float(input('Uma distancia  em metros: '))
dam =medida / 10
dm = medida * 10
hm = medida / 100
km = medida / 1000
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a '.format(medida))
print('{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm '.format(km,hm,dam,dm,cm,mm))