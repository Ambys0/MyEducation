import pickle
original =  {'Illinois': 'Aurora', 'Massachusetts': 'Boston', 'Florida': 'Orlando'}

pickled = pickle.dumps(original)
uclenched = pickle.loads(pickled)

print(original)
print(pickled)
print(uclenched)