#task 1 

a = [12.23, 13.32, 100, 36.32]

arr = np.array(a)

print( f"1d numpy arry : {arr}")

# task 2 2. Create 3x3 Matrix (2?10)



a = np.arange(2,11).reshape(3,3)
print(a)


# task 3 3. Null Vector (10) & Update Sixth Value



a = np.zeros(10)

a[5] = 11

print (a)


# task 4 4. Array from 12 to 38



arr = np.arange(12,39)

print(arr)



# task 5 Convert Array to Float Type

numbers  = [1,2,3,4]

arr = np.array(numbers)

float_arr =  arr.astype(float)

print(float_arr)


# task 6 Celsius to Fahrenheit Conversion

# formula of conversion  F = C * 9/5 + 32



# Массив температур в Цельсиях
C = np.array([0, 12, 45.21, 34, 99.91, 0])
F = C * 9/5 + 32

# Массив температур в Фаренгейтах
f = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
c = (f - 32) * 5/9

print("Values in Fahrenheit degrees:", np.round(F, 2))
print("Values in Centigrade degrees:", np.round(c, 2))



#task 7 Append Values to Array (Do self-tudy)

arr = np.array([10,20,30])

arr2 = np.array([40,50,60,70,80,90])

new_arr = np.append(arr, arr2)

print(new_arr)


# task 8 Array Statistical Functions (Do self-tudy)Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.

arr = np.array([1,2,3,4,5,6,7,8,9,10])

arr_mean = np.mean(arr)
arr_median = np.median(arr)
arr_std = np.std(arr)

print(f"mean: {arr_mean}, median: {arr_median}, std: {arr_std}")



# task 9 Find min and max



arr = np.random.randint(2,100, size=(10,10) )

min_arr = arr.min() 

max_arr = arr.max()

print (f"Min: {min_arr}   Max: {max_arr}")




# task 10 Create a 3x3x3 array with random values.



arr = np.random.randint(1,30, size=(3,3,3))

print (arr)
