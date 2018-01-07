cerita_saya = '''
saya merasa {} hari ini,
jika tidak hujan, hari ini saya akan {},
dan pergi ke {} untuk membuat {},
menghabiskan waktu sebelum memesan {}
untuk makan, dan pulang pada {} hari,
untuk melanjutkan dengan {} di rumah
'''

def program_utama():
	keadaan = input('Bagaimana perasaan Anda hari ini? (ex. senang): ')
	lokasi  = input('Masukkan nama tempat? (ex. taplau/mall): ')
	objek 	= input('Masukkan kata objek? (ex. PR/Tugas/Skripsi): ')
	makanan = input('Nama makanan yang Anda suka? (ex. langkitang): ')
	hari 	= input('Masukkan ungkapan waktu? (ex. pagi/siang/sore/malam): ')

	pekerjaan = []
	pekerjaan.append(input('Masukkan ungkapan kata kerja? (ex. bersepeda/berjalan): '))
	pekerjaan.append(input('Masukkan ungkapan kata kerja yang biasa dilakukan dirumah? (ex. tidur/ngoding): '))

	hasil = cerita_saya.format(keadaan,
							pekerjaan[0],
							lokasi,
							objek,
							makanan,
							hari,
							pekerjaan[1])
	print(hasil)

program_utama()
