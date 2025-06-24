number = [12,15,63,21,24,30,36,106,48]
divisor = 6

print(f"ตัวที่หาร {divisor} ลงตัว")
found = 0

for i in number:
    if i % divisor == 0:
        print(f"{i} หาร {divisor} ลงตัว(={i // divisor})")
        found += 1
        
        if found == 3:
            break