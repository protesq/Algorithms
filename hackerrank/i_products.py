from itertools import product  # itertools kütüphanesinden product fonksiyonunu içe aktarır (kartezyen çarpım için kullanılır).

# Ana fonksiyon tanımlanır.
def main():
    first_list = []  # İlk listeyi tanımlıyoruz (başlangıçta boş).
    second_list = []  # İkinci listeyi tanımlıyoruz (başlangıçta boş).

    # Kullanıcıdan alınan girdiyi boşluklara göre ayırıp, listeye int tipinde atıyoruz.
    first_list = list(map(int, input("İlk liste elemanlarını girin (boşlukla ayırın): ").split()))
    
    # Kullanıcıdan ikinci listeyi alıyoruz.
    second_list = list(map(int, input("İkinci liste elemanlarını girin (boşlukla ayırın): ").split()))

    # product() ile iki liste arasında tüm olası çiftleri üretiyoruz.
    for x in product(first_list, second_list):
        # Üretilen çiftleri aynı satırda aralarına boşluk koyarak yazdırıyoruz.
        print(x, end=" ")

# Ana fonksiyonun yalnızca bu dosya doğrudan çalıştırıldığında çalışması için kontrol.
if __name__ == "__main__":
    main()  # main fonksiyonunu çalıştırır.
