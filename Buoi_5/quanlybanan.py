from lxml import etree

# Đọc file XML
tree = etree.parse("Buoi_5/quanlybanan.xml")

# 1. Lấy tất cả bàn
c01 = tree.xpath("/QUANLY/BANS/BAN")
print("\n# Lấy tất cả bàn")
for ban in c01:
    print(etree.tostring(ban, pretty_print=True, encoding='unicode'))

# 2. Lấy tất cả nhân viên
c02 = tree.xpath("/QUANLY/NHANVIENS/NHANVIEN")
print("\n# Lấy tất cả nhân viên")
for nv in c02:
    print(etree.tostring(nv, pretty_print=True, encoding='unicode'))

# 3. Lấy tất cả tên món
c03 = tree.xpath("/QUANLY/MONS/MON/TENMON/text()")
print("\n# Lấy tất cả tên món")
for tenmon in c03:
    print(tenmon)

# 4. Lấy tên nhân viên có mã NV02
c04 = tree.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV='NV02']/TENV/text()")
print("\n# Lấy tên nhân viên có mã NV02")
for t in c04:
    print(t)

# 5. Lấy tên và số điện thoại của nhân viên NV03
c05 = tree.xpath("concat(/QUANLY/NHANVIENS/NHANVIEN[MANV='NV03']/TENV, ' - ', /QUANLY/NHANVIENS/NHANVIEN[MANV='NV03']/SDT)")
print("\n# Lấy tên và số điện thoại của nhân viên NV03")
print(t)

# 6. Lấy tên món có giá > 50,000
c06 = tree.xpath("/QUANLY/MONS/MON[GIA>50000]/TENMON/text()")
print("\n# Lấy tên món có giá > 50,000")
for t in c06:
    print(t)

# 7. Lấy số bàn của hóa đơn HD03
c07 = tree.xpath("/QUANLY/HOADONS/HOADON[SOHD='HD03']/SOBAN/text()")
print("\n# Lấy số bàn của hóa đơn HD03")
for t in c07:
    print(t)

# 8. Lấy tên món có mã M02
c08 = tree.xpath("/QUANLY/MONS/MON[MAMON='M02']/TENMON/text()")
print("\n# Lấy tên món có mã M02")
for t in c08:
    print(t)

# 9. Lấy ngày lập của hóa đơn HD03
c09 = tree.xpath("/QUANLY/HOADONS/HOADON[SOHD='HD03']/NGAYLAP/text()")
print("\n# Lấy ngày lập của hóa đơn HD03")
for t in c09:
    print(t)

# 10. Lấy tất cả mã món trong hóa đơn HD01
c10 = tree.xpath("/QUANLY/HOADONS/HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON/text()")
print("\n# Lấy tất cả mã món trong hóa đơn HD01")
for t in c10:
    print(t)

# 11. Lấy tên món trong hóa đơn HD01
c11 = tree.xpath("/QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON]/TENMON/text()")
print("\n# Lấy tên món trong hóa đơn HD01")
for t in c11:
    print(t)

# 12. Lấy tên nhân viên lập hóa đơn HD02
c12 = tree.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOHD='HD02']/MANV]/TENV/text()")
print("\n# Lấy tên nhân viên lập hóa đơn HD02")
for t in c12:
    print(t)

# 13. Đếm số bàn
c13 = tree.xpath("count(/QUANLY/BANS/BAN)")
print("\n# Đếm số bàn")
print(int(c13))

# 14. Đếm số hóa đơn lập bởi NV01
c14 = tree.xpath("count(/QUANLY/HOADONS/HOADON[MANV='NV01'])")
print("\n# Đếm số hóa đơn lập bởi NV01")
print(int(c14))

# 15. Lấy tên tất cả món có trong hóa đơn của bàn số 2
c15 = tree.xpath("/QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON[SOBAN='2']/CTHDS/CTHD/MAMON]/TENMON/text()")
print("\n# Lấy tên tất cả món có trong hóa đơn của bàn số 2")
for t in c15:
    print(t)

# 16. Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3
c16 = tree.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOBAN='3']/MANV]/TENV/text()")
print("\n# Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3")
for t in c16:
    print(t)

# 17. Lấy tất cả hóa đơn mà nhân viên nữ lập
c17 = tree.xpath("/QUANLY/HOADONS/HOADON[MANV = /QUANLY/NHANVIENS/NHANVIEN[GIOITINH='Nữ']/MANV]/SOHD/text()")
print("\n# Lấy tất cả hóa đơn mà nhân viên nữ lập")
for t in c17:
    print(t)

# 18. Lấy tất cả nhân viên từng phục vụ bàn số 1
c18 = tree.xpath("/QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOBAN='1']/MANV]/TENV/text()")
print("\n# Lấy tất cả nhân viên từng phục vụ bàn số 1")
for t in c18:
    print(t)

# 19. Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn
c19 = tree.xpath("/QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON/CTHDS/CTHD[SOLUONG>1]/MAMON]/TENMON/text()")
print("\n# Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn")
for t in c19:
    print(t)

# 20. Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02'
c20 = tree.xpath("concat(/QUANLY/BANS/BAN[SOBAN = /QUANLY/HOADONS/HOADON[SOHD='HD02']/SOBAN]/TENBAN, ' - ', /QUANLY/HOADONS/HOADON[SOHD='HD02']/NGAYLAP)")
print("\n# Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02'")
print(t)
