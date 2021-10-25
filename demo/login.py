def main():
    status = False
    i = 1
    while not status:
        print("---------------------> " + str(i) + ". Deneme")

        username = input("Username: ")
        password = input("Password: ")

        if (username == "admin" and password == "mmmsa"):
            print("-------------------------")
            print("### Giriş Başarılı", password)
            print("-------------------------")
            status = True
        else:
            print("### Giriş Başarısız. Lütfen Tekrar Deneyiniz.")
            status = False
        i += 1


if __name__ == "__main__":
    main()
