def likes(names):
  match names:
    case []:
      return "no one likes this"
    case [name1]:
      return f"{name1} likes this"
    case [name1, name2]:
      return f"{name1} and {name2} like this"
    case [name1,name2,name3]:
      return f"{name1}, {name2} and {name3} like this"
    case [name1, name2, *rest]:
      return f"{name1}, {name2} and {len(rest)} others like this"
​
​