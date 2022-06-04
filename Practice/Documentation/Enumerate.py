# enumerate(<collection-object>) generates temporary indices for any collection object
# In this example, enumerate(exercises) generates indices for the Set 'exercises'

exercises = {"Push up", "Sit up", "Pull up", "Bench press", "Biceps curl"}

for sl,exercise in enumerate(exercises):  # indices and the values are referred to as 'sl' and 'exercise' respectively
    print(f"{sl+1}.{exercise}")