def ekstraksi_data():
    """

    tanggal : 24 agustus 2021
    waktu : 12:05:52 WIB
    magnitudo : 4.0
    kedalaman : 40 km
    lokasi : LS= 1.48  BT= 134.01
    pusat gempa : pusat gempa berada di darat 18 km barat laut ransiki
    dirasakan : (skala MMI): II-III manokwari, II_III ransiki
    :return:
    """


    hasil = dict()
    hasil ['tanggal'] = '24 agustus 2021'
    hasil ['waktu'] = '12.05.52 WIB'
    hasil ['magnitudo'] = '4.0'
    hasil ['kedalaman'] = '40 km'
    hasil ['lokasi'] = {'ls':1.48, 'bt':134.01}
    hasil ['pusat'] = 'pusat gempa berada di darat 18 km barat laut ransiki'
    hasil ['dirasakan'] = '(skala MMI): II-III manokwari, II_III ransiki'

        return hasil


def tampilkan_data(result) :
    print ('gempa terakhir berdasarkan BMKG')
    print (f"tanggal {result['tanggal']}")
    print (f"waktu  {result['waktu']}")
    print (f"magnitudo {result['magnitudo']}")
    print (f"lokasi :  LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print (f"pusat {result['pusat']}")
    print (f"dirasakan {result['dirasakan']}")



if __name__ == '__main__':
   print('ini adalah package gempaterkini')




