#    Id=20CS102    Name=Janesh Vyas


#  Function below takes two arguments first is K and second is string of room numbers.
#  String of room numbers are stored in list and each number is checked if it is equal to K it is 
#  discarded and if it is not equal to K it is returned.
def captain_room(no, str):
    num = int(no)
    num_list = str.split()
    for i in num_list:
        cnt = 0
        for j in num_list:
            if j == i:
                cnt = cnt + 1
        if cnt != num:
            return i


a = input()
b = input()
c = captain_room(a, b)
print(c)
