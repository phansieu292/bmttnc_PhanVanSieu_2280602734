from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = [] # Đây là một biến lớp, tất cả các thể hiện của QuanLySinhVien sẽ dùng chung list này.
                      # Thường thì nên đặt list này trong __init__ để mỗi thể hiện có list riêng.
                      # Tuy nhiên, nếu bạn chỉ tạo một thể hiện của QuanLySinhVien thì không sao.

    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            # Cần đảm bảo listSinhVien[0]._id là số để so sánh.
            # Và kiểm tra xem listSinhVien có rỗng không trước khi truy cập phần tử đầu tiên.
            # Logic này có thể gây lỗi nếu list rỗng và bạn cố gắng truy cập listSinhVien[0]._id
            # Tuy nhiên, dòng 'if (self.soLuongSinhVien() > 0):' đã giải quyết vấn đề đó.
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def soLuongSinhVien(self):
        return len(self.listSinhVien) # Sử dụng len() thay vì __len__() trực tiếp

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        # Đảm bảo nhập số thực cho điểm
        try:
            diemTB = float(input("Nhap diem cua sinh vien: "))
        except ValueError:
            print("Diem khong hop le. Vui long nhap so.")
            return # Thoát khỏi hàm nếu nhập sai

        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if (sv != None):
            print("\nCap nhat thong tin sinh vien:")
            name = input("Nhap ten sinh vien moi (Enter de giu nguyen): ")
            if name: # Nếu người dùng nhập gì đó, thì cập nhật
                sv._name = name

            sex = input("Nhap gioi tinh moi (Enter de giu nguyen): ")
            if sex:
                sv._sex = sex

            major = input("Nhap chuyen nganh moi (Enter de giu nguyen): ")
            if major:
                sv._major = major

            diemTB_str = input("Nhap diem moi (Enter de giu nguyen): ")
            if diemTB_str:
                try:
                    sv._diemTB = float(diemTB_str)
                    self.xepLoaiHocLuc(sv) # Cập nhật học lực sau khi đổi điểm
                except ValueError:
                    print("Diem khong hop le. Khong cap nhat diem.")
            print("Cap nhat sinh vien thanh cong!")
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.") # Sử dụng f-string cho dễ đọc

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        # Sắp xếp theo tên, có thể muốn không phân biệt hoa thường
        self.listSinhVien.sort(key=lambda x: x._name.lower(), reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=True) # Sắp xếp giảm dần điểm TB

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if (sv._id == ID):
                return sv
        return None # Trả về None nếu không tìm thấy

    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            keyword_upper = keyword.upper() # Chuyển keyword sang chữ hoa một lần
            for sv in self.listSinhVien:
                if (keyword_upper in sv._name.upper()):
                    listSV.append(sv)
        return listSV

    def deleteByID(self, ID):
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            return True
        return False

    def xepLoaiHocLuc(self, sv:SinhVien): # Annotation kiểu dữ liệu cho sv
        if (sv._diemTB >= 8):
            sv._hocluc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocluc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocluc = "Trung binh"
        else:
            sv._hocluc = "Yeu"

    def showSinhVien(self, listSV):
        if not listSV: # Kiểm tra xem listSV có rỗng không
            print("Danh sach sinh vien trong.")
            return

        print("{:<8}{:<25}{:<10}{:<15}{:<10}{:<10}" # Điều chỉnh độ rộng cột cho phù hợp
              .format("ID", "Ten", "Gioi Tinh", "Chuyen Nganh", "Diem TB", "Hoc Luc"))
        print("-" * 78) # Đường kẻ phân cách
        for sv in listSV:
            print("{:<8}{:<25}{:<10}{:<15}{:<10.2f}{:<10}" # .2f để định dạng điểm TB 2 chữ số thập phân
                  .format(sv._id, sv._name, sv._sex, sv._major,
                          sv._diemTB, sv._hocluc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien