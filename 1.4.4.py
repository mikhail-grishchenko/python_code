n = int(input())
all_num_card = 0
sum_cards = 0
for i in range (1,n):
    all_num_card += i
    x = int(input())
    sum_cards += x
all_num_card += n
a=all_num_card-sum_cards
print(a)
