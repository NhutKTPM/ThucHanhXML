from lxml import etree

# Đọc file XML
tree = etree.parse("Buoi_5/sv.xml")

# 1. Lấy tất cả sinh viên
c01 = tree.xpath("//student")
print("# Lấy tất cả sinh viên")
for s in c01:
    print(etree.tostring(s, pretty_print=True, encoding='unicode'))

# 2. Liệt kê tên tất cả sinh viên
c02 = tree.xpath("//student/name/text()")
print("\n# Liệt kê tên tất cả sinh viên")
for name in c02:
    print(name)

# 3. Lấy tất cả id của sinh viên
c03 = tree.xpath("//student/id/text()")
print("\n# Lấy tất cả id của sinh viên")
for sid in c03:
    print(sid)

# 4. Lấy ngày sinh của sinh viên có id = 'SV01'
c04 = tree.xpath("//student[id='SV01']/date/text()")
print("\n# Lấy ngày sinh của sinh viên có id = 'SV01'")
print(c04)

# 5. Lấy các khóa học
c05 = tree.xpath("//enrollment/course/text()")
print("\n# Lấy các khóa học")
for course in c05:
    print(course)

# 6. Lấy toàn bộ thông tin của sinh viên đầu tiên
c06 = tree.xpath("//student[1]")
print("\n# Lấy toàn bộ thông tin của sinh viên đầu tiên")
print(etree.tostring(c06[0], pretty_print=True, encoding='unicode'))

# 7. Lấy mã sinh viên đăng ký khóa học 'Vatly203'
c07 = tree.xpath("//enrollment[course='Vatly203']/studentRef/text()")
print("\n# Lấy mã sinh viên đăng ký khóa học 'Vatly203'")
for sid in c07:
    print(sid)

# 8. Lấy tên sinh viên học môn 'Toan101'
c08 = tree.xpath("//student[id=//enrollment[course='Toan101']/studentRef]/name/text()")
print("\n# Lấy tên sinh viên học môn 'Toan101'")
for name in c08:
    print(name)

# 9. Lấy tên sinh viên học môn 'Vatly203'
c09 = tree.xpath("//student[id=//enrollment[course='Vatly203']/studentRef]/name/text()")
print("\n# Lấy tên sinh viên học môn 'Vatly203'")
for name in c09:
    print(name)

# 10. Lấy ngày sinh của sinh viên có id='SV01'
c10 = tree.xpath("//student[id='SV01']/date/text()")
print("\n# Lấy ngày sinh của sinh viên có id='SV01'")
print(c10)

# 11. Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997
c11 = tree.xpath("//student[starts-with(date, '1997')]")
print("\n# Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997")
for s in c11:
    name = s.xpath("name/text()")[0]
    date = s.xpath("date/text()")[0]
    print(f"{name} - {date}")

# 12. Lấy tên của các sinh viên có ngày sinh trước năm 1998
c12 = tree.xpath("//student[number(substring(date,1,4)) < 1998]/name/text()")
print("\n# Lấy tên của các sinh viên có ngày sinh trước năm 1998")
for name in c12:
    print(name)

# 13. Đếm tổng số sinh viên
c13 = tree.xpath("count(//student)")
print("\n# Đếm tổng số sinh viên")
print(int(c13))

# 14. Lấy tất cả sinh viên chưa đăng ký môn nào
c14 = tree.xpath("//student[not(id = //enrollment/studentRef)]/name/text()")
print("\n# Lấy tất cả sinh viên chưa đăng ký môn nào")
for name in c14:
    print(name)

# 15. Lấy phần tử <date> anh em ngay sau <name> của SV01
c15 = tree.xpath("//student[id='SV01']/name/following-sibling::date[1]/text()")
print("\n# Lấy phần tử <date> anh em ngay sau <name> của SV01")
print(c15)

# 16. Lấy phần tử <id> anh em ngay trước <name> của SV02
c16 = tree.xpath("//student[id='SV02']/name/preceding-sibling::id[1]/text()")
print("\n# Lấy phần tử <id> anh em ngay trước <name> của SV02")
print(c16)

# 17. Lấy toàn bộ node <course> trong cùng một <enrollment> với studentRef='SV03'
c17 = tree.xpath("//enrollment[studentRef='SV03']/course/text()")
print("\n# Lấy toàn bộ node <course> trong cùng một <enrollment> với studentRef='SV03'")
for course in c17:
    print(course)

# 18. Lấy sinh viên có họ là “Trần”
c18 = tree.xpath("//student[starts-with(name, 'Trần')]/name/text()")
print("\n# Lấy sinh viên có họ là 'Trần'")
for name in c18:
    print(name)

# 19. Lấy năm sinh của sinh viên SV01
c19 = tree.xpath("substring(//student[id='SV01']/date, 1, 4)")
print("\n# Lấy năm sinh của sinh viên SV01")
print(c19)
