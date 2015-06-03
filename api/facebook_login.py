import facebook

token = ''

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me". "friends")

