from datetime import datetime
data1 = datetime(2015, 8, 5)
data2 = datetime(2016, 8, 9)
difdata = data2 - data1
diashora = '{0}:{2}'.format(*str(difdata).split())


print(diashora.split(':')[0])
input()