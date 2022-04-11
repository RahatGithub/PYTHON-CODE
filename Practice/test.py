# ***Task: Find the max/min score***

scores = {'Hayden':111, 'Gilchrist':117, 'Ponting':129, 'Symonds':87}
current_scores = {'Maxwell':142, 'Carey':46, 'Wade':82}

scores.update(current_scores)
aus_scores = scores.copy()
print(scores)
print(aus_scores)
del scores['Carey']
aus_scores['Wade'] = 101

# for key in scores: print(key, ':', scores[key])
# print('_______________________________________')
# for key in scores: print(key, ':', aus_scores[key])
# print(scores)