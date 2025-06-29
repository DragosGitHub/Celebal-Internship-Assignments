# 📅 Problem 04: Last Saturday of the Month Trigger

This module explains how I configured a **custom time-based trigger** in Azure Data Factory to automatically run a pipeline on the **last Saturday of every month**—a common scheduling requirement for periodic reporting or batch jobs.

---

## 📌 Problem Statement

> **Automate a Pipeline to Trigger Every Last Saturday of the Month:**  
Configure a custom time-based trigger in Azure Data Factory to run the pipeline on the last Saturday of each month. This supports periodic reporting and batch processing without manual intervention.

---

## 🛠️ Components Used

- **Azure Data Factory**
- **Custom Time-Based Trigger**
- **Trigger Type**: Schedule
- **Recurrence Rule**: Monthly → Last Saturday

---

## 🔧 Implementation Steps

### ✅ Step 1: Create the Trigger

I created a **Scheduled Trigger** in Azure Data Factory with the following recurrence settings:

- **Frequency**: Every 1 month
- **Advanced Options**:
  - **Recur every**: Last
  - **Day**: Saturday
- **Execution Time**: 00:05 AM IST

📸 ![Trigger Published](./last-saturday-trigger-published.png)

📝 [View Trigger JSON](./LastSaturdayTrigger.json)

---

## 📦 Folder Contents

| File | Description |
|------|-------------|
| `last-saturday-trigger-published.png` | Screenshot of the published trigger |
| `LastSaturdayTrigger.json` | JSON configuration for the scheduled trigger |
| `README.md` | This documentation file |

---

## 💡 Challenges & Solutions

- ❗ **No Native “Last Day” Picker**: Azure doesn’t provide direct options like "last Saturday". Solved using **Advanced Recurrence Options** in the trigger configuration.
- ❗ **Execution Time Confusion**: Set to 00:05 IST to avoid overlap with daily triggers.

---

## ✅ Outcome

- The pipeline now **automatically runs on the last Saturday** of each month without any manual trigger.
- This ensures timely execution of month-end reporting or batch jobs.

---

> _This concludes Problem Statement 04 of the Celebal Internship Week 6 assignment._

---
