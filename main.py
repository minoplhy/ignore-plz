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
