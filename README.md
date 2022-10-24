# Attendance Tracker

Tracks the attendance of participants in online events using their emails

### Install
```bash
pip install attendance_tracker_email
```
[PyPi Package](https://pypi.org/project/attendance-tracker-email)
### Directory structure

```
your_project
│   README.md
│   your_script.py
│
└───email_files
   │   day1.txt
   │   day2.txt
   |   day3.txt

```

------- day1.txt
```day1.txt
first2emai@outlook.com
second12email@gmail.com
```

### How to use 


```
from attendance_tracker_email import attended
```
Directory with emails as day1.txt, day2.txt etc
```
directory = 'email_files'
print( attended.show_attended(directory))
```

### Next in the project
- [X] Published for easy plug n play
- [ ] #739 Create a chrome extension for the frontend
- [ ] Authentication to take attendance automatically
- [ ] Track time attended
- [ ] Add more features

### Issues
a)  [Open an issue](https://github.com/morehwachege/attendance-tracker-email/issues)
b) [Star this for the future](https://github.com/morehwachege/attendance-tracker-email/fork)
## License
MIT

Contributions are welcome. Pull requests are welcome.

  