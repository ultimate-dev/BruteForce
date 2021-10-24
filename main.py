from generator import Default


def main():
    print("(1) Kelimeler")
    print("(2) Sayılar")
    print("(3) Deneme")

    choice = int(input("=> "))
    if (choice == 1):
        words = input("Kelimeleri Giriniz=> ").replace(" ", "").split(",")
        length = int(input("Şifre uzunluğu=> "))
        filename = input("Çıktı Dosya Adı=> ")
    elif (choice == 2):
        words = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        length = int(input("Şifre uzunluğu=> "))
        filename = input("Çıktı Dosya Adı=> ")
    elif (choice == 3):
        words = ["masa", "erik", "saat"]
        length = 5
        filename = "şifreler"

    combinations = Default(words, filename, length)

    print("----------------------------------------------")
    print("Üretilen Kobinasyon:", combinations)
    print("----------------------------------------------")


if __name__ == "__main__":
    main()
