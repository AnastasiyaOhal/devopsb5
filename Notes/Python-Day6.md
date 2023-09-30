# If Statement in Python
- Purpose of an if statement is executing the certain parts of the code 
depending on the given boolean conditions.
- When a `boolean` condition is `True` for the if statatement the 
**next** block of code will be executed.


#### How do we know where next block of code starts and ends? 
- In python same block of codes has same indentation. So that, 
by looking at the indentation we could understand beginning and end of the 
block of codes.
**Note!** a block of code refers to the lines of codes that belong to 
same implementations.This implementations could be `if statement`, methods, class etc.

#### How if statement works? 
```py
if boolean_cond:
  # code belongs to if
  # code belongs to if   
#code that is not effected by if statement, this line will always gets executed regardless of the if statement's condition.   
  
```
**Note:** As seen on the example above, only if a boolan condition is True 
if block will get executed.

## Examples:
```py
if True:
  #line1
  #line2
#line3

#Which of the lines above will be executed? 
# Since the condition is True code block of if statement(line1 and line2),
# will get executed. line 3 will never be effected by if statement so it will 
# always gets executed. 
```

```py
if False:
  #line1
  #line2
#line3

# # Since the condition is False code block of if statement(line1 and line2),
# will NOT get executed. line 3 will never be effected by if statement so it will always gets executed. 
``````

















