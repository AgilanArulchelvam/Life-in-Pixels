def string_to_rgb(input_string):
    string = input_string.upper()
    count = 0
    for i in string:
        num = ord(i) - 64
        count+= num
    num1 = [count*1,count*2,count*3]
    return num1

print(string_to_rgb('world'))

