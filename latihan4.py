print("\tLATIHAN 3")
print("Nota Pembelian")
print("_"*40)
namabrg = input("nama barang\t: ")
hargabrg = int(input("harga barang\t: "))
jumlahbrg = int(input("jumlah barang\t: "))

subtotal = hargabrg * jumlahbrg
print(f"subtotal\t: Rp.{subtotal:>20} ")

diskon = 0.2 * subtotal
print(f"diskon\t\t: Rp.{diskon:>20.0f} ")

total = subtotal - diskon
print(f"total\t\t: Rp.{total:>20.0f} ")

bayar = int(input("bayar\t\t: Rp.               "))

print("_"*40)

kembalian = bayar - total
print(f"kembalian\t: Rp. {kembalian:>20.0f} ")

print("Rincian Kembalian")


