def Default(words, filename, length):
    # Kelimlerlerdeki harfleri dizide benzersiz olacak şekilde ayır.
    chars = getChars(words)
    # Toplam Kaç Kombinsayon olacağını Hesapla
    combinations = pow(len(chars), length)

    # Kaydedilecek Dosyayı Aç/Oluştur
    file = open(filename + ".txt", "a")
    # Kaydedilecek Dosya İçeriğini Temizle
    file.truncate(0)

    # Kombinasyon Sayısı Kadar Dön
    for i in range(combinations):
        word = ""  # Üretilen Veri
        val = i
        # Şifre uzunluğu kadar Dön
        for j in range(length):
            ch = int(val % len(chars))
            word = chars[ch] + word
            val = int(val / len(chars))

        # Veriyi Dosyaya Yazdırma
        if (i == 0):
            file.write(word)
        else:
            file.write("\n" + word)

    return combinations


def getChars(words):
    chars = []
    for word in words:
        for i in range(len(word)):
            if (word[i] not in chars):
                chars.extend(word[i])
    return chars
