# Technical Lesson: SQL JOINs

In almost all industry cases, rather than just working with a single table you will generally need data from multiple tables. Doing this requires the use of joins using shared columns from the two tables.

For example, take another look at the Northwinds database ERD (Entity Relationship Diagram):

![Northwinds database ERD](/assets/erm-data-orders.png)

While this practice database has 8 tables, it is not unusual in industry for a company to have databases with 20 or more tables. But the skills you are learning with “merely” 8 tables can be extended in a straightforward way to more tables than that since the process of using Joins is the same whether there are two or 200 tables.

For this lesson, let's say we need to generate a report that includes details about products from orders. To do that, we would need to take data from multiple tables in a single statement. We'll accomplish this by using JOIN in the following steps.

## Set Up

* Fork and Clone the GitHub Repo
* Install dependencies and enter the virtual environment:
    * `pipenv install`
    * `pipenv shell`

All your code will be in `main.py`. You can add any print statements needed to check your code and run the file with `python3 main.py`.

## Instructions

### Step 1: Connecting to the Database

In the code below, we import sqlite and pandas with the standard alias. Then we create a connection to the database `data.sqlite` and assign it to a variable:

```python
import sqlite3
import pandas as pd
conn = sqlite3.connect('data.sqlite')
```

### Step 2: Displaying Product Details Along with Order Details

In the code below, we select all records from `orderdetails` and `products` and join them using their common key `productCode` and display the first 10.

```python
q = """
SELECT *
 FROM orderdetails
      JOIN products
      ON orderdetails.productCode = products.productCode
      LIMIT 10;
"""
print(pd.read_sql(q, conn))
```

| # | orderNumber | productCode | quantityOrdered | priceEach | orderLineNumber | productCode | productName                               | productLine   | productScale | productVendor             | productDescription                                             | quantityInStock | buyPrice | MSRP   |
|---|-------------|-------------|------------------|-----------|------------------|-------------|--------------------------------------------|----------------|---------------|----------------------------|----------------------------------------------------------------|------------------|----------|--------|
| 0 | 10100       | S18_1749    | 30               | 136.00    | 3                | S18_1749    | 1917 Grand Touring Sedan                   | Vintage Cars   | 1:18          | Welly Diecast Productions | This 1:18 scale replica of the 1917 Grand Tour...             | 2724             | 86.70    | 170.00 |
| 1 | 10100       | S18_2248    | 50               | 55.09     | 2                | S18_2248    | 1911 Ford Town Car                         | Vintage Cars   | 1:18          | Motor City Art Classics   | Features opening hood, opening doors, opening ...             | 540              | 33.30    | 60.54  |
| 2 | 10100       | S18_4409    | 22               | 75.46     | 4                | S18_4409    | 1932 Alfa Romeo 8C2300 Spider Sport        | Vintage Cars   | 1:18          | Exoto Designs             | This 1:18 scale precision die cast replica fea...             | 6553             | 43.26    | 92.03  |
| 3 | 10100       | S24_3969    | 49               | 35.29     | 1                | S24_3969    | 1936 Mercedes Benz 500k Roadster           | Vintage Cars   | 1:24          | Red Start Diecast         | This model features grille-mounted chrome horn...             | 2081             | 21.75    | 41.03  |
| 4 | 10101       | S18_2325    | 25               | 108.06    | 4                | S18_2325    | 1932 Model A Ford J-Coupe                  | Vintage Cars   | 1:18          | Autoart Studio Design     | This model features grille-mounted chrome horn...             | 9354             | 58.48    | 127.13 |
| 5 | 10101       | S18_2795    | 26               | 167.06    | 1                | S18_2795    | 1928 Mercedes-Benz SSK                     | Vintage Cars   | 1:18          | Gearbox Collectibles      | This 1:18 replica features grille-mounted chro...             | 548              | 72.56    | 168.75 |
| 6 | 10101       | S24_1937    | 45               | 32.53     | 3                | S24_1937    | 1939 Chevrolet Deluxe Coupe                | Vintage Cars   | 1:24          | Motor City Art Classics   | This 1:24 scale die-cast replica of the 1939 C...             | 7332             | 22.57    | 33.19  |
| 7 | 10101       | S24_2022    | 46               | 44.35     | 2                | S24_2022    | 1938 Cadillac V-16 Presidential Limousine  | Vintage Cars   | 1:24          | Classic Metal Creations   | This 1:24 scale precision die cast replica of ...             | 2847             | 20.61    | 44.80  |
| 8 | 10102       | S18_1342    | 39               | 95.55     | 2                | S18_1342    | 1937 Lincoln Berline                       | Vintage Cars   | 1:18          | Motor City Art Classics   | Features opening engine cover, doors, trunk, a...             | 8693             | 60.62    | 102.74 |
| 9 | 10102       | S18_1367    | 41               | 43.13     | 1                | S18_1367    | 1936 Mercedes-Benz 500K Special Roadster   | Vintage Cars   | 1:18          | Studio M Art Models       | This 1:18 scale replica is constructed of heav...             | 8635             | 24.26    | 53.91  |

***display of first 10 records from orderdetails and products using join and common key***

### Step 3: Compare to the Individual Tables

Let’s consider some of the other tables.

`orderdetails` Table:

In the code below, we select all records from orderdetails and display the first 10
```python
q = """
SELECT *
 FROM orderdetails
 LIMIT 10;
"""
print(pd.read_sql(q, conn))
```

| # | orderNumber | productCode | quantityOrdered | priceEach | orderLineNumber |
|---|-------------|-------------|------------------|-----------|------------------|
| 0 | 10100       | S18_1749    | 30               | 136.00    | 3                |
| 1 | 10100       | S18_2248    | 50               | 55.09     | 2                |
| 2 | 10100       | S18_4409    | 22               | 75.46     | 4                |
| 3 | 10100       | S24_3969    | 49               | 35.29     | 1                |
| 4 | 10101       | S18_2325    | 25               | 108.06    | 4                |
| 5 | 10101       | S18_2795    | 26               | 167.06    | 1                |
| 6 | 10101       | S24_1937    | 45               | 32.53     | 3                |
| 7 | 10101       | S24_2022    | 46               | 44.35     | 2                |
| 8 | 10102       | S18_1342    | 39               | 95.55     | 2                |
| 9 | 10102       | S18_1367    | 41               | 43.13     | 1                |

***orderdetails Table***

`products` Table:

In the code below, we select all records from `products` and display the first 10

```python
q = """
SELECT *
 FROM products
 LIMIT 10;
"""
print(pd.read_sql(q, conn))
```

| Order Number | Product Code | Quantity Ordered | Price Each | Order Line Number | Product Name                              | Product Line  | Product Scale | Product Vendor             | Product Description                                                           | Quantity In Stock | Buy Price | MSRP   |
|--------------|--------------|------------------|-------------|--------------------|--------------------------------------------|----------------|----------------|-----------------------------|--------------------------------------------------------------------------------|--------------------|------------|--------|
| 10100        | S18_1749     | 30               | 136.00      | 3                  | 1917 Grand Touring Sedan                   | Vintage Cars   | 1:18           | Welly Diecast Productions  | This 1:18 scale replica of the 1917 Grand Touring Sedan...                   | 2724               | 86.70      | 170.00 |
| 10100        | S18_2248     | 50               | 55.09       | 2                  | 1911 Ford Town Car                         | Vintage Cars   | 1:18           | Motor City Art Classics    | Features opening hood, opening doors, opening trunk...                       | 540                | 33.30      | 60.54  |
| 10100        | S18_4409     | 22               | 75.46       | 4                  | 1932 Alfa Romeo 8C2300 Spider Sport        | Vintage Cars   | 1:18           | Exoto Designs              | This 1:18 scale precision die cast replica features...                        | 6553               | 43.26      | 92.03  |
| 10100        | S24_3969     | 49               | 35.29       | 1                  | 1936 Mercedes Benz 500k Roadster           | Vintage Cars   | 1:24           | Red Start Diecast          | This model features grille-mounted chrome horns...                            | 2081               | 21.75      | 41.03  |
| 10101        | S18_2325     | 25               | 108.06      | 4                  | 1932 Model A Ford J-Coupe                  | Vintage Cars   | 1:18           | Autoart Studio Design      | This model features grille-mounted chrome horns...                            | 9354               | 58.48      | 127.13 |
| 10101        | S18_2795     | 26               | 167.06      | 1                  | 1928 Mercedes-Benz SSK                     | Vintage Cars   | 1:18           | Gearbox Collectibles       | This 1:18 replica features grille-mounted chrome horns...                     | 548                | 72.56      | 168.75 |
| 10101        | S24_1937     | 45               | 32.53       | 3                  | 1939 Chevrolet Deluxe Coupe                | Vintage Cars   | 1:24           | Motor City Art Classics    | This 1:24 scale die-cast replica of the 1939 Chevrolet Deluxe Coupe...       | 7332               | 22.57      | 33.19  |
| 10101        | S24_2022     | 46               | 44.35       | 2                  | 1938 Cadillac V-16 Presidential Limousine  | Vintage Cars   | 1:24           | Classic Metal Creations    | This 1:24 scale precision die cast replica of the 1938 Cadillac...           | 2847               | 20.61      | 44.80  |
| 10102        | S18_1342     | 39               | 95.55       | 2                  | 1937 Lincoln Berline                       | Vintage Cars   | 1:18           | Motor City Art Classics    | Features opening engine cover, doors, trunk, and more...                     | 8693               | 60.62      | 102.74 |
| 10102        | S18_1367     | 41               | 43.13       | 1                  | 1936 Mercedes-Benz 500K Special Roadster   | Vintage Cars   | 1:18           | Studio M Art Models        | This 1:18 scale replica is constructed of heavy-gauge die-cast metal...       | 8635               | 24.26      | 53.91  |

***SQL Data Set: Order and Product Information***

### Step 4: The USING clause

A more concise way to join the tables, if the column name is identical, is the `USING` clause. Rather than saying `ON tableA.column = tableB.column` we can simply say `USING(column)`. Again, this only works if the column is identically named for both tables.

In the code below, we select all records in orderdetails and products and join them on productCode with the `USING()` clause, and return the first 10 records:

```python
q = """
SELECT *
 FROM orderdetails
   JOIN products
     USING(productCode)
 LIMIT 10;
"""
print(pd.read_sql(q, conn))
```

| # | orderNumber | productCode | quantityOrdered | priceEach | orderLineNumber | productName                               | productLine  | productScale | productVendor             | productDescription                                             | quantityInStock | buyPrice | MSRP   |
|---|-------------|-------------|------------------|-----------|------------------|--------------------------------------------|---------------|---------------|----------------------------|----------------------------------------------------------------|------------------|----------|--------|
| 0 | 10100       | S18_1749    | 30               | 136.00    | 3                | 1917 Grand Touring Sedan                   | Vintage Cars  | 1:18          | Welly Diecast Productions  | This 1:18 scale replica of the 1917 Grand Tour...             | 2724             | 86.70    | 170.00 |
| 1 | 10100       | S18_2248    | 50               | 55.09     | 2                | 1911 Ford Town Car                         | Vintage Cars  | 1:18          | Motor City Art Classics    | Features opening hood, opening doors, opening ...             | 540              | 33.30    | 60.54  |
| 2 | 10100       | S18_4409    | 22               | 75.46     | 4                | 1932 Alfa Romeo 8C2300 Spider Sport        | Vintage Cars  | 1:18          | Exoto Designs              | This 1:18 scale precision die cast replica fea...             | 6553             | 43.26    | 92.03  |
| 3 | 10100       | S24_3969    | 49               | 35.29     | 1                | 1936 Mercedes Benz 500k Roadster           | Vintage Cars  | 1:24          | Red Start Diecast          | This model features grille-mounted chrome horn...             | 2081             | 21.75    | 41.03  |
| 4 | 10101       | S18_2325    | 25               | 108.06    | 4                | 1932 Model A Ford J-Coupe                  | Vintage Cars  | 1:18          | Autoart Studio Design      | This model features grille-mounted chrome horn...             | 9354             | 58.48    | 127.13 |
| 5 | 10101       | S18_2795    | 26               | 167.06    | 1                | 1928 Mercedes-Benz SSK                     | Vintage Cars  | 1:18          | Gearbox Collectibles       | This 1:18 replica features grille-mounted chro...             | 548              | 72.56    | 168.75 |
| 6 | 10101       | S24_1937    | 45               | 32.53     | 3                | 1939 Chevrolet Deluxe Coupe                | Vintage Cars  | 1:24          | Motor City Art Classics    | This 1:24 scale die-cast replica of the 1939 C...             | 7332             | 22.57    | 33.19  |
| 7 | 10101       | S24_2022    | 46               | 44.35     | 2                | 1938 Cadillac V-16 Presidential Limousine  | Vintage Cars  | 1:24          | Classic Metal Creations    | This 1:24 scale precision die cast replica of ...             | 2847             | 20.61    | 44.80  |
| 8 | 10102       | S18_1342    | 39               | 95.55     | 2                | 1937 Lincoln Berline                       | Vintage Cars  | 1:18          | Motor City Art Classics    | Features opening engine cover, doors, trunk, a...             | 8693             | 60.62    | 102.74 |
| 9 | 10102       | S18_1367    | 41               | 43.13     | 1                | 1936 Mercedes-Benz 500K Special Roadster   | Vintage Cars  |_

***SQL Data Set: USING() clause***

### Step 5: More Aliasing

You can also assign tables an alias by entering an alternative shorthand name. This is slightly different than the previous lesson where we introduced aliases for column names, since now we are aliasing tables.

When aliasing columns the goal is usually to improve readability by giving something a more specific or easier-to-read name.

For example, `name AS employee_name`, `AVG(AVG) AS average_batting_average`, or `COUNT(*) AS num_products`.

When aliasing tables the goal is usually to shorten the name, in order to shorten the overall query. So typically, you'll see examples that alias a longer table name to a one-character or two-character shorthand. For example, `orderdetails AS od` or `products AS p`. (It is also possible to use aliases to clarify what exactly is in a table, like how aliases are used for columns, just less common.)

The following query produces the same result as the previous ones, using aliases `od` and `p` for `orderdetails` and `products`, respectively:

In `main.py`, type the following code to demonstrate the use of aliasing:

```python
q = """
SELECT *
 FROM orderdetails AS od
   JOIN products AS p
     ON od.productCode = p.productCode
 LIMIT 10;
"""
print(pd.read_sql(q, conn))
```

| # | Order Number | Product Code | Quantity Ordered | Price Each | Order Line Number | Product Code | Product Name                              | Product Line  | Product Scale | Product Vendor             | Product Description                                                           | Quantity In Stock | Buy Price | MSRP   |
|---|--------------|--------------|------------------|------------|-------------------|--------------|--------------------------------------------|----------------|----------------|-----------------------------|--------------------------------------------------------------------------------|--------------------|------------|--------|
| 0 | 10100        | S18_1749     | 30               | 136.00     | 3                 | S18_1749     | 1917 Grand Touring Sedan                   | Vintage Cars   | 1:18           | Welly Diecast Productions  | This 1:18 scale replica of the 1917 Grand Touring Sedan...                   | 2724               | 86.70      | 170.00 |
| 1 | 10100        | S18_2248     | 50               | 55.09      | 2                 | S18_2248     | 1911 Ford Town Car                         | Vintage Cars   | 1:18           | Motor City Art Classics    | Features opening hood, opening doors, opening trunk...                       | 540                | 33.30      | 60.54  |
| 2 | 10100        | S18_4409     | 22               | 75.46      | 4                 | S18_4409     | 1932 Alfa Romeo 8C2300 Spider Sport        | Vintage Cars   | 1:18           | Exoto Designs              | This 1:18 scale precision die cast replica features...                        | 6553               | 43.26      | 92.03  |
| 3 | 10100        | S24_3969     | 49               | 35.29      | 1                 | S24_3969     | 1936 Mercedes Benz 500k Roadster           | Vintage Cars   | 1:24           | Red Start Diecast          | This model features grille-mounted chrome horns...                            | 2081               | 21.75      | 41.03  |
| 4 | 10101        | S18_2325     | 25               | 108.06     | 4                 | S18_2325     | 1932 Model A Ford J-Coupe                  | Vintage Cars   | 1:18           | Autoart Studio Design      | This model features grille-mounted chrome horns...                            | 9354               | 58.48      | 127.13 |
| 5 | 10101        | S18_2795     | 26               | 167.06     | 1                 | S18_2795     | 1928 Mercedes-Benz SSK                     | Vintage Cars   | 1:18           | Gearbox Collectibles       | This 1:18 replica features grille-mounted chrome horns...                     | 548                | 72.56      | 168.75 |
| 6 | 10101        | S24_1937     | 45               | 32.53      | 3                 | S24_1937     | 1939 Chevrolet Deluxe Coupe                | Vintage Cars   | 1:24           | Motor City Art Classics    | This 1:24 scale die-cast replica of the 1939 Chevrolet Deluxe Coupe...       | 7332               | 22.57      | 33.19  |
| 7 | 10101        | S24_2022     | 46               | 44.35      | 2                 | S24_2022     | 1938 Cadillac V-16 Presidential Limousine  | Vintage Cars   | 1:24           | Classic Metal Creations    | This 1:24 scale precision die cast replica of the 1938 Cadillac...           | 2847               | 20.61      | 44.80  |
| 8 | 10102        | S18_1342     | 39               | 95.55      | 2                 | S18_1342     | 1937 Lincoln Berline                       | Vintage Cars   | 1:18           | Motor City Art Classics    | Features opening engine cover, doors, trunk, and much more...                | 8693               | 60.62      | 102.74 |
| 9 | 10102        | S18_1367     | 41               | 43.13      | 1                 | S18_1367     | 1936 Mercedes-Benz 500K Special Roadster   | Vintage Cars   | 1:18           | Studio M Art Models        | This 1:18 scale replica is constructed of heavy-gauge die-cast metal...       | 8635               | 24.26      | 53.91  |

***Product SQL Data Set: Using Aliases***

Note that just like with column aliases, the `AS` keyword is optional in SQLite. So, instead of `FROM orderdetails AS od` you could write `FROM orderdetails od` with the same outcome.

It is somewhat more common to see `AS` used with column aliases and skipped with table aliases, but again, you'll want to check the syntax rules of your particular type of SQL as well as style guidelines from your employer to know which syntax to use in a professional setting.

### Step 6: LEFT JOINs

By default a `JOIN` is an `INNER JOIN`, or the intersection between two tables. In other words, the `JOIN` between orders and products is only for `productCodes` that are in both the `orderdetails` and `products` tables. If a product had yet to be ordered (and wasn't in the `orderdetails` table) then it would also not be in the result of the `JOIN`.

The `LEFT JOIN` keyword returns all records from the left table (table1), and the matched records from the right table (table2). The result is `NULL` from the right side if there is no match.

There are many other types of joins (refer back to the image on the Defining SQL JOINs page). Of these, SQLite does not support outer joins, but it is good to be aware of as more powerful versions of SQL such as PostgreSQL support these additional functions.

For example, the statement `SELECT * FROM products LEFT JOIN orderdetails;` would return all products, even those that hadn't been ordered. You can imagine that all products in inventory should have a description in the `product` table, but perhaps not every product is represented in the `orderdetails` table.

In the cell below, we select all records from products and join them with all records in orderdetails on productcode using `LEFT JOIN`, then execute the query and store it in a dataframe named `df`:

```python
q = """
SELECT *
 FROM products
   LEFT JOIN orderdetails
     USING(productCode);
"""
df = pd.read_sql(q, conn)

print("Number of records returned:", len(df))
print("Number of records where order details are null:", len(df[df.orderNumber.isnull()]))
```
```
Number of records returned: 2997
Number of records where order details are null: 1
```

Let's take a look at the one record that has null values in the order details:
```python
print(df[df.orderNumber.isnull()])
``` 

| productCode | productName       | productLine  | productScale | ProductVendor             | productDescription                                              | quantityInStock | buyPrice | MSRP   | orderNumber | quantityOrdered | priceEach | orderLineNumber |
|-------------|-------------------|--------------|--------------|----------------------------|------------------------------------------------------------------|------------------|----------|--------|-------------|------------------|-----------|------------------|
| S18_3233    | 1985 Toyota Supra | Classic Cars | 1:18         | Highway 66 Mini Classics  | This model features soft rubber tires, working...               | 7733             | 57.01    | 107.57 | NaN         | NaN              | NaN       | NaN              |

***SQL data set: output of order details record with null values***

As you can see, it's a rare occurrence, but there is one product that has yet to be ordered.

### Step 7: Primary Versus Foreign Keys

Another important consideration when performing joins is to think more about the key or column you are joining on. As you'll see in upcoming lessons, this can lead to interesting behavior if the join value is not unique in one or both of the tables. In all of the above examples, you joined two tables using the primary key. The primary key(s) of a table are those column(s) which uniquely identify a row. You'll also see this designated in the schema diagram with the asterisk `*`. 

You can also join tables using foreign keys which are not the primary key for that particular table, but rather another table. For example, `employeeNumber` is the primary key for the employees table and corresponds to the salesRepEmployeeNumber of the customers table. In the customers table, `salesRepEmployeeNumber` is only a foreign key, and is unlikely to be a unique identifier, as it is likely that an employee serves multiple customers. As such, in the resulting view `employeeNumber` would no longer be a unique field.

In `main.py`, add the code below to join customers using the alias `c` with employees using the alias `e` on the foreign keys `salesRepEmployeeNumber` and `employeeNumber` and order the result by `employeeNumber`, then type the code to execute the query:

```python
q = """
SELECT *
 FROM customers AS c
      JOIN employees AS e
      ON c.salesRepEmployeeNumber = e.employeeNumber
      ORDER By employeeNumber;
"""
print(pd.read_sql(q, conn))
```

Notice that this also returned both columns: `salesRepEmployeeNumber` and `employeeNumber`. These columns contain identical values so you would probably actually only want to select one or the other.

```python
# Remember to close the connection when you are done
conn.close()
```

## Summary

In this lesson, you investigated joins. This included implementing the `ON` and `USING` clauses, aliasing table names, implementing `LEFT JOIN`, and using primary vs. foreign keys.

## Considerations

When using the four types of SQL JOINs (`INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN`) with SQLite in Python, it's important to be aware of certain pitfalls and limitations. Here's a summary of each `JOIN` type and the potential pitfalls when working with SQLite:

* `INNER JOIN`
  * Summary: Returns only the rows that have matching values in both tables.
  * Pitfalls:
    * Missing Matches: If there are no matches between the tables, the `INNER JOIN` will result in an empty set for that specific join, which might lead to data loss if not handled properly.
    * Unintended Data Reduction: If you mistakenly use an `INNER JOIN` when you should be using an outer join, you might unintentionally filter out important data.
* `LEFT JOIN` (or `LEFT OUTER JOIN`)
  * Summary: Returns all the rows from the left table and the matched rows from the right table. If there's no match, the result is `NULL` on the side of the right table.
  * Pitfalls:
    * NULL Handling: The result set will contain `NULL` values where there are no matches. If not handled carefully in subsequent logic or analysis, these `NULL` values can lead to incorrect results (e.g., misinterpreting the meaning of `NULL` values or failing to account for them in calculations).
    * Performance: `LEFT JOIN` can be less efficient than `INNER JOIN`, especially with large datasets, as they include more rows in the result set.
* `RIGHT JOIN` (or `RIGHT OUTER JOIN`)
  * Summary: Returns all the rows from the right table and the matched rows from the left table. If there's no match, the result is `NULL` on the side of the left table.
  * Pitfalls:
    * SQLite Limitation: SQLite does not natively support `RIGHT JOIN`. Attempting to use a `RIGHT JOIN` will result in an error. To achieve the same result, you would need to reverse the order of the tables and use a `LEFT JOIN`.
    * Workarounds Required: Since `RIGHT JOIN` isn't supported, you need to manually rewrite queries, which can introduce errors or misunderstandings in query logic.
* `FULL OUTER JOIN`
  * Summary: Returns all rows when there is a match in either left or right table. It combines the results of both `LEFT JOIN` and `RIGHT JOIN`.
  * Pitfalls:
    * SQLite Limitation: SQLite does not natively support `FULL OUTER JOIN`. Trying to use it directly in SQLite will cause an error.
    * Complex Workarounds: To achieve the effect of a `FULL OUTER JOIN`, you would need to use a combination of `LEFT JOIN` and `UNION` with an appropriate `RIGHT JOIN` logic. This can lead to more complex queries that are harder to maintain and debug.
    * Performance: The workaround queries (using `UNION` and multiple joins) can be less efficient and more challenging to optimize.
* General Pitfalls Across All Joins:
  * Ambiguity in Column Names: When joining tables, if columns with the same name exist in both tables, you need to explicitly specify the table name or alias to avoid ambiguity.
  * Incorrect Join Conditions: Ensure the join condition is correctly defined. A wrong or missing join condition might result in a Cartesian product (all possible combinations of rows), which can lead to large, unusable datasets.
  * Data Integrity: Be cautious about missing or mismatched data, especially when dealing with outer joins, as they can introduce `NULL` values or exclude important rows.
  * Performance: Joins can significantly impact the performance of queries, especially on large tables. Indexing and query optimization are crucial to avoid slow queries.

By being aware of these pitfalls and limitations, you can write more effective and efficient SQL queries when using SQLite in Python.

