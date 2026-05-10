print("SMART ATTENDANCE SYSTEM")
print("1. Capture Faces")
print("2. Train Model")
print("3. Start Attendance")

choice = input("Enter Choice: ")

if choice == '1':
    exec(open('src/capture.py').read())

elif choice == '2':
    exec(open('src/train.py').read())

elif choice == '3':
    exec(open('src/recognize.py').read())

else:
    print("Invalid Choice")