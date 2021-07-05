import hashlib;

str = "Hello World";

ott = hashlib.md5(str.encode());

print("The desired hash is : ");

print(ott.hexdigest());