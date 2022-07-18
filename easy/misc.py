
# Exercise: Array DataStructure
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190

# Create a list to store these monthly expenses and using that find out,
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


mylist = []

mylist.extend([2200, 2350,2600,2130,2190])

month_map = {'january':0, 
            'febraury':1, 'march':2, 'april':3, 'may':4, 'june':5, 'july':6, 'august':7, 'september':8, 'october':9, 'november':10,
                'december':12}

feb_extra_jan = mylist[month_map['january']] - mylist[month_map['febraury']]

sum_expense = sum(mylist[:3])

print(2000 in mylist)


mylist.append(1980)

mylist[month_map['april']] = mylist[month_map['april']] - 200

print(mylist, feb_extra_jan, sum_expense)
