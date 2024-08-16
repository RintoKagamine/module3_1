calls = 0
def contain_calls():
    global calls
    calls += 1
def string_info(s):
    contain_calls()
    return len(s), s.upper(), s.lower()


def is_contains(s, l):
    contain_calls()
    l_ = [i.lower() for i in l]
    return s.lower() in l_

print(string_info('skdER'))
print(is_contains('sD', ['Sd']))
print(calls)