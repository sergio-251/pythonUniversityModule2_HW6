# Дополнительное практическое задание по модулю 2
n, s = int(input('Введите число первого камня: ')), ''
nums = list(range(1, n))
for i in range(n // 2):
    for j in range(i + 1, len(nums)):
        if n % (nums[i] + nums[j]) == 0:
            s += str(nums[i]) + str(nums[j])
print(f'{s} - нужный пароль')