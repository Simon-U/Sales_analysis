# Analysing sales data

In the following project the e-commerce sales data will be analysed.
The data is stored in an Impala database running in a docker container.
Initial data exploration will be performed in a Jupyter notebook.


## Prerequisites

To work with the project the following technologies need to be installed:

 - Docker
 - Jupyter Notebook
          
To run the code successfully in the notebook the following packages need to be installed with the pip install command:

```
import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np
import impala as ip
```
To start the docker container with the database navigate in the console to the folder of the project and run

```
docker-compose up
```

The database can be accessed by attaching to the container and running the command:

```
impala-shell
```
Issue:
Sometimes the container is set up properly but after running the impala-shell command one cannot connect. So far, the reason is unknown, but a proper connection can be established with restarting the container (1-3 times).

## Data sources and table structure

The data is from Kaggle and can be found under the following link:

https://www.kaggle.com/mkechinov/ecommerce-behavior-data-from-multi-category-store

The data is preloaded in the docker container and available there in the database sales and table sales.

The table and underlying data have the following structure:



| name          | type      | comment |
|---------------| ----------|---------|
| event_time    | timestamp |         |
| event_type    | string    |         |
| product_id    | bigint    |         |
| category_id   | bigint    |         |
| category_code | string    |         |
| brand         | string    |         |
| price         | double    |         |
| user_id       | bigint    |         |
| user_session  | string    |         |

The following steps were used to create the table:


 1. Transform the csv into parquet file ina Jupyter notebook
 2. Import the data file into the container
    ```
    docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH
    ```
 3. Create the database in Impala
 
    ``` 
    CREATE DATABASE sales;
    ```
 4. Create the table
 
    ```
    CREATE TABLE sales.sales (
    event_time TIMESTAMP,
    event_type STRING,
    product_id BIGINT,
    category_id BIGINT,
    category_code STRING,
    brand STRING,
    price DOUBLE,
    user_id BIGINT,
    user_session STRING)
    STORED AS PARQUET;
    ```
            
 5. Move the parquet file into the table directory using hdfs
 
    ```
    hdfs dfs -put *file path* *table path*
    ```


After the first analysis an update on the data might be necessary to handle missing values appropriately or to add additional columns. 


## Ideas

- Interesting could be a cart rate. How much and what from the cart got purchased at the end. And how long did it stay in the  cart.
- Same from view to cart or purchase.
- These could be analysed by user, category or brand



## Authors

* **Simon Unterbusch**