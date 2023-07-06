a = 10   # Binary: 1010
b = 6    # Binary: 0110

result = a & b
print("Result:", result, "Binary:", bin(result)[2:].zfill(4))

a = 10   # Binary: 1010
b = 6    # Binary: 0110

result = a | b
print("Result:", result, "Binary:", bin(result)[2:].zfill(4))



a = 10   # Binary: 1010
b = 6    # Binary: 0110

result = a ^ b
print("Result:", result, "Binary:", bin(result)[2:].zfill(4))

a = 10   # Binary: 1010

result = ~a
print("Result:", result, "Binary:", bin(result)[3:].zfill(4))
