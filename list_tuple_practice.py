movies = []
mov1= input("enter your  first  movie :")
movies.append(mov1)
mov2= input("enter your  second movie :")
movies.append(mov2)
mov3= input("enter your  third  movie :")
movies.append(mov3)

print(movies)

mov4 = input("add your forth movie :")
movies.insert(0,mov4)

print(movies)


deleted_movie = movies.pop()
print("removed movie : ",deleted_movie)
print(movies)

print("tuple count")
gread = ("a","b","c","a","a","b",)
print("tuple:",gread)
print(gread.count("a"))






