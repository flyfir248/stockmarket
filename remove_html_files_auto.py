import os
import schedule
import time

def remove_html_files():
    folder_path = 'templates'

    for filename in os.listdir(folder_path):
        if filename.endswith('.html') and filename != 'index.html' and filename != 'plot.html':
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

def job():
    print("Running the script to remove HTML files...")
    remove_html_files()

# Schedule the job to run every hour
schedule.every().hour.do(job)

# Run the scheduled jobs indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)