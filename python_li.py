def find_range(lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)
def missing_numbers(input_list, lower, upper):
        ans = []
        pre = lower - 1

        for i in range(len(input_list) + 1):
            if i == len(input_list):
                cur = upper + 1
            else:
                cur = input_list[i]
            if cur - pre >= 2:
                ans.append(find_range(pre + 1, cur - 1))
            pre = cur
        return ans


a = [0, 1, 3, 50, 75]
lower = 0
upper=99
result=missing_numbers(a, lower, upper)
print(result)