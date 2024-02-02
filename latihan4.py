print("\tLATIHAN 3")
print(">>" * 2 + " nota penjualan - tko xyz " * 2 + "<<")

print("-" * 90)

namaBarang = input("Masukkan nama barang: ")
hargaSatuan = float(input("Masukkan harga satuan: "))
jumlahBeli = float(input("Masukkan jumlah beli: "))
besarBayar = float(input("Masukkan besar bayar: "))

subTotal = hargaSatuan * jumlahBeli

diskon = 0.20
totalDiskon = subTotal * diskon

totalBayar = subTotal - totalDiskon

print("-" * 90)
print(" Alignment dengan f.string")
print(f"namaBarang   :  {namaBarang} ")
print(f"hargaSatuan  :  {hargaSatuan:.2f} ")
print(f"jumlahBeli   :  {jumlahBeli:.2f} ")
print(f"subTotal     : Rp {subTotal:>11.2f} ")  
print(f"Diskon (20%) : Rp {totalDiskon:>11.2f} ")
print(f"totalBayar   : Rp {totalBayar:>11.2f} ")
print(f"besarBayar   : Rp {besarBayar:>11.2f} ")

print("-" * 90)

kembalian = besarBayar - totalBayar

print(f"kembalian    : Rp {kembalian:>11.2f} ") 

uang = [50000, 20000, 10000, 5000, 2000, 1000]
rincianUang = {}

for nominal in uang:
    lembar = kembalian // nominal
    if lembar > 0:
        rincianUang[nominal] = int(lembar)
        kembalian %= nominal

print("Rincian Lembar Uang:")
for nominal, lembar in rincianUang.items():
    print(f"Rp {nominal}: {lembar} lembar")


if kembalian > 0:
    print(f"Sisa kembalian yang tidak dapat dipecah: Rp {kembalian:.2f}")