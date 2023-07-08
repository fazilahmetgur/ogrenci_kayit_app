students = []

def add_student():
    name = input("Öğrenci adını girin: ")
    student = {"Ad": name}
    students.append(student)
    print("Öğrenci başarıyla eklendi.")

def search_student():
    name = input("Aranacak öğrenci adını girin: ")
    found_students = []
    for student in students:
        if student["Ad"].lower() == name.lower():
            found_students.append(student)
    
    if found_students:
        print("Aranan öğrenci bulundu:")
        for found_student in found_students:
            print("Ad:", found_student["Ad"])
    else:
        print("Aranan öğrenci bulunamadı.")

def delete_student():
    name = input("Silinecek öğrenci adını girin: ")
    deleted_students = []
    for student in students:
        if student["Ad"].lower() == name.lower():
            students.remove(student)
            deleted_students.append(student)
    
    if deleted_students:
        print("Öğrenci başarıyla silindi:")
        for deleted_student in deleted_students:
            print("Ad:", deleted_student["Ad"])
    else:
        print("Silinecek öğrenci bulunamadı.")

def delete_all_students():
    confirmation = input("Tüm öğrenci kayıtlarını silmek istediğinize emin misiniz? (E/H): ")
    if confirmation.lower() == "e":
        students.clear()
        print("Tüm öğrenci kayıtları başarıyla silindi.")
    else:
        print("İşlem iptal edildi.")

def display_menu():
    print("\nÖğrenci Kayıt Programı")
    print("1. Öğrenci Ekle")
    print("2. Öğrenci Ara")
    print("3. Öğrenci Sil")
    print("4. Tüm Kayıtları Sil")
    print("5. Çıkış")

def main():
    while True:
        display_menu()
        choice = input("Seçiminizi yapın (1-5): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            delete_all_students()
        elif choice == "5":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()