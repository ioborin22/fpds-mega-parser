# FPDS Parser CLI

## Overview
The FPDS Parser CLI allows users to retrieve federal contract data from the FPDS Atom Feed. The parser supports retrieving data for a specific date or parsing all available data sequentially from **1960/01/01** onward. The data is stored in a database table (`fpds_parser`) to track parsing status and ensure efficient updates.

---

## Commands

### **1. Parse a Specific Date**
**Command:**
```sh
fpds parse YYYY/MM/DD
```
**Example:**
```sh
fpds parse 2023/01/01
```
This command:
- Fetches contract data for the specified date using `SIGNED_DATE=YYYY/MM/DD`.
- Stores the JSON output in the folder structure: `/Users/iliaoborin/fpds/data/{year}/{MM_DD}.json`.
- Updates or inserts the parsed date in the `fpds_parser` table:
  - If the date exists, it updates `last_run_at`.
  - If the date does not exist, it creates a new entry with `first_run_at` set to the current timestamp.

---

### **2. Parse All Available Data**
**Command:**
```sh
fpds parse all
```
This command:
- Starts parsing data sequentially from **1960/01/01** onward.
- Iterates over each day, checking the `fpds_parser` table to determine if the date was already processed.
- Downloads and stores each day's data as JSON in `/Users/iliaoborin/fpds/data/{year}/{MM_DD}.json`.
- Updates the `fpds_parser` table after processing each day.
- If interrupted, the next run resumes from the last unprocessed date.

---

## Database Schema (`fpds_parser` Table)
```sql
CREATE TABLE `fpds_parser` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `first_run_at` DATETIME NOT NULL,  -- Date of the first parsing run
    `status` VARCHAR(50) NOT NULL,     -- Parsing status (e.g., "pending", "completed", "error")
    `last_run_at` DATETIME DEFAULT NULL, -- Date of the last parsing run
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```
**Status Field Values:**
- `pending` - The date is scheduled for parsing.
- `in_progress` - The date is currently being parsed.
- `completed` - The data for this date has been successfully parsed.
- `error` - An issue occurred during parsing.

---

## Execution Flow
1. **Check the database** (`fpds_parser`) to determine the parsing status of a given date.
2. **If the date is not in the table:**
   - Insert a new record with `first_run_at = CURRENT_TIMESTAMP` and `status = 'pending'`.
3. **If the date exists but is not completed:**
   - Update `status = 'in_progress'` and attempt to fetch the data.
4. **Download the data** from FPDS using the `SIGNED_DATE=YYYY/MM/DD` parameter.
5. **Save the JSON file** in `/fpds/data/{year}/{MM_DD}.json`.
6. **Update the database**:
   - If parsing is successful, set `status = 'completed'` and update `last_run_at`.
   - If parsing fails, set `status = 'error'`.

---

## Example Usage
```sh
# Parse a specific date
fpds parse 2024/01/01

# Parse all available data from 1960/01/01 onward
fpds parse all
```

---

## Future Enhancements
- Implement multi-threaded downloading for improved efficiency.
- Add retry mechanisms for handling network failures.
- Create a web dashboard for monitoring parsing progress.

---

## Contact
For issues or contributions, please contact **iliaoborin@getwabinc.com** or submit a GitHub issue.

