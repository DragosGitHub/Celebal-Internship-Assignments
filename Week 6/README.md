# 🚀 Celebal Internship — Week 6 Assignment: Azure Data Factory

Welcome to my Week 6 assignment for the Celebal Technologies Internship! 🌐  
This week was packed with real-world **data integration and automation** tasks using **Azure Data Factory (ADF)**, focusing on securely moving data from local/on-premises environments and external servers into cloud-based analytics systems.

This assignment is broken down into **five mini-projects**, each targeting a critical data engineering scenario. The learnings, troubleshooting, and hands-on exploration made it one of the most rewarding weeks so far!

---

## 📌 Problem Statements

Here’s a breakdown of the tasks assigned:

### 🔷 Problem 01: SHIR — Load Local Server Data into Azure SQL
Set up **Self-hosted Integration Runtime (SHIR)** in ADF to securely extract data from a **local file server** and load it into an **Azure SQL Database**.

### 🔷 Problem 02: SFTP to Azure SQL Pipeline
Configure an **SFTP server**, upload files via FileZilla, and use ADF to **extract those files** and load them into Azure SQL.

### 🔷 Problem 03: Incremental Load Pipeline (Daily)
Create a **daily incremental pipeline** using a **watermark table** and **stored procedure** logic to process only new or updated data.

### 🔷 Problem 04: Monthly Trigger — Last Saturday of Month
Set up a custom **scheduled trigger** that runs the pipeline automatically on the **last Saturday of each month**.

### 🔷 Problem 05: Retry Logic / Fail-safe Pipeline
Implement **retry policies** and fail-safe mechanisms to gracefully handle **transient errors** and ensure resilience in pipeline execution.

---

## 🛠️ Solution Overview

Each problem was tackled using native features of **Azure Data Factory**, supported by manual setup in tools like Excel, FileZilla, and Notepad.

### ✅ SHIR Setup and Local File Copy
- Installed **Self-hosted Integration Runtime** on a local system.
- Created a **File System Linked Service** pointing to a shared local folder.
- Used **Copy Activity** to push data into Azure SQL.
- 🔗 Stored passwords securely via SHIR and verified connectivity.
- 💡 Used test connection & monitored status before running the pipeline.

### ✅ SFTP Integration
- Installed and configured an **SFTP server** (OpenSSH).
- Connected using **FileZilla** to upload files to `/upload`.
- Created a dataset in ADF pointing to the SFTP path.
- Designed pipeline to pull and push to SQL using mappings.

### ✅ Incremental Load Pipeline
- Created a `watermark_table` and `usp_MergeTransactions` stored procedure.
- Designed a lookup activity to fetch the `last_loaded_date`.
- Used a filter in source to only load data **greater than watermark date**.
- Successfully handled inserts and updates via **Upsert** logic.

### ✅ Monthly Scheduled Trigger
- Configured a custom trigger using **Advanced Recurrence** settings.
- Set to fire **only on the last Saturday** of each month at `00:05 IST`.
- Bound the trigger to the main pipeline and tested successfully.

### ✅ Retry and Fault Tolerance
- Set **Retry Count = 3** and **Retry Interval = 60 seconds** for all critical activities.
- Ensured failures due to temporary issues were retried automatically.
- Improved stability and reduced manual intervention needs.

---

## 📸 Screenshots & Demonstrations
Each problem statement also has its own subfolder with:
- 💻 JSON Files (pipelines, triggers, linked services)
- 📷 Key screenshots
- 📄 Individual README with explanation

---

## 🧠 Challenges Faced & How I Solved Them

| Challenge | How I Solved It |
|----------|------------------|
| SHIR path not accessible | Fixed network path `\\DevNexus\SHIRData`, ensured sharing & firewall access |
| SQL Firewall | Whitelisted the integration runtime IP in **SQL Server networking** |
| Duplicate primary key error | Switched to **upsert logic** and used watermark filter |
| Retry logic config error | Updated `retryIntervalInSeconds` to valid range (min 30s) |
| SFTP upload confusion | Used **FileZilla** and verified upload location `/upload` |
| Trigger timing issues | Converted UTC time to IST manually and adjusted to `00:05` |
| JSON export confusion | Located each component’s export in ADF Manage → Export |

---

## 💼 Folder Structure

```bash
Celebal-Internship-Assignments/
└── Week 6/
    ├── Problem-01_SHIR-Local-to-SQL/
    ├── Problem-02_SFTP-to-SQL/
    ├── Problem-03_Incremental-Load-Daily/
    ├── Problem-04_Last-Saturday-Trigger/
    ├── Problem-05_Retry-Logic-Fail-Safe/
    ├── Datasets/
    │   ├── transactions.csv
    │   ├── watermark_table.csv
    └── README.md ← This file
