<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html>
      <head>
        <title>Danh sách sinh viên</title>
        <style>
          table { border-collapse: collapse; width: 50%; }
          th, td { border: 1px solid #333; padding: 8px; text-align: left; }
          th { background-color: #f2f2f2; }
        </style>
      </head>
      <body>
        <!-- 1. Liệt kê thông tin của tất cả sinh viên gồm mã và họ tên -->
        <h2>Liệt kê thông tin của tất cả sinh viên gồm mã và họ tên</h2>
        <table>
          <tr>
            <th>Mã sinh viên</th>
            <th>Họ tên</th>
          </tr>
          <xsl:for-each select="/school/student">
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
            </tr>
          </xsl:for-each>
        </table>


        <!-- 2. Liệt kê danh sách sinh viên gồm mã, tên, điểm. Sắp xếp theo điểm giảm dần -->
        <h2>Liệt kê danh sách sinh viên gồm mã, tên, điểm (sắp xếp theo điểm giảm dần)</h2>
        <table>
          <tr>
            <th>Mã sinh viên</th>
            <th>Họ tên</th>
            <th>Điểm</th>
          </tr>
          <xsl:for-each select="/school/student">
            <xsl:sort select="grade" data-type="number" order="descending"/>
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="grade"/></td>
            </tr>
          </xsl:for-each>
        </table>


        <!-- 3. Hiển thị danh sách sinh viên sinh tháng gần nhau -->
        <h2>Danh sách sinh viên sinh tháng gần nhau</h2>
        <table>
          <tr>
            <th>STT</th>
            <th>Họ tên</th>
            <th>Ngày sinh</th>
          </tr>
          <xsl:for-each select="/school/student">
            <xsl:sort select="substring(date,6,2)" data-type="number"/>
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="date"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- 4. Hiển thị danh sách các khóa học có sinh viên học. Sắp xếp theo khóa học -->
        <h2>Danh sách các khóa học có sinh viên học (sắp xếp theo tên khóa học)</h2>
        <table>
          <tr>
            <th>Mã khóa học</th>
            <th>Tên khóa học</th>
          </tr>
          <xsl:for-each select="/school/course">
            <xsl:sort select="name"/>
            <xsl:if test="/school/enrollment[courseRef=current()/id]">
              <tr>
                <td><xsl:value-of select="id"/></td>
                <td><xsl:value-of select="name"/></td>
              </tr>
            </xsl:if>
          </xsl:for-each>
        </table>

        <!-- 5. Lấy danh sách sinh viên đăng ký khóa học "Hóa học 201" -->
        <h2>Danh sách sinh viên đăng ký khóa học "Hóa học 201"</h2>
        <table>
          <tr>
            <th>Mã sinh viên</th>
            <th>Họ tên</th>
          </tr>
          <xsl:for-each select="/school/enrollment[courseRef=/school/course[name='Hóa học 201']/id]">
            <tr>
              <td><xsl:value-of select="/school/student[id=current()/studentRef]/id"/></td>
              <td><xsl:value-of select="/school/student[id=current()/studentRef]/name"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- 6. Lấy danh sách sinh viên sinh năm 1997 -->
        <h2>Danh sách sinh viên sinh năm 1997</h2>
        <table>
          <tr>
            <th>Mã sinh viên</th>
            <th>Họ tên</th>
            <th>Ngày sinh</th>
          </tr>
          <xsl:for-each select="/school/student[starts-with(date,'1997')]">
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="date"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- 7. Thống kê danh sách sinh viên họ “Trần” -->
        <h2>Thống kê danh sách sinh viên họ “Trần”</h2>
        <table>
          <tr>
            <th>Mã sinh viên</th>
            <th>Họ tên</th>
          </tr>
          <xsl:for-each select="/school/student[starts-with(name,'Trần')]">
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
            </tr>
          </xsl:for-each>
        </table>

        
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>