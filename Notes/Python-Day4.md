
# Python Comparison Operators

### 1. Equal to **==**
- Checks if the value on the left is equal to value on the right.
**Example**
```py
print (11 == 11)
```
**Output: 
#### Note! Comparison operators always result in a boolean value.
- For the code above since 11 is the same as 11 the output of the code will be `True`. 

### 2. Not Equal to **!=**
- Checks if the left side is **not equal to ** right side.
```py
print(6 !='6')  # Since texts cannot be equal to numbers this line will print True
print(6 != 6 ) # Since the both side of equation is same, this will print False
```
### 3. Greater Sign **>**
- Checks if the left side of equation is bigger than the right side.
```py
print(5.0 > 5) # False because 5.0 is not bigger than the 5
print(3  >  4) # False because 3 is not bigger than the 4
print(10 >  9) # True because 10 is bigger than the 9
```
### 4. Less than Sign **<**
- Checks if the left side of equation is smaller than the right side.
```py
print(5.0 < 5) # False because 5.0 is not smaller than the 5
print(3  <  4) # True because 3 is smaller than the 4
print(10 <  9) # False because 10 is not smaller than the 9
```

### 5. Less than equal <= || 6. Greater Equal Sign >=
- Checks if the left side is smaller OR equal **<=**, 
- Checks if the left side is bigger OR equal **>=** .
```py
print(5.0 <= 5) # True becaue the values are equal.
print(5.0 >= 5) # True becaue the values are equal.
print(3  <=  4) # True because 3 is smaller than the 4
print(10 >= 9) #  True because 10 is bigger than the 9
```

## Note !
- **Type Matters:**
- When comparing values type of the values also important:
For ex: `5 == '5'` is `False` because one is string(text)
the other is a int type.

- **We can chain the comparison operators in python**
```py
print(1 < 2 < 3) # True
```

## Note! 
- `True` numerically equals to `1` and `False` numerically 
 equals to `0`. For example:
 ```py
 print(int(True)) # 1
 print(int(False))# 0
 # When using comparison operators between bool and int type 
 # python auto-converts bool type to int. 
 print(True == 1)    # True
 print(True > False) # True  
 print(False < 3 )   # True
 ```
## Converting Other Types To Bool
- Which function do you think we are going to use to convert other types 
to boolean? 
**bool()** function.
```py
b = bool(-2)
print(b) # True
b1 = bool(0)
print(b1) # False
```
#### Every number except 0 will result in True. 






