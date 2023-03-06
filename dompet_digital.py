

menu = (''' Menu
1. Menabung
2. Bayar
3. Transfer
4. cek saldo
''')

print('=======MY DIGITAL WALLET=======\n')
address = 220411100043
password = 12345678

login = int(input('Enter your address\t= '))
passw = int(input('Enter your password\t= '))

stop = False
while not(stop):
    if login == address and passw == password:
        print('\n',menu)
        ingin = int(input('Anda ingin\t= '))
        if ingin==1:
            saldo = 0
            tabung = int(input('Jumlah uang yang ingin anda tabung = Rp '))
            saldo+=tabung
            print('saldo anda = ',saldo)

        elif ingin==2:
            print('Saldo anda sekarang = ')
            starup = input('Anda ingin membayar di starup = ')
            berapa = int(input('jumlah yang ingin anda bayar = Rp '))
            saldo-=berapa
            if berapa<=saldo:
                print('======STRUK=======\n')
                print('Bayar ke\t= ',starup)
                print('Jumlah bayar\t= Rp ',berapa)
                print('========:)===========')
            else:
                print('\n=Maaf saldo anda tidak mencukupi=')
                print('===Silahkan isi saldo terlebih dahulu:)===')
        elif ingin ==3:
            print('Saldo anda sekarang = ')
            tujuan = input('Address tujuan transfer = ')
            berapa = int(input('Jumlah yang ingin anda transfer = Rp '))
            saldo-=berapa
            if berapa<=saldo:
                print('======STRUK=======\n')
                print('Tujuan transfer\t= ',tujuan)
                print('Jumlah transfer\t= Rp ',berapa)
                print('========:)===========')
            else:
                print('\n=Maaf saldo anda tidak mencukupi=')
                print('===Silahkan isi saldo terlebih dahulu:)===')
        elif ingin==4:
            print('Saldo anda sekarang\t= Rp ', saldo)
    else:
        print('Maaf Password yang anda masukkan salah')
        print('===Silahkan coba lagi :)===')

    print('\n===============================')  
    lagi = input('Kembali ke menu (y/t)\t?')
    print('===============================\n')  
    if lagi == 't':
        stop = True



