# CataFile - A File Categorizing Tool

## About

CataFile is a small tool to categorize and check file integerity **(File integerity tests are under development)**.

### Why?

Sometimes e.g. after data recovery with tools like Photorec or downloading a large number of files, you end up having a mess of various files scatterred in randomly named different folders and you may wonder:

- How and where should you start checking and looking for specific file(s)?
- Which files are healthy?
- It takes a lot of time checking it. How can I do that?

This tool can automate this job.
On my own PC running Linux, it's first release took about 10 min to categorize 160 GB of my own data. I see, it might be pretty slow, but it really IS far more faster than human check.

## Some tips for using the first release

- On its current release, this script makes use of Python Magic library for mime type detection. Any odd behavior in file mime detection could be result of that library. Hence, this was the most low-hanging fruit that worked for me.
- For the time being, except getting the source folder, the rest of process is automated in CLI.
- The files will be copied to /Category directory within the given address. There will be some sub category directories based on libmagic file detection algorithm.
- All undetected adn possibly corrupted files are copied to /Corrupted sub-directory within /Category folder. The log file will be left in the source directory.
- Do Check the code before using it to prevent further data loss (I created this script for my own use and redistributed in a hope that it would be useful for some one. It might not work as you expected. So, Change it in a way that you desire and help the project grow).

## Requirements

- [Jalali Calendar Library](https://github.com/shobeiry/jalali). This library produces a calendar ouput which is used mainly in Iran and Afghanistan. You can change it to use default Python datetime library.
- [Patoolib](https://github.com/wummel/patool): The script uses this library to test archive integerity. It really is the best all-in-one solution I found for this purpose. If you know a better and faster one, let me know.
- [Python Magic Library](https://github.com/ahupp/python-magic) : As mentioned, this library is used to detect file mimes/types.

Amongst *filetype*, *fleep*, and *Python Maigc Library*, I tried the latter two. ~~Fleep was good, magic worked better. so, I changed the code to use *magic* before uploading it here.~~ ~~On the second thought and further tests, fleep provided a better detection and category folder structure.~~ Untill now, I've tested these libraries:
    - [Fleep](https://github.com/ua-nick/fleep-py)
    - [Magic](https://github.com/ahupp/python-magic)
    - [Pure Magic](https://github.com/cdgriffith/puremagic)
    - [Filetype](https://github.com/h2non/filetype.py)
    - [Pyfsig](https://github.com/schlerp/pyfsig)
    - [Defity](https://github.com/hongquan/Defity)
  
Having tried all these magic-number-based file mime and extension detectors, most of the libraries detect files differently in module level and standolone use. I couldn't find out why. For the time being, with my sample of files and  tests, ~~"filetype" is the one that returns the same result both in and out of my modules.~~ none of these libraries could pass all the tests. So, continuing this project with libraries that don't detect file types correctly from time to time is not a good idea. For now, I abandon it since I think its going to be a yakshaving if I try to develop another file type detector. maybe  I learned alot from doing this self defined project.

## Roadmap

  Status:

  :heavy_check_mark: **Done**
  
  :white_check_mark: **Being Developed**
  
:heavy_check_mark: **Version 1:**

- :heavy_check_mark: Creating subfolders for each category
- :heavy_check_mark: Creating first working build for categorizing

:white_check_mark: **Version 2:**

- :heavy_check_mark: Creating GUI:
  - :heavy_check_mark: Creating simple UI for currently automated procedure to give the user some options
  - :heavy_check_mark: Directory input.
  - :heavy_check_mark: Calendar choice.
  - :heavy_check_mark: Logging procedure whether to print/save the log or not
  - :white_check_mark: Selecting a different file mime detector other than lib-magic e.g filetype or fleep
  - :heavy_check_mark: Renaming file extensions into their detected  ones (still have some problems because of the libraries);
- [ ] Verifying file integerity and extension along with mime type matching procedure:
  - [ ] Archives:
    - :heavy_check_mark: Checking archive like files e.g. new MS-Office files and moving possible corrupted ones to /corrupted folder category
  - [ ] Fonts:
    - :white_check_mark: File Inegerity check;
    - :white_check_mark: Renaming font files into their original internal file name;

**Version 3:**

- [ ] Trying to fix corrupted archives using patoolib/some other tools
- [ ] Adding internationalization / translations features
- [ ] Option to remove remaining empty folders
- [ ] Processing Audio / video files
- [ ] Processing files using [filetype](https://github.com/h2non/filetype.py)
- [ ] Absurd dream ideas to categorize:
  - [ ] images using opencv (More like a scary dream to me than an extravagant claim )
  - [ ] books & articles based on their ISNB, online book services or processing their texts
  - [ ] audio files based on their mood, tone, etc.
  
    and also:
  - [ ] implementing multi-processing / GPU processing thechniques to speed it up
  - [ ] verifying images and fix their probable byte errors
  - [ ] implementing some part of the tool in C to speed the procedures up.
  - [ ] using glob and pathlib functions in some path-related actions for more speed.
