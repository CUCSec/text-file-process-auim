
with open("log_files/201811113017.log","rb") as file:
    h=0
    for line in file:
        data = file.readline()
        data = data[26:38]
        data2 = bytes.decode(data)
        if data2 == '201811113017':
            h=h+1
    print(h)