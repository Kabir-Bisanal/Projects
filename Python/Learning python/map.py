names = ["kabir","rahul","kakashi","kruskal","suresh","raja"]
def names_with_k(name):
    return name[0] == 'k'
new_names = list(filter(names_with_k,names))
print(new_names)