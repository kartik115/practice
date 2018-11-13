from itertools import islice
import os


def merge(file_name_1, file_name_2):

    with open(file_name_1) as f1, open(file_name_2) as f2, open("merge.txt", 'a') as result:

        first = second = True

        while True:
            if first is not None and first:
                next_lines_file1 = list(islice(f1, 1))
            if second is not None and second:
                next_lines_file2 = list(islice(f2, 1))
            # print(next_lines_file1, next_lines_file2)

            if next_lines_file1 != []:
                first = next_lines_file1[0].replace("\n", "")
            else:
                first = None

            if next_lines_file2 != []:
                second = next_lines_file2[0].replace("\n", "")
            else:
                second = None

            if first is None and second is None:
                break

            elif first is None and second is not None:
                result.write(second + "\n")

            elif first is not None and second is None:
                result.write(first + "\n")

            elif first < second:
                result.write(first + "\n")
                first = True
                second = False

            elif first > second:
                result.write(second + "\n")
                second = True
                first = False


merge("file1.txt", "file2.txt")
os.rename('merge.txt', 'temp.txt')
merge("file3.txt", "temp.txt")
os.remove("temp.txt")