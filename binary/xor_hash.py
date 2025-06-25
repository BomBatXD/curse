import time

xorNum = 5

path = input("enter a file path: ")
new_path = path.replace('.',f" {int(time.time())}.")

with open(path, 'rb') as file:
    with open(new_path, 'wb') as output:
        while True:
            byte = file.read(1)
            if not byte:
                break
            output.write(bytes([xorNum^byte[0]]))