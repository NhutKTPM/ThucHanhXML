<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>

    <xsl:template match="/">
        <html>
        <head>
            <title>Quản lý bàn ăn - Truy vấn dữ liệu</title>
            <style>
                table { border-collapse: collapse; margin-bottom: 30px; }
                th, td { border: 1px solid #333; padding: 6px 12px; }
                th { background: #eee; }
                h2 { margin-top: 40px; }
            </style>
        </head>
        <body>
            <!-- 1. Danh sách tất cả các bàn -->
            <h2>1. Danh sách tất cả các bàn</h2>
            <table>
                <tr>
                    <th>STT</th>
                    <th>Số bàn</th>
                    <th>Tên bàn</th>
                </tr>
                <xsl:for-each select="QUANLY/BANS/BAN">
                    <tr>
                        <td><xsl:value-of select="position()"/></td>
                        <td><xsl:value-of select="SOBAN"/></td>
                        <td><xsl:value-of select="TENBAN"/></td>
                    </tr>
                </xsl:for-each>
            </table>

            <!-- 2. Danh sách các nhân viên -->
            <h2>2. Danh sách các nhân viên</h2>
            <table>
                <tr>
                    <th>STT</th>
                    <th>Mã NV</th>
                    <th>Tên NV</th>
                    <th>SĐT</th>
                    <th>Địa chỉ</th>
                    <th>Giới tính</th>
                    <th>Username</th>
                </tr>
                <xsl:for-each select="QUANLY/NHANVIENS/NHANVIEN">
                    <tr>
                        <td><xsl:value-of select="position()"/></td>
                        <td><xsl:value-of select="MANV"/></td>
                        <td><xsl:value-of select="TENV"/></td>
                        <td><xsl:value-of select="SDT"/></td>
                        <td><xsl:value-of select="DIACHI"/></td>
                        <td><xsl:value-of select="GIOITINH"/></td>
                        <td><xsl:value-of select="USERNAME"/></td>
                    </tr>
                </xsl:for-each>
            </table>

            <!-- 3. Danh sách các món ăn -->
            <h2>3. Danh sách các món ăn</h2>
            <table>
                <tr>
                    <th>STT</th>
                    <th>Mã món</th>
                    <th>Tên món</th>
                    <th>Giá</th>
                    <th>Hình ảnh</th>
                </tr>
                <xsl:for-each select="QUANLY/MONS/MON">
                    <tr>
                        <td><xsl:value-of select="position()"/></td>
                        <td><xsl:value-of select="MAMON"/></td>
                        <td><xsl:value-of select="TENMON"/></td>
                        <td><xsl:value-of select="GIA"/></td>
                        <td><xsl:value-of select="HINHANH"/></td>
                    </tr>
                </xsl:for-each>
            </table>

            <!-- 4. Thông tin nhân viên NV02 -->
            <h2>4. Thông tin của nhân viên NV02</h2>
            <table>
                <tr>
                    <th>Mã NV</th>
                    <th>Tên NV</th>
                    <th>SĐT</th>
                    <th>Địa chỉ</th>
                    <th>Giới tính</th>
                    <th>Username</th>
                </tr>
                <xsl:for-each select="QUANLY/NHANVIENS/NHANVIEN[MANV='NV02']">
                    <tr>
                        <td><xsl:value-of select="MANV"/></td>
                        <td><xsl:value-of select="TENV"/></td>
                        <td><xsl:value-of select="SDT"/></td>
                        <td><xsl:value-of select="DIACHI"/></td>
                        <td><xsl:value-of select="GIOITINH"/></td>
                        <td><xsl:value-of select="USERNAME"/></td>
                    </tr>
                </xsl:for-each>
            </table>

            <!-- 5. Danh sách các món ăn có giá > 50,000 -->
            <h2>5. Danh sách các món ăn có giá &gt; 50,000</h2>
            <table>
                <tr>
                    <th>STT</th>
                    <th>Mã món</th>
                    <th>Tên món</th>
                    <th>Giá</th>
                </tr>
                <xsl:for-each select="QUANLY/MONS/MON[GIA &gt; 50000]">
                    <tr>
                        <td><xsl:value-of select="position()"/></td>
                        <td><xsl:value-of select="MAMON"/></td>
                        <td><xsl:value-of select="TENMON"/></td>
                        <td><xsl:value-of select="GIA"/></td>
                    </tr>
                </xsl:for-each>
            </table>

            <!-- 6. Thông tin hóa đơn HD03: tên nhân viên, số bàn, ngày lập, tổng tiền -->
            <h2>6. Thông tin hóa đơn HD03</h2>
            <table>
                <tr>
                    <th>Tên nhân viên phục vụ</th>
                    <th>Số bàn</th>
                    <th>Ngày lập</th>
                    <th>Tổng tiền</th>
                </tr>
                <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD03']">
                    <tr>
                        <td>
                            <xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=current()/MANV]/TENV"/>
                        </td>
                        <td><xsl:value-of select="SOBAN"/></td>
                        <td><xsl:value-of select="NGAYLAP"/></td>
                        <td><xsl:value-of select="TONGTIEN"/></td>
                    </tr>
                </xsl:for-each>
            </table>

            <!-- 7. Tên các món ăn trong hóa đơn HD02 -->
            <h2>7. Tên các món ăn trong hóa đơn HD02</h2>
            <table>
                <tr>
                    <th>STT</th>
                    <th>Tên món</th>
                </tr>
                <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD02']/CTHDS/CTHD">
                    <tr>
                        <td><xsl:value-of select="position()"/></td>
                        <td>
                            <xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/TENMON"/>
                        </td>
                    </tr>
                </xsl:for-each>
            </table>

            <!-- 8. Tên nhân viên lập hóa đơn HD02 -->
            <h2>8. Tên nhân viên lập hóa đơn HD02</h2>
            <table>
                <tr>
                    <th>Tên nhân viên</th>
                </tr>
                <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD02']">
                    <tr>
                        <td>
                            <xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=current()/MANV]/TENV"/>
                        </td>
                    </tr>
                </xsl:for-each>
            </table>

            <!-- 9. Đếm số bàn -->
            <h2>9. Đếm số bàn</h2>
            <table>
                <tr>
                    <th>Tổng số bàn</th>
                </tr>
                <tr>
                    <td>
                        <xsl:value-of select="count(QUANLY/BANS/BAN)"/>
                    </td>
                </tr>
            </table>

            <!-- 10. Đếm số hóa đơn lập bởi NV01 -->
            <h2>10. Đếm số hóa đơn lập bởi NV01</h2>
            <table>
                <tr>
                    <th>Số hóa đơn lập bởi NV01</th>
                </tr>
                <tr>
                    <td>
                        <xsl:value-of select="count(QUANLY/HOADONS/HOADON[MANV='NV01'])"/>
                    </td>
                </tr>
            </table>

            <!-- 11. Danh sách các món từng bán cho bàn số 2 -->
            <h2>11. Danh sách các món từng bán cho bàn số 2</h2>
            <table>
                <tr>
                    <th>STT</th>
                    <th>Tên món</th>
                </tr>
                <xsl:for-each select="QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON[SOBAN='2']/CTHDS/CTHD/MAMON]">
                    <xsl:sort select="TENMON"/>
                    <tr>
                        <td><xsl:value-of select="position()"/></td>
                        <td><xsl:value-of select="TENMON"/></td>
                    </tr>
                </xsl:for-each>
            </table>

            <!-- 12. Danh sách nhân viên từng lập hóa đơn cho bàn số 3 -->
            <h2>12. Danh sách nhân viên từng lập hóa đơn cho bàn số 3</h2>
            <table>
                <tr>
                    <th>STT</th>
                    <th>Tên nhân viên</th>
                </tr>
                <xsl:for-each select="QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOBAN='3']/MANV]">
                    <tr>
                        <td><xsl:value-of select="position()"/></td>
                        <td><xsl:value-of select="TENV"/></td>
                    </tr>
                </xsl:for-each>
            </table>

            <!-- 13. Các món ăn được gọi nhiều hơn 1 lần trong các hóa đơn -->
            <h2>13. Các món ăn được gọi nhiều hơn 1 lần trong các hóa đơn</h2>
            <table>
                <tr>
                    <th>STT</th>
                    <th>Tên món</th>
                    <th>Tổng số lần gọi</th>
                </tr>
                <xsl:for-each select="QUANLY/MONS/MON">
                    <xsl:variable name="mam" select="MAMON"/>
                    <xsl:variable name="tong" select="sum(/QUANLY/HOADONS/HOADON/CTHDS/CTHD[MAMON=$mam]/SOLUONG)"/>
                    <xsl:if test="$tong &gt; 1">
                        <tr>
                            <td><xsl:value-of select="position()"/></td>
                            <td><xsl:value-of select="TENMON"/></td>
                            <td><xsl:value-of select="$tong"/></td>
                        </tr>
                    </xsl:if>
                </xsl:for-each>
            </table>

            <!-- 14. Thông tin hóa đơn chi tiết tính tiền cho hóa đơn HD04 -->
            <h2>14. Thông tin hóa đơn chi tiết tính tiền cho hóa đơn HD04</h2>
            <table>
                <tr>
                    <th>STT</th>
                    <th>Mã món</th>
                    <th>Tên món</th>
                    <th>Đơn giá</th>
                    <th>Số lượng</th>
                    <th>Tiền</th>
                </tr>
                <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD04']/CTHDS/CTHD">
                    <xsl:variable name="mon" select="/QUANLY/MONS/MON[MAMON=current()/MAMON]"/>
                    <tr>
                        <td><xsl:value-of select="position()"/></td>
                        <td><xsl:value-of select="MAMON"/></td>
                        <td><xsl:value-of select="$mon/TENMON"/></td>
                        <td><xsl:value-of select="$mon/GIA"/></td>
                        <td><xsl:value-of select="SOLUONG"/></td>
                        <td>
                            <xsl:value-of select="number($mon/GIA) * number(SOLUONG)"/>
                        </td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>