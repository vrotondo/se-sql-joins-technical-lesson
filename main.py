# Step 1
import sqlite3
import pandas as pd
conn = sqlite3.connect('data.sqlite')

# Step 2
q = """
SELECT *
 FROM orderdetails
      JOIN products
      ON orderdetails.productCode = products.productCode
      LIMIT 10;
"""
# print(pd.read_sql(q, conn))

# Step 3
# orderDetails table
q = """
SELECT *
 FROM orderdetails
 LIMIT 10;
"""
# print(pd.read_sql(q, conn))

# products table
q = """
SELECT *
 FROM products
 LIMIT 10;
"""
# print(pd.read_sql(q, conn))

# Step 4
q = """
SELECT *
 FROM orderdetails
   JOIN products
     USING(productCode)
 LIMIT 10;
"""
# print(pd.read_sql(q, conn))

# Step 5
q = """
SELECT *
 FROM orderdetails AS od
   JOIN products AS p
     ON od.productCode = p.productCode
 LIMIT 10;
"""
# print(pd.read_sql(q, conn))

# Step 6
q = """
SELECT *
 FROM products
   LEFT JOIN orderdetails
     USING(productCode);
"""
df = pd.read_sql(q, conn)

# print("Number of records returned:", len(df))
# print("Number of records where order details are null:", len(df[df.orderNumber.isnull()]))

# Step 7
q = """
SELECT *
 FROM customers AS c
      JOIN employees AS e
      ON c.salesRepEmployeeNumber = e.employeeNumber
      ORDER By employeeNumber;
"""
print(pd.read_sql(q, conn))

conn.close()