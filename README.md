# 📊 Accounting Automation: Bank Reconciliation & Journal Entry Generator

**A Python-powered tool that automates month-end bank reconciliations, matches transactions to the general ledger, and flags exceptions for review.**

---

## 📌 Project Overview

Manual bank reconciliations are time-consuming and error-prone. This project automates the process by:

- ✅ Reading bank transactions and general ledger entries from a single Excel file
- ✅ Automatically matching transactions based on amount
- ✅ Flagging unmatched transactions (exceptions) for review
- ✅ Generating a draft journal entry for suspense accounts
- ✅ Exporting a clean reconciliation report to Excel

**Time Saved:** Reduces a 30-minute manual reconciliation to a **5-second script execution**.

---

## 🤖 How It Works (The Logic)

The script uses Python (Pandas) to perform a **merge operation** on the Bank and GL datasets:

| Step | Action |
| :--- | :--- |
| 1 | Loads Bank and GL data from `accounting_data.xlsx` |
| 2 | Cleans amounts (handles positive/negative signs) |
| 3 | Performs an outer join to find matches and exceptions |
| 4 | Flags unmatched items for accountant review |
| 5 | Generates a proposed journal entry for the exception |
| 6 | Exports a clean Excel report with two tabs |

---

## 🔍 How to Find Unmatched Transactions (Two Methods)

### Method 1: Console Output (Real-Time)

When you run the script, it immediately prints the exceptions:



---

### Method 2: Excel Report (Audit Trail)

Open `reconciliation_report.xlsx` and go to the **`Exceptions_Review`** tab:

| Date_x | Description | Amount_x | _merge |
| :--- | :--- | :--- | :--- |
| 2025-01-22 | UNKNOWN TRANSACTION | 75.0 | left_only |

*The `left_only` flag means this transaction exists in the Bank statement but not in the General Ledger.*

---

## 📝 Sample Journal Entry for the Exception

When an unknown transaction is found, the script suggests this entry:



*This keeps the books balanced while the accounting team investigates.*

---

## 🛠️ Tools Used

| Tool | Purpose |
| :--- | :--- |
| **Python (Pandas)** | Data cleaning, merging, and analysis |
| **Excel** | Source data storage and output reporting |
| **GitHub** | Version control and portfolio hosting |

---

## 📁 File Structure


---

## 🗣️ How to Use This Portfolio in an Interview

This project demonstrates:

| Skill | How It's Shown |
| :--- | :--- |
| **Automation** | Replacing manual Excel work with Python |
| **Accounting Knowledge** | Understanding reconciliation, journal entries, suspense accounts |
| **Internal Controls** | Flagging exceptions for human review (audit trail) |
| **Efficiency** | Reducing month-end close time by 90% |
| **Dual Reporting** | Providing both real-time (console) and documented (Excel) outputs |

---

## 📚 Data Source

All data is **dummy/simulated** data created for portfolio demonstration purposes.

---

*Built by **Biman Kalita** | For Accounting & Finance Portfolio*
