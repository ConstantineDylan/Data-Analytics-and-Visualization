#########
asset = 10
trade_percent = .2
trade_capacity = asset * trade_percent

num_of_compensation = 5

print(f"For  {asset}$ in all assets")
print(f"with {int(trade_percent*100)}% put into trading")
print(f"and  {num_of_compensation}x compensation\n")

print(f'you have to trade with these numbers: ')

list_X = []
for c in range(1,num_of_compensation+2):
    ammount = trade_capacity / (2.5 ** (num_of_compensation+1- c))
    list_X.append(ammount)
    print(f'x{c} = {ammount}$')

#########
num_wrong_pred = 4

amm_lost = 0
for w in range(num_wrong_pred):
    amm_lost += list_X[w]

profit = list_X[num_wrong_pred] - amm_lost
round_roe = profit / amm_lost
roe = profit / asset


print(f'\nif you lost {num_wrong_pred}x in your prediction and lose {"{:.2f}".format(amm_lost)}$')
print(f'you will profit in the {num_wrong_pred+1}th prediction with {"{:.2f}".format(list_X[num_wrong_pred])}$ income')
print(f'therefore profit = {"{:.2f}".format(profit)}$')
print(f'with round ROE = {"{:.2f}".format(round_roe * 100)}%')
print(f'with full ROE = {"{:.2f}".format(roe*100)}%')

#########
# 1 year = 52 week
weeks = 24
new_asset = "{:,.2f}".format(asset * (1+roe) ** (weeks*7))

print(f'\nif you do this consistenly with same ROE for {weeks * 7} days,')
print(f'you will have an overall asset of {new_asset}$')
print("============================================================")

#########
wrong_pred = 1
wrong_pred_days = 7
right_pred_days = (7 - wrong_pred) * weeks
# pred_asset = "{:.2f}".format((1+roe) ** right_pred_days)

week_profit = asset
# print(roe)

for w in range(weeks):
    week_profit *= ((1+roe) ** (wrong_pred_days - wrong_pred))
    # print(week_profit)

    for d in range (wrong_pred):
        trade_cap = week_profit * trade_percent
        week_profit -= trade_cap
        # print(week_profit)
    
    # print()  

pred_asset = "{:,.2f}".format(week_profit)

print(f'\nyou still can lose one or a few times')
print(f'lets say for a week you can lose up to {wrong_pred} times,')
print(f'so you have {right_pred_days} right prediction days')
print(f'in {weeks} week you will have {pred_asset}$')


