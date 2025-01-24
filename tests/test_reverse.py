from project.reverse import reverse


test_txt = 'project/input.txt'

with open('project/input.txt', 'r', encoding='utf-8') as f:
    test_txt = f.read()

reversed_txt = reverse(test_txt)

with open('project/output.txt', 'w') as f:
    f.write(reversed_txt)

print(test_txt)
print(reversed_txt)