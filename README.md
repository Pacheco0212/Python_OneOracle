# Python_GettingStarted
> ### Course. Python: getting started with the language


> ### Course. Python: incorporated functions
>> #### Class: Format Function
>>
>> We can use the "**Format**" in the following ways.
>>
>> **Interpolate variables**: we can insert values into a string using braces `{}` and the format function. 
>> ```python
>> print("Intento {} de {}".format(1,3))
>> print("Intento {1} de {0}".format(1,3))
>> ```
>>```bash
>> In[1]: Intento 1 de 3
>> In[2]: Intento 3 de 1
>>```
>> **Control the format numbers**: we can specify the number of decimals, spaces and zeros that we want to display in a number.
>> ```python
>> print("{:7.1f}".format(1000.12))
>> print("{:07.2f}".format(4.11))
>> ```
>>```bash
>> In[1]:  1000.1
>> In[2]: 0004.11
>>```
>> **Format dates**: we can use format to display dates in a specific format.
>> ```python
>> print("Fecha {:02d}/{:02d}/{:4d}".format(16,7,2024))
>> ```
>>```bash
>> In[1]: Fecha 16/07/2024
>>```

>> ### Class: Random Function
>>
>> **Random** isn't a built-in function in Python, so we need to import it.
>> 
>> We can use it to generate a random number using `random()` between zero and one, such as between 0 and 100, and we can use `round()` to round a number
>>
>>```python
>> import random
>>
>> randNumber = random.random()
>> randNumber_2 = random.random() *  100
>> roundNumber = round(randNumber_2)
>>```
>>```bash
>> In[1]: 0.19117567147752912
>> In[2]: 48.71476823037345
>> In[3]: 49
>>```   
>> We can use the `randint()` function of the module `random` to generate a random number within a range.
>>
>>```python
>> number = random.randint(1,100)
>>```
>>```bash
>> In[1]: 85
>>```
>>
>> :memo: **Note:** we can use `abs()` to get the absolute value.