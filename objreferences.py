li = ["Larry", "Curly"]
print getattr(li, "pop")
print li.pop
print getattr(li, "append")("Moe")
print li
print getattr({}, "clear")
print getattr((), "pop")