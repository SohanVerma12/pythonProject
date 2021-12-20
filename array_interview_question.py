# Reveres the array
def reverse(nums):
    start_index = 0
    end_index = len(nums)-1

    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

if __name__ == '__main__':
    n = [1,2,3,4,5]
    reverse(n)
    print(n)

# Palindrone question in array
def palindronen_python(s):
    if s == s[::-1]:
        return True
    return False

if __name__ == '__main__':
    print(palindronen_python("madam"))

# reverse integre
def reversed_integre(n):
    reversed_int = 0
    reminder = 0
    while n > 0:
        reminder = n % 10
        reversed_int = reversed_int*10 + reminder
        n = n // 10
    return reversed_int

if __name__ == '__main__':
    print(reversed_integre(12345))

# anagram array
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

if __name__ == '__main__':
    s1 = ['f', 'l', 'u', 's', 't', 'e', 'r']
    s2 = ['r', 'e', 's', 't', 'f', 'u', 'l']
    print(is_anagram(s1,s2))

#finding dulipcate in array
l = [1,2,3,4,5,6,2]
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
    else:
        print(i, end=' ')