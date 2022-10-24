from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.5'
DESCRIPTION = 'Attendance tracker package using emails'
LONG_DESCRIPTION = 'This package tracks the attendance of participants in online events using their emails'

# Setting up
setup(
    name="attendance_tracker_email",
    version=VERSION,
    author="morehwachege (Antony Muriithi Gakuru)",
    author_email="<antony123muriithi@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'attendance', 'tracking',
              'live stream', 'camera stream'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    # entry_points={
    #     'console_scripts': [
    #         'attendance_tracker_email=attendance_tracker_email.main:main',
    #     ],
    # }
)
