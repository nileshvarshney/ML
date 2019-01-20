# You need to process items in an iterable, but for whatever reason,
# you can’t or don’t want to use a for loop.

with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end=' ')
    except StopIteration:
        pass

items = [1, 2, 3, 4]
item = iter(items)
print(next(item))
print(next(item))

# Forward iterator
def f_range(start, end, step):
    x = start
    while x < end:
        yield x
        x += step


print([item for item in f_range(40, 50, 1)])


# countdown iterator
def count_down(start):
    x = start
    while x > 0:
        yield x
        x -= 1


c = count_down(3)
print(next(c))
print(next(c))



