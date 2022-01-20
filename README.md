# File Categorizer
A small tool to categorize and check file integerity after data recovery with photorec

Some tips for using:
- This script makes use of Python Magic library for mime type detection. Any odd behavior in file mime detection could be result of that library.
- Except getting the source folder, the respt of process is automated in CLI.
- The files will be copied to /Category directory within the given address. The will be some sub category directories based on libmagic file detection.
- All file which are recognized as defective are copied to /Corrupted directory within /Category. The log file will be in the source directory.
- Do Check the code before using it to prevent data lose (I created this script for my own use and reditributed for those who may find it useful. It might not work as you expected. So, Change it in a way that you desire.

# Requirements:

- jalali calendar library. This library produces a calendar which is used mainly in Iran and Afghanistan. You can change it to use default Python datetime library.
- patoolib: The script uses the lib to test archive integerity.
- python magic lib : As mentioned this library is used to detect file mimes. Amongst filetype, fleep, and magic, I tried the latter two. fleep was good, magic worked better. so I changed the code to use *maigc* before uploading here.
