#This is python list

numbers=[1,2,3,4,5];
#O(1) complexity if we know index of the data
#print(numbers[0]);
numbers[2]=100;
for num in numbers:
    print(num);

for i in range(len(numbers)):
    print(numbers[i]);

#print out indices
print(numbers[0:3]);
#print out the last two elements
print(numbers[:-2]);

max=numbers[0]
for num in numbers:
    if num>max:
        max=num;
print(max);

