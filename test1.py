input_text = ""
repeat_num = 0
def setting(a, b):
    print("입력할 말을 입력하세요")
    input_text = input()
    #print(input_text)
    print("반복할 횟수를 입력하세요")
    repeat_num = int(input())
    #print(repeat_num)
    #print(type(repeat_num))
setting()
print(input_text)
print(repeat_num)