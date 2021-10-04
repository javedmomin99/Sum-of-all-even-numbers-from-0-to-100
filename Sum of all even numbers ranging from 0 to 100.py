#Find the Sum of all the even numbers ranging from 0 to 100
total = 0
for number in range(0,101,2):
# higher limit is given as 101 since python considers one lesser than higher limit given, so for upto 100, we will define one higher, that is 101
  total = total + number
print(f"Sum of all the even numbers ranging from 0 to 100 is {total}")

