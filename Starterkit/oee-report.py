import sqlite3

# Connect to the database (replace "mydb.db" with your actual database file)
conn = sqlite3.connect("/opt/plcnext/logs/datalogger/OEEReport.db")
cursor = conn.cursor()

# Execute a query to fetch table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = [row[0] for row in cursor.fetchall()]

# Execute a query to fetch data (replace "SELECT * FROM mytable" with your actual query)
query = f"SELECT * FROM {table_names[0]}"
cursor.execute(query)
data = cursor.fetchall()

# Close the database connection
conn.close()

# Generate a report (replace this with your actual report generation logic)
report = "Timestamp,OEE\n"
for row in data:
    report += f"{row[0]},{row[2]}\n"

# Save the report to a file (replace "report.txt" with your desired file name)
with open("/opt/plcnext/projects/PCWE/Services/Ehmi/ehmi/oee-report.csv", "w") as f:
    f.write(report)

# Print a success message
print("Report generated and saved as oee-report.csv")
