from lxml import etree
import os
import mysql.connector
from mysql.connector import Error

def parse_xsd_and_validate():
    """
    Parse XSD file, create XMLSchema object and validate XML with XSD
    """
    try:
        # Đường dẫn đến các file
        xsd_file = "Buoi_6/tmdt.xsd"
        xml_file = "Buoi_6/tmdt.xml"
        
        # Kiểm tra xem file có tồn tại không
        if not os.path.exists(xsd_file):
            print(f"File XSD không tồn tại: {xsd_file}")
            return False, None
            
        if not os.path.exists(xml_file):
            print(f"File XML không tồn tại: {xml_file}")
            return False, None
        
        print("1. Đọc và parse file XSD...")
        # Đọc file XSD
        with open(xsd_file, 'r', encoding='utf-8') as f:
            xsd_content = f.read()
            print(f"Nội dung XSD đã được đọc ({len(xsd_content)} ký tự)")
        
        # Parse XSD content
        xsd_doc = etree.fromstring(xsd_content.encode('utf-8'))
        print("XSD đã được parse thành công")
        
        print("\n2. Tạo XMLSchema object từ XSD...")
        # Tạo XMLSchema object
        xmlschema = etree.XMLSchema(xsd_doc)
        print("XMLSchema object đã được tạo thành công")
        
        print("\n3. Đọc và parse file XML...")
        # Đọc và parse file XML
        xml_doc = etree.parse(xml_file)
        print("XML đã được parse thành công")
        
        print("\n4. Validation XML với XSD...")
        # Validate XML với XSD
        is_valid = xmlschema.validate(xml_doc)
        
        if is_valid:
            print("✅ XML hợp lệ theo XSD schema!")
            return True, xml_doc
        else:
            print("❌ XML không hợp lệ theo XSD schema!")
            print("Các lỗi validation:")
            for error in xmlschema.error_log:
                print(f"  - Dòng {error.line}: {error.message}")
            return False, None
        
    except etree.XMLSyntaxError as e:
        print(f"Lỗi cú pháp XML/XSD: {e}")
        return False, None
    except etree.XMLSchemaParseError as e:
        print(f"Lỗi parse XSD schema: {e}")
        return False, None
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return False, None

def connect_to_database():
    """
    Kết nối đến MySQL database
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='xml_tmdt',
            user='root',  # Thay đổi username của bạn
            password='root',  # Thay đổi password của bạn
            charset='utf8mb4'
        )
        
        if connection.is_connected():
            print("✅ Kết nối database thành công!")
            return connection
            
    except Error as e:
        print(f"❌ Lỗi kết nối database: {e}")
        # Thử tạo database nếu chưa tồn tại
        try:
            temp_connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                charset='utf8mb4'
            )
            cursor = temp_connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS tmdt_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            cursor.close()
            temp_connection.close()
            print("Database tmdt_db đã được tạo")
            
            # Thử kết nối lại
            return connect_to_database()
            
        except Error as create_error:
            print(f"❌ Không thể tạo database: {create_error}")
            return None

def create_tables(connection):
    """
    Tạo các bảng category và product nếu chưa tồn tại
    """
    try:
        cursor = connection.cursor()
        
        # Tạo bảng categories
        create_categories_table = """
        CREATE TABLE IF NOT EXISTS categories (
            id VARCHAR(50) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
        """
        
        # Tạo bảng products
        create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id VARCHAR(50) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            price DECIMAL(10,2) NOT NULL,
            currency VARCHAR(10) DEFAULT 'USD',
            stock INT DEFAULT 0,
            category_id VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
        ) ENGINE=InnoDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
        """
        
        cursor.execute(create_categories_table)
        cursor.execute(create_products_table)
        connection.commit()
        
        print("✅ Các bảng đã được tạo thành công!")
        cursor.close()
        return True
        
    except Error as e:
        print(f"❌ Lỗi tạo bảng: {e}")
        return False

def extract_data_with_xpath(xml_doc):
    """
    Sử dụng XPath để trích xuất dữ liệu từ XML
    """
    try:
        root = xml_doc.getroot()
        
        # Trích xuất categories
        categories = []
        category_elements = root.xpath('//categories/category')
        
        for i, category_elem in enumerate(category_elements):
            category_id = category_elem.get('id', f'cat_{i+1}')
            category_name = category_elem.text.strip() if category_elem.text else f'Category {i+1}'
            categories.append({
                'id': category_id,
                'name': category_name,
                'description': f'Description for {category_name}'
            })
        
        print(f"📋 Tìm thấy {len(categories)} categories:")
        for cat in categories:
            print(f"  - {cat['id']}: {cat['name']}")
        
        # Trích xuất products
        products = []
        product_elements = root.xpath('//products/product')
        
        for i, product_elem in enumerate(product_elements):
            product_id = product_elem.get('id', f'prod_{i+1}')
            category_ref = product_elem.get('categoryRef')
            
            # Lấy thông tin sản phẩm
            name_elem = product_elem.xpath('./name')[0] if product_elem.xpath('./name') else None
            description_elem = product_elem.xpath('./description')[0] if product_elem.xpath('./description') else None
            price_elem = product_elem.xpath('./price')[0] if product_elem.xpath('./price') else None
            stock_elem = product_elem.xpath('./stock')[0] if product_elem.xpath('./stock') else None
            
            product = {
                'id': product_id,
                'name': name_elem.text.strip() if name_elem is not None and name_elem.text else f'Product {i+1}',
                'description': description_elem.text.strip() if description_elem is not None and description_elem.text else None,
                'price': float(price_elem.text) if price_elem is not None and price_elem.text else 0.0,
                'currency': price_elem.get('currency', 'USD') if price_elem is not None else 'USD',
                'stock': int(stock_elem.text) if stock_elem is not None and stock_elem.text else 0,
                'category_id': category_ref
            }
            products.append(product)
        
        print(f"📦 Tìm thấy {len(products)} products:")
        for prod in products:
            print(f"  - {prod['id']}: {prod['name']} (${prod['price']} {prod['currency']})")
        
        return categories, products
        
    except Exception as e:
        print(f"❌ Lỗi trích xuất dữ liệu: {e}")
        return [], []

def insert_data_to_database(connection, categories, products):
    """
    Insert dữ liệu vào database
    """
    try:
        cursor = connection.cursor()
        
        # Xóa dữ liệu cũ (nếu có)
        cursor.execute("DELETE FROM products")
        cursor.execute("DELETE FROM categories")
        
        # Insert categories
        insert_category_query = """
        INSERT INTO categories (id, name, description) 
        VALUES (%s, %s, %s)
        """
        
        for category in categories:
            cursor.execute(insert_category_query, (
                category['id'],
                category['name'],
                category['description']
            ))
        
        print(f"✅ Đã insert {len(categories)} categories")
        
        # Insert products
        insert_product_query = """
        INSERT INTO products (id, name, description, price, currency, stock, category_id) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        
        for product in products:
            cursor.execute(insert_product_query, (
                product['id'],
                product['name'],
                product['description'],
                product['price'],
                product['currency'],
                product['stock'],
                product['category_id']
            ))
        
        print(f"✅ Đã insert {len(products)} products")
        
        connection.commit()
        cursor.close()
        
        print("✅ Tất cả dữ liệu đã được insert thành công!")
        return True
        
    except Error as e:
        print(f"❌ Lỗi insert dữ liệu: {e}")
        connection.rollback()
        return False

def display_database_data(connection):
    """
    Hiển thị dữ liệu từ database để kiểm tra
    """
    try:
        cursor = connection.cursor()
        
        print("\n" + "="*60)
        print("DỮ LIỆU TRONG DATABASE")
        print("="*60)
        
        # Hiển thị categories
        cursor.execute("SELECT * FROM categories")
        categories = cursor.fetchall()
        
        print("\n📋 CATEGORIES:")
        print("-" * 50)
        for cat in categories:
            print(f"ID: {cat[0]}, Name: {cat[1]}, Description: {cat[2]}")
        
        # Hiển thị products với join category
        cursor.execute("""
            SELECT p.id, p.name, p.description, p.price, p.currency, 
                   p.stock, c.name as category_name
            FROM products p
            LEFT JOIN categories c ON p.category_id = c.id
        """)
        products = cursor.fetchall()
        
        print("\n📦 PRODUCTS:")
        print("-" * 50)
        for prod in products:
            print(f"ID: {prod[0]}, Name: {prod[1]}")
            print(f"    Price: ${prod[3]} {prod[4]}, Stock: {prod[5]}")
            print(f"    Category: {prod[6] or 'No category'}")
            print(f"    Description: {prod[2] or 'No description'}")
            print()
        
        cursor.close()
        
    except Error as e:
        print(f"❌ Lỗi hiển thị dữ liệu: {e}")

if __name__ == "__main__":
    print("CHƯƠNG TRÌNH VALIDATION XML VỚI XSD VÀ INSERT VÀO DATABASE")
    print("="*70)
    
    # 1. Validation XML với XSD
    print("\n1. Validation XML với XSD:")
    is_valid, xml_doc = parse_xsd_and_validate()
    
    if not is_valid:
        print("❌ XML không hợp lệ. Dừng chương trình.")
        exit(1)
    
    # 2. Kết nối database
    print("\n2. Kết nối đến MySQL database:")
    connection = connect_to_database()
    
    if not connection:
        print("❌ Không thể kết nối database. Dừng chương trình.")
        exit(1)
    
    try:
        # 3. Tạo tables
        print("\n3. Tạo các bảng trong database:")
        if not create_tables(connection):
            print("❌ Không thể tạo bảng. Dừng chương trình.")
            exit(1)
        
        # 4. Trích xuất dữ liệu bằng XPath
        print("\n4. Trích xuất dữ liệu từ XML bằng XPath:")
        categories, products = extract_data_with_xpath(xml_doc)
        
        if not categories and not products:
            print("❌ Không có dữ liệu để insert.")
            exit(1)
        
        # 5. Insert dữ liệu vào database
        print("\n5. Insert dữ liệu vào database:")
        if insert_data_to_database(connection, categories, products):
            # 6. Hiển thị dữ liệu đã insert
            display_database_data(connection)
        
    finally:
        # Đóng kết nối
        if connection.is_connected():
            connection.close()
            print("\n🔐 Đã đóng kết nối database")
    
    print("\n" + "="*70)
    print("HOÀN THÀNH!")
    print("="*70)