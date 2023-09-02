print("%3s"%"Dec"+"%5s"%"Hex"+"%5s"%"Oct"+"%5s"%"Chr")
for n in range(65,91) :
    print(f"%3s"%n
        +"%5s"%hex(n).replace("0x"," ")
        +"%5s"%oct(n).replace("0o"," ")
        +"%5s"%chr(n))