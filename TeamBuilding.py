import time as tm

date = '11․09․2021'
place = 'Երևան Պանդոկ'

while date == '11․09․2021':
     time = tm.strftime("%H:%M", tm.localtime())
     if time == '17:00':
          print('Դու արդեն պետքա ' + place + '-ում լինեիր')
     elif time > '17:00' and 'ունեք գործեր':
          print('կարող եք նաև միանալ ավելի ուշ')
     else:
          print('լիկվիդ!')
          exit(1)
