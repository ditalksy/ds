hari = {
    "senin" : "monday",
    "selasa" : "tuesday",
    "rabu" : "wednesday",
    "kamis" : "thursday",
    "jumat" : "friday",
    "sabtu" : "saturday",
    "minggu" : "sunday",
}

def namahari():
    while True:
        print("""
        Menu : Pilihan
        1. IND - ENG
        2. ENG - IND
        """)

        pilihan = input("Masukkan pilihan/Input choice: ")
        
        #Jika pilih IND - ENG (1)
        if pilihan == "1":
            idEn()
        
        #Jika pilih ENG - IND (2)
        elif pilihan == "2":
            enId()
        
        #Jika pilihan lain
        else:
            print("Pilihan tidak valid / Option is not valid.")

def idEn():
    hariId = input("Masukkan nama hari: ").lower()
    for key, value in hari.items():
        if hariId != key:
            pass
        elif hariId == key:
            print(f"{hariId} dalam bahasa inggris adalah {hari[hariId]}")
            break
        else:
            pass
    else:
        print(f"{hariId} bukan hari yang valid.")

def enId():
    hariEn = input("Enter name of the day: ").lower()
    for key, value in hari.items():
        if hariEn != value:
            pass
        elif hariEn == value:
            print(f"{hariEn} in bahasa is {key}")
            break
        else:
            pass
    else:
        print(f"{hariEn} is not a valid day.")


mekas = babi

namahari()