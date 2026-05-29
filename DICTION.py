employees = {
    "NV01": {"ten": "Nguyễn Văn A", "tuoi": 25, "so_thich": ["Đá bóng", "Đọc sách"]},
    "NV02": {"ten": "Trần Thị B", "tuoi": 28, "so_thich": ["Nấu ăn", "Xem phim"]}
}

# if "NV01" in employees:
#     employees["NV01"]["so_thich"].append("Chơi game")
# Cho thêm sở thích cho NV01


# Lay ra ma nhan vien
# print(employees["NV01"])
# print()

# # Them nhan vien
employees["NV03"] = {
    "ten" : "hello",
    "tuoi" : 18,
    "so_thich": ["An com"]
}
print(employees)
# Duyệt qua từng thông tin nhân viên
for emp_id , emp_info in employees.items():
    print(f"{emp_id} - {emp_info["ten"]} - {emp_info["tuoi"]}")

#Tìm kiếm nhân viên 
find_id = "NV02"

if find_id in employees:
    employ = employees[find_id]
    print(employ["ten"])
else:
    print("Not exist")


print("--- DANH SÁCH SỞ THÍCH CỦA TỪNG NGƯỜI ---")

for emp_id, emp_info in employees.items():
    # Biến list sở thích thành chuỗi, ví dụ: "Đá bóng, Đọc sách"
    chuoi_so_thich = ", ".join(emp_info["so_thich"])
    
    print(f"- {emp_info['ten']} ({emp_id}) thích: {chuoi_so_thich}")


#Xóa mục của nhân viên
muc_bi_xoa = employees["NV01"].pop("so_thich", None)

#Theo phương pháp del dict[key]
# if "NV01" in employees:
#     del employees["NV01"]["so_thich"]

# print(employees["NV01"])

#Dọn dữ liệu bên trong mục 
if "NV01" in employees:
    employees["NV01"]["so_thich"].clear()

print(employees["NV01"])


# --------- CẬP NHẬT NHÂN VIÊN
update_id = input("Nhập mã nhân viên cần cập nhật (ví dụ: NV01): ").strip().upper()

# Kiểm tra xem mã này có tồn tại không
if update_id in employees:
    # Lấy ra dict thông tin của nhân viên đó để xử lý cho gọn
    emp = employees[update_id]
    
    print(f"\n--- ĐANG CẬP NHẬT CHO NHÂN VIÊN {update_id} ---")
    print("(Nếu muốn giữ nguyên mục nào, chỉ cần ấn ENTER mà không cần nhập gì)\n")
    
    # ---------------------------------------------
    # THAO TÁC 1: Cập nhật Tên
    # ---------------------------------------------
    ten_moi = input(f"Tên hiện tại là [{emp['ten']}]. Nhập tên mới: ").strip()
    if ten_moi:  # Nếu người dùng có nhập chữ (không phải chuỗi rỗng)
        emp['ten'] = ten_moi # Tiến hành đè dữ liệu mới lên key 'ten'
        print("-> Đã cập nhật Tên.")
        
    # ---------------------------------------------
    # THAO TÁC 2: Cập nhật Tuổi
    # ---------------------------------------------
    tuoi_moi_str = input(f"Tuổi hiện tại là [{emp['tuoi']}]. Nhập tuổi mới: ").strip()
    if tuoi_moi_str:  # Nếu có nhập tuổi mới
        try:
            emp['tuoi'] = int(tuoi_moi_str) # Ép kiểu sang số nguyên int
            print("-> Đã cập nhật Tuổi.")
        except ValueError:
            print(" Lỗi: Tuổi phải là số! Giữ nguyên tuổi cũ.")

    # # ---------------------------------------------
    # # THAO TÁC 3: Cập nhật Sở thích (Dạng List)
    # # ---------------------------------------------
    # chuoi_st_cu = ", ".join(emp['so_thich'])
    # st_moi_str = input(f"Sở thích hiện tại là [{chuoi_st_cu}]. Nhập các sở thích mới (cách nhau bằng dấu phẩy): ").strip()
    # if st_moi_str: # Nếu có nhập sở thích mới
    #     # Cắt chuỗi nhập vào bằng dấu phẩy thành list, xóa khoảng trắng thừa từng món
    #     emp['so_thich'] = [st.strip() for st in st_moi_str.split(",") if st.strip()]
    #     print("-> Đã cập nhật Sở thích.")

    # print(f"\n✔️ Cập nhật hoàn tất cho {update_id}!")
    # print("Thông tin mới:", employees[update_id])

else:
    print(f"Mã nhân viên {update_id} không tồn tại trên hệ thống!")


# # Xóa nhân viên theo mã 
input_delete_id = input("Nhập mã nhân viên muốn xóa: ").strip().upper()
if input_delete_id in employees:
    # Thêm bước hỏi lại để tránh người dùng bấm nhầm
    xac_nhan = input(f"Bạn có chắc chắn muốn XÓA nhân viên {input_delete_id} không? (y/n): ").strip().lower()
    
    if xac_nhan == "y":
        del employees[input_delete_id]
        print("✔️ Đã xóa thành công.")
    else:
        print("Đã hủy thao tác xóa, dữ liệu vẫn an toàn!")
else:
    print("❌ Không tìm thấy mã nhân viên cần xóa.")