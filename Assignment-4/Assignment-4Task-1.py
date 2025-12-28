try:
    with open("sample.txt",'rt') as fh:
        print("Reading file content:")
        line1=fh.readline()
        line2=fh.readline()
        print(f'Line 1:{line1}')
        print(f'Line 2:{line2}')
except:
    raise Exception ("Error: The file 'sample.txt' was not found.")