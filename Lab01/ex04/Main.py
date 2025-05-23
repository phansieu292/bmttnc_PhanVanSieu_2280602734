from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (True): # Dùng while True: gọn hơn while (1 == 1):
        print("\nCHUONG TRINH QUAN LY SINH VIEN")
        print("********************MENU********************")
        print("** 1. Them sinh vien.                     **")
        print("** 2. Cap nhat thong tin sinh vien boi ID.  **")
        print("** 3. Xoa sinh vien boi ID.               **")
        print("** 4. Tim kiem sinh vien theo ten.        **")
        print("** 5. Sap xep sinh vien theo diem trung binh. **")
        print("** 6. Sap xep sinh vien theo ten chuyen nganh. **")
        print("** 7. Hien thi danh sach sinh vien.       **")
        print("** 0. Thoat                               **")
        print("********************************************")

        try:
            key = int(input("Nhap tuy chon: "))
        except ValueError:
            print("Vui long nhap mot so cho lua chon menu.")
            continue # Quay lại đầu vòng lặp

        if (key == 1):
            print("\n--- 1. Them sinh vien ---")
            qlsv.nhapSinhVien()
            print("\nThem sinh vien thanh cong!")
        elif (key == 2):
            print("\n--- 2. Cap nhat thong tin sinh vien ---")
            if (qlsv.soLuongSinhVien() > 0):
                try:
                    ID_to_update = int(input("Nhap ID sinh vien can cap nhat: "))
                    qlsv.updateSinhVien(ID_to_update)
                except ValueError:
                    print("ID khong hop le. Vui long nhap so.")
            else:
                print("Danh sach sinh vien trong! Khong co sinh vien de cap nhat.")
        elif (key == 3):
            print("\n--- 3. Xoa sinh vien ---")
            if (qlsv.soLuongSinhVien() > 0):
                try:
                    ID_to_delete = int(input("Nhap ID sinh vien can xoa: "))
                    if (qlsv.deleteByID(ID_to_delete)):
                        print(f"Sinh vien co ID = {ID_to_delete} da bi xoa.")
                    else:
                        print(f"Sinh vien co ID = {ID_to_delete} khong ton tai.")
                except ValueError:
                    print("ID khong hop le. Vui long nhap so.")
            else:
                print("Danh sach sinh vien trong! Khong co sinh vien de xoa.")
        elif (key == 4):
            print("\n--- 4. Tim kiem sinh vien theo ten ---")
            if (qlsv.soLuongSinhVien() > 0):
                name_keyword = input("Nhap ten (hoac mot phan ten) de tim kiem: ")
                search_results = qlsv.findByName(name_keyword)
                if search_results:
                    print("\nKet qua tim kiem:")
                    qlsv.showSinhVien(search_results)
                else:
                    print("Khong tim thay sinh vien nao co ten/tu khoa nay.")
            else:
                print("Danh sach sinh vien trong! Khong co sinh vien de tim kiem.")
        elif (key == 5):
            print("\n--- 5. Sap xep sinh vien theo diem trung binh (GPA) ---")
            if (qlsv.soLuongSinhVien() > 0):
                qlsv.sortByDiemTB()
                print("\nDanh sach sinh vien sau khi sap xep theo diem trung binh:")
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("Danh sach sinh vien trong! Khong co sinh vien de sap xep.")
        elif (key == 6):
            print("\n--- 6. Sap xep sinh vien theo ten ---")
            if (qlsv.soLuongSinhVien() > 0):
                qlsv.sortByName()
                print("\nDanh sach sinh vien sau khi sap xep theo ten:")
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("Danh sach sinh vien trong! Khong co sinh vien de sap xep.")
        elif (key == 7):
            print("\n--- 7. Hien thi danh sach sinh vien ---")
            if (qlsv.soLuongSinhVien() > 0):
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("Danh sach sinh vien trong!")
        elif (key == 0):
            print("\nBan da chon thoat chuong trinh! Tam biet.")
            break # Thoát khỏi vòng lặp while True
        else:
            print("\nKhong co chuc nang nay! Hay chon chuc nang trong hop menu.")