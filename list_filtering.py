li = ["a", "mpilgrim", "foo", "b", "c", "d"]

print [elem for elem in li if len(elem) > 1]

print [elem for elem in li if elem != "b"]

print [elem for elem in li if li.count(elem) == 1]