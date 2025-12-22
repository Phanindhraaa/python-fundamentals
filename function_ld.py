def find_largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest


print(find_largest([8, 9, 3, 1, 6]))


def count_even(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

print(count_even([8, 9, 3, 1, 6])) 

def get_names(users):
    names = []
    for user in users:
        name = user['name']
        names.append(name)

    return names  

print(get_names([{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'Charlie'}]))  

def get_adults(users):
    adults = []
    for user in users:
        if user['age'] >= 18:
            adults.append(user)

    return adults

print(get_adults([{'name': 'Alice', 'age': 17}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 16}, {'name': 'David', 'age': 22}]))        

def create_user(name, age, email):
    user = {
        'name': name,
        'age': age,
        'email': email
    }
    return user

print(create_user('Eve', 30, 'eve@example.com'))