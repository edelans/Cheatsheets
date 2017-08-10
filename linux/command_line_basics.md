


# Filters

**sort**

Sorts standard input then outputs the sorted result on standard output.

**uniq**

Given a sorted stream of data from standard input, it removes duplicate lines of data (i.e., it makes sure that every line is unique).

**wc**

wc stands for word count and it does just that (as well as characters and lines. By default it will give a count of all 3 but using command line options we may limit it to just what we are after  :

- `-l` lines only
- `-w` words only
- `-m` characters only

**cut**

cut is a nice little program to use if your content is separated into fields (columns) and you only want certain fields.

The -d option specifies the separator (defaults to TAB).

The -f option allows us to specify which field or fields we would like. If we wanted 2 or more fields then we separate them with a comma as below.

```bash
$ cut -f 1 -d ' ' mysampledata.txt
Fred
Susy

$ cut -f 1,2 -d ' ' mysampledata.txt
Fred apples
Susy oranges
```

**fmt**

Reads text from standard input, then outputs formatted text on standard output.

**pr**

Takes text input from standard input and splits the data into pages with page breaks, headers and footers in preparation for printing.

**head**

Outputs the first few lines of its input. Useful for getting the header of a file.

**tail**

Outputs the last few lines of its input. Useful for things like getting the most recent entries from a log file.

**tr**

Translates characters. Can be used to perform tasks such as upper/lowercase conversions or changing line termination characters from one type to another (for example, converting DOS text files into Unix style text files).

**sed**

Stream editor. Can perform more sophisticated text translations than tr.

A basic expression is of the following format: `s/search/replace/g`

- initial s stands for substitute and specifies the action to perform (there are others but for now we'll keep it simple).
- The g at the end stands for global and is optional. If we omit it then it will only replace the first instance of search on each line.

# Commands

**egrep or grep -E**

Examines each line of data it receives from standard input and outputs every line that contains a specified regex pattern.


options :

-i
Ignore case (ie uppercase, lowercase letters).

-v
Return all lines which don't match the pattern.

-w
Select only matches that form whole words.

-c
Print a count of matching lines.
Can be combined with the -v option to print a count of non matchine lines.

-l
Print the name of each file which contains a match.
Normally used when grep is invoked with wildcards for the file argument.

-n
Print the line number before each line that matches.

-r
Recursive, read all files in given directory and subdirectories.


examples :

```bash
$ egrep 'mellon' myfile.txt
# Print every line in myfile.txt containing the string 'mellon'.
$ egrep -n 'mellon' myfile.txt
# Same as above but print a line number before each line.
$ egrep '(.)bb\1' myfile.txt
# Find every line with 2 b's and the same character both before and after those b's.
$ egrep -l '[0-9]{8,}' /files/projectx/*
# Print each file in the directory projectx which contains a number of 8 digits or more.
$ egrep '\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}\b' myfile.txt
# Print every line of myfiles.txt containing an email address (naive email matching pattern)
```


**find**

Find is a great tool for fine grained control over searching for files.

search for files over 200mb in the users home directories :

```bash
$ find /home -size +200M -exec ls -sh {} \;
452M /home/barry/backups/everything.tar.gz
941M /home/lisa/projects/loony/servermigration.tar.gz
768M /home/mark/Documents/gregs_birthday.mpg
```

**xargs**

Xargs is a useful tool to run a particular command for every item in a list.

Example :

```bash
$ ls
image1.JPG image2.JPG image3.JPG image4.jpg
$ basename -s .JPG -a *.JPG | xargs -n1 -i mv {}.JPG {}.jpg
$ ls
image1.jpg image2.jpg image3.jpg image4.jpg
```

**awk**

An entire programming language designed for constructing filters. Extremely powerful.

**man -k <search term>**
Search for man pages containing the search term.


# Regular Expression Overview

I will outline the basic building blocks of re's below then follow on with a set of examples to demonstrate their usage.

- `.` (dot) - a single character.
- `?` - the preceding character matches 0 or 1 times only.
- `*` - the preceding character matches 0 or more times.
- `+` - the preceding character matches 1 or more times.
- `{n}` - the preceding character matches exactly n times.
- `{n,m}` - the preceding character matches at least n times and not more than m times.
- `[agd]` - the character is one of those included within the square brackets.
- `[^agd]` - the character is not one of those included within the square brackets.
- `[c-f]`` - the dash within the square brackets operates as a range. In this case it means either the letters c, d, e or f.
- `()`` - allows us to group several characters to behave as one.
- `|` (pipe symbol) - the logical OR operation.
- `^` - matches the beginning of the line.
- `$` - matches the end of the line.

More comprehensive guide @ https://github.com/zeeshanu/learn-regex .
Awesome testing tool @ https://regex101.com/ with lots of helpers, code generators and more.




# Useful Commands

Find Biggest files/repo

        sudo du -shx /* 2>/dev/null | sort -n
