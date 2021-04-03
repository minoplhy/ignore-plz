# name = value

player_posit = 10
print(player_posit)

player_posit = 15
print(player_posit)

pi = 3.14
pi = 3.14159
print(pi)

player_posit = 15
print(player_posit)

print(type(player_posit))

is_died = True
is_died = False

print(is_died)
print(type(is_died))

is_died = 1
print(is_died)
print(type(is_died))

name = "Namesis"
is_died_message = "False"
age_as_a_string = "5"
print(name)
print(type(name))

age = 33
name_age = "{}: {}".format(name,age)
print(name_age)
# + - * / % // ** =

player_posit = 100
# player_posit = 11
forward = player_posit + 1
print(forward)
backward = player_posit - 1
print(backward)

remainder = 10 % 2
print(remainder)
floor_division = 10 // 2
print(floor_division)

five_squared = 5 ** 2
print(five_squared)

# player_posit = player_posit + 1
player_posit += 1
print(player_posit)
player_posit -= 1
print(player_posit)

f_name = "Nemedis "
l_name = "Fuckyou"
print(f_name + l_name)

player_posit %= 50
print(player_posit)

# > >= < <= == != not or and

player_posit = 10
player_end_posit = 10

is_end = player_posit == player_end_posit
print(is_end)
is_halfway = player_posit >= player_end_posit / 2
print(is_halfway)

not_end = not is_end
print(not_end)

# score = 10
# is_over = score >= 10 and is_end == True
score = 8
is_over = score >= 10 or is_end ==True
print(is_over); print(score)

# item = [5, True, "Speak"]

Monsters_posit = [2, 23 , 10 ,2]
print(Monsters_posit)

print(len(Monsters_posit))
print(Monsters_posit[0])

Monsters_posit[1] = 21
print(Monsters_posit)

print(Monsters_posit[0:2])

Monsters_posit.append(25)
print(Monsters_posit)

Monsters_posit.insert(3,55)
print(Monsters_posit)

Monsters_posit.remove(55)
print(Monsters_posit)

del(Monsters_posit[3])
print(Monsters_posit)

Monsters_posit.append("null")
print(Monsters_posit)

high_score = ("Nemesis", 2222)
print(high_score)

high_score = ("Monal", 150)
print(high_score)

polly = high_score[0]
print(polly)

print(len(high_score))

print("Nemesis" in high_score)
print("Monal" in high_score)

print(polly[0])
print(polly[0:2])
print("Mo" in polly)
print(len(polly))

# dict = {key:vaule, key:vaule}
actions = {"r":1, "l":-1}
print(actions)

print(actions["r"])
print(actions.get("g"))

actions["r"] = 2
actions["h"] = 5
print(actions)

print(actions.keys())
print(actions.values())
print(actions.items())

del(actions["r"])
print(actions)

actions.pop("h")
print(actions)

print("l" in actions)

key = "u"

if key == "r":
  print("move right")
elif key == "l":
  print("move left")
else:
  print("Key not in code lol!")

print("fin")