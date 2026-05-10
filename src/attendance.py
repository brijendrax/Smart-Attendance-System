import csv
import os
import winsound

from datetime import datetime

def mark_attendance(name):

    file_path = "attendance.csv"

    already_marked = []

    if os.path.exists(file_path):

        with open(file_path, "r") as file:

            reader = csv.reader(file)

            next(reader, None)

            for row in reader:

                if len(row) > 0:

                    already_marked.append(row[0])

    if name not in already_marked:

        now = datetime.now()

        date = now.strftime("%Y-%m-%d")

        time = now.strftime("%H:%M:%S")

        with open(file_path, "a", newline="") as file:

            writer = csv.writer(file)

            if os.stat(file_path).st_size == 0:

                writer.writerow(["Name", "Date", "Time"])

            writer.writerow([name, date, time])

        print(f"{name} attendance marked")

        winsound.Beep(1000, 500)

    else:

        print(f"{name} already marked")