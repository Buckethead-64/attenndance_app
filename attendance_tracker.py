import datetime
import csv
import pandas as pd

class AttendanceTracker:
    def __init__(self, filename='attendance.csv'):
        self.filename = filename

    def mark_attendance(self, name):
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([datetime.date.today(), name])

    def view_daily_logs(self):
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                logs = list(reader)
                today = datetime.date.today()
                daily_logs = [log for log in logs if log[0] == str(today)]
                return daily_logs
        except FileNotFoundError:
            return []

    def view_monthly_report(self):
        try:
            df = pd.read_csv(self.filename, header=None)
            df.columns = ['Date', 'Name']
            df['Date'] = pd.to_datetime(df['Date'])
            df['Month'] = df['Date'].dt.month
            monthly_report = df.groupby('Month')['Name'].count().reset_index()
            return monthly_report
        except FileNotFoundError:
            return pd.DataFrame()
          def main():
    tracker = AttendanceTracker()

    while True:
        print("\nAttendance Tracker Menu:")
        print("1. Mark Attendance")
        print("2. View Daily Logs")
        print("3. View Monthly Report")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            tracker.mark_attendance(name)
            print("Attendance marked successfully!")
        elif choice == '2':
            daily_logs = tracker.view_daily_logs()
            if daily_logs:
                print("\nDaily Logs:")
                for log in daily_logs:
                    print(f"{log[0]} - {log[1]}")
            else:
                print("No logs found for today.")
        elif choice == '3':
            monthly_report = tracker.view_monthly_report()
            if not monthly_report.empty:
                print("\nMonthly Report:")
                print(monthly_report)
            else:
                print("No data available.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
