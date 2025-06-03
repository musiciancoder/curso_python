animals1 = ("dog","giraffe","elephant","lion","tiger")

print(sorted(animals1))

animals2 = sorted(animals1, reverse=True, key= lambda s: len(s))

print(animals2)