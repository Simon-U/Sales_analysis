# Analysing sales data

In the following project the e-commerce sales data will be analysed.
The data is stored in an Impala database running in a docker container.
Initial data exploration will be performed in a jupiter notebook.


## Prerequisites

To work with the project the following technologies need to be installed:

 - Docker
 - Jupiter Notebook
          
To run the code sucessfully in the notebook the following packages need to be installed with the pip install command:

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

## Data sources and table structure

The data ist from Kaggle and can be found under the following link:

https://www.kaggle.com/mkechinov/ecommerce-behavior-data-from-multi-category-store

The data is pre loaded in the docker container and available there in the database sales and table sales.

The table and underlying data have the following structure:



| name          | type      | comment |
|---------------| ----------|---------|
| event_time    | timestamp |         |
| event_type    | string    |         |
| product_id    | bigint    |         |
| category_id   | bigint    |         |
| category_code | string    |         |
| brand         | string    |         |
| price         | double    |         |
| user_id       | bigint    |         |
| user_session  | string    |         |

The following steps were used to create the table:


 1. Transform the csv into parquet file ina jupiter notebook
 2. Import the data file into the container
 
    ```docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH```
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
 
             ```hdfs dfs -put *file path* *table path*```


After the first analysis an update on the data might be neccessary to handle missing values appropriately or to add additional columns. 

## Next steps

After the inital set up of the environment the analysis will be performed via SQL and the jupiter notebook.



## Authors

* **Simon Unterbusch**

