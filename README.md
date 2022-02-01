# File Categorizer

## About 
A small tool to categorize and check file integerity **(integerity test in under development).

### Why?
Sometimes like after data recovery with photorec or your download folder, you end up having a mess of different files scattering in randomly named different folders and you may wonder:
- How and where should you start finding and checking specific file(s)?
- Is the file healty to take time checking it?

This tool can automate this job.
On my own PC running linux, it took about 10 min to categorize 160 GB of my own data. I see, it might be pretty slow, but it really IS far more faster than human check.

## Some tips for using
- This script makes use of Python Magic library for mime type detection. Any odd behavior in file mime detection could be result of that library.
- Except getting the source folder, the rest of process is automated in CLI.
- The files will be copied to /Category directory within the given address. The will be some sub category directories based on libmagic file detection algorithm.
- **[not completed yet!]** All defective files are copied to /Corrupted directory within /Category. The log file will be in the source directory.
- Do Check the code before using it to prevent further data lose (I created this script for my own use and reditributed for those who may find it useful. It might not work as you expected. So, Change it in a way that you desire).

## Requirements

- [Jalali Calendar Library](https://github.com/shobeiry/jalali). This library produces a calendar ouput which is used mainly in Iran and Afghanistan. You can change it to use default Python datetime library.
- [Patoolib](https://github.com/wummel/patool): The script uses this library to test archive integerity. It really is the best all-in-one solution I found.
- [Python Magic Library](https://github.com/ahupp/python-magic) : As mentioned this library is used to detect file mimes/types. Amongst *filetype*, *fleep*, and *Python Maigc Library*, I tried the latter two. Fleep was good, magic worked better. so, I changed the code to use *magic* before uploading it here.

## Roadmap
- Creating first working build for categorizing --> done
- Renaming font files into their internal file name --> Being developed
- Removing empty folders
- Creating user customization in CLI
  - Calendar choice.
  - Logging procedure whether to print/save the log or not
  - Using mime type or extension or both.
  - Clearing messy folders
  - Creating subfolders for each category
  - selecting a different file type detector other than lib-magic e.g filetype or fleep
- Using multi-processing to speed the script up.
- Verifying file integerity and extension and mime type matching procedure
  - Checking archives and trying to fix corrupted ones using patoolib ---> needs fixing
  - font itnegerity check
  - Audio / video check
  - Verifying Image and fixes byte errors using
- Adding GUI.
