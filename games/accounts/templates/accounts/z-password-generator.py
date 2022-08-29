
import random

lower_case = "qwertyuiopasdfghjklzxcvbnm"
upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "0123456789"
symbols = "!@#$%*()&\/?"

Use_for = lower_case + upper_case + numbers + symbols
length_for_password = 10


password = "".join(random.sample(Use_for, length_for_password))

print(password)