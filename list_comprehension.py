"""
List Comprehension
- Bundan foydalanish biroz sizni chalg'itishi mumkin lekin unda ancha performance yaxshiroq
"""

# bad
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# good
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


############################### Django loyihada ################################
# views.py da


def user_list(request):
    # Bad
    active_users = []
    for user in User.objects.all():
        if user.is_active:
            active_users.append(user)

    # Good
    active_users = [user for user in User.objects.all() if user.is_active]

    return render(request, "user_list.html", {"users": active_users})
