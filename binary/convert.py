"""The function collects the initial paramaters and returns them"""
def get_input():
    positive_number = int(input("Enter a positive integer: "))
    bits = int(input("Enter the amount of bits: "))
    return positive_number, bits


"""The function recives a positive integer and amount of bits.
The function transform the number to it's binary number 
and padding it with zero's until the amount of bits is reached.
Finally the function inverts each bit to it's opposite
and return the result"""
def to_invert_bin(num, bits):
    binary = bin(num)[2:].zfill(bits)
    inv_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
    return inv_binary


"""The function adds 1 to the inverted binary in order to apply the two's complement rule.
lastly it returns the negetive binary of the original number"""
def to_negetive(inv_binary):
    negetive_binary = bin(int(inv_binary, base=2) + 1)[2:]
    return negetive_binary


"""The main function"""
def main():
    positive_number, bits = get_input()
    inverted_binary = to_invert_bin(positive_number, bits)
    negetive_binary = to_negetive(inverted_binary)
    print(negetive_binary)


"""Calls the main function from the module"""
if __name__ == '__main__':
    main()