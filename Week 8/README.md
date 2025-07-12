# 🎉 Welcome to Week 8 – Final Assignment  
### Celebal Technologies Summer Internship – Data Engineering Track

This is my final project for **Week 8** of the internship at **Celebal Technologies**.  
In this assignment, I explored and analyzed the **NYC Yellow Taxi Trip dataset (Jan 2020)** using **Apache Spark with Azure Synapse**.

---

## ⚠️ Important Note – Please Read First!

> ⚠️ **Why Synapse and not Databricks?**  
> While **Azure Databricks** offers a 14-day free trial, it's **not included** under **Azure for Students**.  
> Students **cannot create compute clusters** using free credits on Databricks.  
> So instead of Databricks DBFS, I used **Azure Synapse Analytics**, which supports **Apache Spark notebooks** and is available under the student plan.

> ✅ Synapse worked great for loading the data, processing with PySpark, and storing results as Parquet files on ADLS Gen2.

---

## 🧰 What This Project Does

- ✅ Uploads NYC Taxi CSV dataset to **Azure Data Lake Gen2**
- ✅ Reads and processes it in **Azure Synapse notebook**
- ✅ Performs **7 analytical queries** using **PySpark**
- ✅ Saves each query output as a **Parquet file**
- ✅ Stores configuration as **JSON files**
- ✅ Takes screenshots to show outputs and steps

---

## 📂 Folder Structure

```plaintext
Week 8/
├── NYC_Taxi_Data_Analysis_Azure_Synapse_PySpark.ipynb   <- Final notebook
├── README.md                                            <- You're here!
├── JSON_Files/
│   ├── saptadipnyctaxi.json
│   └── linkedService_adls.json
├── Screenshots/
│   ├── 01_synapse_workspace_created.png
│   ├── 02_file_uploaded_to_raw_folder.png
│   ├── 03_spark_pool_started.png
│   ├── 04_cell1_df_loaded_and_printschema.png
│   ├── 05_cell2_revenue_column_and_output.png
│   ├── 06_cell3_passenger_by_area_output.png
│   ├── 07_cell4_vendor_average_output.png
│   ├── 08_cell5_payment_type_moving_count.png
│   ├── 09_cell6_top_2_vendors_on_date.png
│   ├── 10_cell7_popular_routes_output.png
│   ├── 11_cell8_pickup_hotspots_output.png
│   ├── 12_cell9_saving_to_parquet.png
│   └── 13_parquet_files_in_adls_processed.png
```

---

## 🧪 Step-by-Step Execution (with Screenshots)

### 1️⃣ Created Synapse Workspace  
![01 Synapse Created](Week%208/Screenshots/01_synapse_workspace_creation.png)

---

### 2️⃣ Uploaded Dataset to ADLS Gen2  
![02 File Uploaded](Week%208/Screenshots/02_file_uploaded_to_raw.png)

---

### 3️⃣ Started Spark Pool in Synapse  
![03 Spark Pool](Week%208/Screenshots/03_spark_pool_started.png)

---

### 4️⃣ Loaded Data into DataFrame and Printed Schema  
![04 Print Schema](Week%208/Screenshots/04_cell1_df_loaded_and_printschema.png)

---

### 5️⃣ Added Revenue Column to DataFrame  
![05 Revenue Column](Week%208/Screenshots/05_cell2_revenue_column_and_output.png)

---

### 6️⃣ Passenger Count by Pickup & Dropoff Location  
![06 Passenger Area](Week%208/Screenshots/06_cell3_passenger_by_area_output.png)

---

### 7️⃣ Average Fare and Earnings by Vendor  
![07 Vendor Stats](Week%208/Screenshots/07_cell4_vendor_average_output.png)

---

### 8️⃣ Moving Count of Payment Types  
![08 Payment Count](Week%208/Screenshots/08_cell5_payment_type_moving_count.png)

---

### 9️⃣ Top 2 Vendors by Revenue on a Given Date  
![09 Top Vendors](Week%208/Screenshots/09_cell6_top_2_vendors_on_date.png)

---

### 🔟 Most Popular Route (Pickup → Dropoff)  
![10 Popular Routes](Week%208/Screenshots/10_cell7_popular_routes_output.png)

---

### 🔁 Pickup Hotspots in Last 10 Seconds  
![11 Pickup Hotspots](Week%208/Screenshots/11_cell8_pickup_hotspots_output.png)

---

### 💾 Saved Results as Parquet Files to ADLS  
![12 Parquet Save](Week%208/Screenshots/12_cell9_saving_to_parquet.png)

---

### 📂 Processed Parquet Data in ADLS Gen2  
![13 Processed Folder](Week%208/Screenshots/13_parquet_files_in_adls_processed.png)

---

## 📘 Main Notebook File

- 📓 [NYC_Taxi_Data_Analysis_Azure_Synapse_PySpark.ipynb](Week%208/NYC_Taxi_Data_Analysis_Azure_Synapse_PySpark.ipynb)

---

## 🧾 JSON Configuration Files

Stored inside [`JSON_Files/`](Week%208/JSON_Files/):

- [saptadipnyctaxi.json](Week%208/JSON_Files/saptadipnyctaxi.json)
- [linkedService_adls.json](Week%208/JSON_Files/linkedService_adls.json)

These were exported from Synapse Studio to track linked services and workspace.

---

## 📊 Queries Performed

| Query # | Task |
|--------|------|
| Q1 | Add a new column `Revenue` (sum of fare + taxes + surcharges) |
| Q2 | Count of total passengers by Pickup & Dropoff area |
| Q3 | Average fare, total amount & revenue per Vendor |
| Q4 | Moving payment count by payment type (by minute) |
| Q5 | Top 2 vendors on 2020-01-15 by revenue, distance, and passengers |
| Q6 | Most common pickup → dropoff route by passenger count |
| Q7 | Real-time pickup hotspots in last 10 seconds |
| Q8 | Save all query outputs as Parquet to ADLS Gen2 |

---

## 🙋🏻‍♂️ Author

**Saptadip Das**  
_Data Engineering Intern – Celebal Technologies (Summer 2025)_

> Thanks for visiting this repo! If you found this project helpful or inspiring, feel free to ⭐️ star it or fork for your own learning.

---
