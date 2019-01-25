import string

original = "map"

table = string.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
)

print()
original.translate(table)
