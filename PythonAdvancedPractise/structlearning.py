import struct

def isBMP(file):
    with open(file, 'rb') as f:
        symbol = f.read(30)
        s_info = struct.unpack('<ccIIIIIIHH', symbol)
        if s_info[0] == b'B' and s_info[1] == b'M':
            print('The size is %d*%d, the color number is %s' 
                  %(s_info[6], s_info[7], s_info[9]))
        else:
            print("The file is not a BMP!") 



isBMP("1.bmp")