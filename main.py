"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION

"""

def ekstraksi_data():
    """
    tanggal:24 agustus 2021
    waktu:24 agustus 2021
    magnitudo:4.0
    kedalaman:40km
    lokasi: LS=1.48 BT=134.01
    pusat gempa: pusat gempa berada di darat 18 km barat laut Ransiki
    dirasakan: dirasakan (skala MMI): II-III Manokwari, II-III Ransiki
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '24 agustus 2021'
    hasil['waktu'] = '12:05:52 WIB'
    hasil['magnitudo'] = '4.0'
    hasil['kedalaman'] = '40km'
    hasil['lokasi'] = 'LS=1.48 BT=134.01'
    hasil['pusat gempa'] = 'pusat gempa berada di darat 18 km barat'
    hasil [ 'dirasakan'] = 'dirasakan (skala MMI): II-III Manokwari'



    return hasil




def tampilkan_data(result):
    print('gempa terakhir berdasarkan BMKG')
    print (f"tanggal {result['tanggal']}")
    print (f"waktu {result['waktu']}")
    print (f"magnitudo {result['magnitudo']}")
    print (f"kedalaman {result['kedalaman']}")
    print (f"lokasi {result['lokasi']}")
    print (f"pusat gempa: {result['pusat gempa']}")
    print (f"dirasakan {result['dirasakan']}")







if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)