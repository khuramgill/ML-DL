import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

# Database connection configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': '1life'
}

# Establish a connection to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Query to retrieve data
query = "SELECT id FROM users"
cursor.execute(query)

# Fetch all rows from the executed query
user_rows = cursor.fetchall()

# Query to retrieve donor data
query1 = "SELECT donor_id FROM blood_donors"
cursor.execute(query1)
donor_rows = cursor.fetchall()

# Close the database connection
cursor.close()
conn.close()

# Process the data
user_ids = [row[0] for row in user_rows]
donor_ids = [row[0] for row in donor_rows]

print(user_ids)
print(donor_ids)

# For this example, we will plot user IDs as x-axis values and donor IDs as y-axis values.
# However, you need to ensure that both lists have the same length or adjust accordingly.
if len(user_ids) != len(donor_ids):
    print("Warning: The number of user IDs and donor IDs do not match.")
    # Adjust the length to match for plotting
    min_length = min(len(user_ids), len(donor_ids))
    user_ids = user_ids[:min_length]
    donor_ids = donor_ids[:min_length]

# Convert data to numpy arrays for easier manipulation
x = np.array(user_ids)
y = np.array(donor_ids)

# Define color regions based on y-values
colors = np.where(y < 10, 'skyblue', np.where(y < 20, 'grey', 'pink'))

# Plot the bar chart with different colors
plt.figure(figsize=(10, 6))
plt.bar(x, y, color=colors)

# Additional customization
plt.title('Bar Chart with Different Colors')
plt.xlabel('User IDs')
plt.ylabel('Donor IDs')
plt.grid(True)

# Show the plot
plt.show()
