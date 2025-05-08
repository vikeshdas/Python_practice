import csv

with open('generated_file.csv','r') as f:
    rows=csv.reader(f)
    
    """
    next method reads next item from iterable object reader() method creates an iterator.We know iterator is memroy efficient it takes one item at a time in memory to process using next method 
    """

    headers=next(rows)
    print(headers)

    next(rows)
    for row in rows:
        print(row)

""""
csv library will not work well with millions of rows in that cas we should use pandas which has parllel processing.csv module is good for: Live / Streaming data following.Because the csv reader reads one row at a time.

pandas is good for: Batch data analysis.Pandas loads the entire file into memory as a DataFrame.It is designed for powerful data manipulation: filtering, grouping, merging, pivoting, statistical operations, etc
"""


"""
write csv file
"""

# we have use 'a' in open for append mode to append item at the end of the file.
with open('new_csv.csv','a') as f:
    writer=csv.writer(f)
    data=('name','age','roll')
    writer.writerow(data)

    data=('vikesh','27','49')
    writer.writerow(data)

