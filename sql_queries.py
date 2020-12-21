
# CREATE Views

sales_cat_code_null_create= ("""CREATE VIEW IF NOT EXISTS sales.cat_code_null AS 
            SELECT category_id, category_code, brand 
            FROM sales.sales 
            WHERE category_code IS NULL""")

sales_cat_code_not_null_create = ("""CREATE VIEW IF NOT EXISTS sales.cat_code_not_null AS
            SELECT category_id, category_code, brand
            FROM sales.sales
            WHERE category_code IS NOT NULL""")

sales_week_45 = ("""CREATE VIEW IF NOT EXISTS sales.sales_week_45 AS 
            SELECT brand, DAYNAME(event_time) AS day, sum(price) AS Revenue FROM sales.sales
            WHERE event_type ='purchase' AND WEEKOFYEAR(event_time) = 45
            GROUP BY day, brand
            """)

sales_week_46 = ("""CREATE VIEW IF NOT EXISTS sales.sales_week_46 AS 
            SELECT brand, DAYNAME(event_time) AS day, sum(price) AS Revenue FROM sales.sales
            WHERE event_type ='purchase' AND WEEKOFYEAR(event_time) = 46
            GROUP BY day, brand
            """)

brand_cat_45 = ("""CREATE VIEW IF NOT EXISTS brand_cat_45 AS 
            SELECT brand, category_code, sum(price) AS Revenue FROM sales.sales
            WHERE event_type ='purchase' AND WEEKOFYEAR(event_time) = 45
            GROUP BY brand, category_code
            """)

brand_cat_46 = ("""CREATE VIEW IF NOT EXISTS brand_cat_46 AS 
            SELECT brand, category_code, sum(price) AS Revenue FROM sales.sales
            WHERE event_type ='purchase' AND WEEKOFYEAR(event_time) = 46
            GROUP BY brand, category_code
            """)


# QUERY LISTS

create_views = [sales_cat_code_null_create, sales_cat_code_not_null_create, sales_week_45, sales_week_46, brand_cat_45, brand_cat_46]
