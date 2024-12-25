calls = 0

def count_calls():
    global calls
    calls += 1

def strig_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains (string, list_to_search):
    count_calls()
    return string.lower() in [s.lower() for s in list_to_search]

print(strig_info('Capybara'))
print(strig_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)