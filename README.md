# FPDS Parser CLI

## Overview
The FPDS Parser CLI allows users to retrieve federal contract data from the FPDS Atom Feed. The parser supports retrieving data for a specific date or parsing all available data sequentially from **1960/01/01** onward. The data is stored in a database table (`parser_stage`) to track parsing status and ensure efficient updates.

---

## Setup

### **1. Configure `.env` File**
Before running the application, create a `.env` file in the root directory and configure your database settings:

```
# Choose database type (mysql, postgresql, sqlite)
DB_TYPE=mysql

# Database connection settings
DB_HOST=localhost
DB_PORT=8889
DB_NAME=fpds
DB_USER=root
DB_PASSWORD=root
```

### **2. Install Dependencies**
Make sure you have Python and `pip` installed. Then, install the required dependencies:

```sh
pip install -r requirements.txt
```

### **3. Run Migrations**
Initialize and apply database migrations:

```sh
alembic downgrade base && alembic upgrade head
```

This will create the necessary tables (`contracts` and `parser_stage`) in your database.

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
- Updates or inserts the parsed date in the `parser_stage` table:
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
- Iterates over each day, checking the `parser_stage` table to determine if the date was already processed.
- Downloads and stores each day's data as JSON in `/Users/iliaoborin/fpds/data/{year}/{MM_DD}.json`.
- Updates the `parser_stage` table after processing each day.
- If interrupted, the next run resumes from the last unprocessed date.

---

## Database Schema

### `parser_stage` Table
```sql
CREATE TABLE `parser_stage` (
    `id` BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `parsed_date` DATE NOT NULL,
    `file_path` VARCHAR(255) NOT NULL,
    `status` ENUM('pending', 'running', 'completed', 'failed') DEFAULT 'pending',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (`parsed_date`),
    INDEX (`file_path`),
    INDEX (`status`)
);
```

### `contracts` Table
```sql
CREATE TABLE `contracts` (
    `id` BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `piid` VARCHAR(255) NULL,
    `idv_piid` VARCHAR(255) NULL,
    `referenced_piid` VARCHAR(255) NULL,
    `mod_number` VARCHAR(255) NULL,
    `transaction_number` VARCHAR(255) NULL,
    `signed_date` DATE NULL,
    `effective_date` DATE NULL,
    `current_completion_date` DATE NULL,
    `obligated_amount` DECIMAL(15,2) NULL,
    `base_and_exercised_options_value` DECIMAL(15,2) NULL,
    `base_and_all_options_value` DECIMAL(15,2) NULL,
    `vendor_uei` VARCHAR(255) NULL,
    `naics_code` VARCHAR(255) NULL,
    `psc_code` VARCHAR(255) NULL,
    `contracting_office_agency_id` VARCHAR(255) NULL,
    `contracting_office_id` VARCHAR(255) NULL,
    `funding_requesting_agency_id` VARCHAR(255) NULL,
    `funding_requesting_office_id` VARCHAR(255) NULL,
    `number_of_offers_received` INT NULL,
    `extent_competed` VARCHAR(255) NULL,
    `file_path` VARCHAR(255) NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (`referenced_piid`),
    INDEX (`signed_date`),
    INDEX (`effective_date`),
    INDEX (`current_completion_date`),
    INDEX (`obligated_amount`),
    INDEX (`vendor_uei`),
    INDEX (`naics_code`),
    INDEX (`psc_code`)
);
```

---

## Execution Flow
1. **Check the database** (`parser_stage`) to determine the parsing status of a given date.
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

