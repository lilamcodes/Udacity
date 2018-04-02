import fresh_tomatoes
import media

the_matrix = media.Movie("The Matrix", "A story of dystopian future in which reality as perceived by most humans is actually a simulated reality. ","https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", "https://youtu.be/vKQi3bBA1y8")

#print(the_matrix.storyline)

apocalypto= media.Movie("Apocalypto", "In the Maya civilization, a peaceful tribe is brutally attacked by warriors seeking slaves and human beings for sacrifice. ","https://upload.wikimedia.org/wikipedia/en/6/62/Apocalypto-poster01.jpg", "https://youtu.be/pXuwjdQx924")

#print(apocalypto.storyline)

#apocalypto.show_trailer()

a_i= media.Movie("A.I. Artificial Intelligence", "A highly advanced robotic boy longs to become real so that he can regain the love of his human mother. ","https://upload.wikimedia.org/wikipedia/en/e/e6/AI_Poster.jpg", "https://www.youtube.com/watch?v=oBUAQGwzGk0")

#print(a_i.storyline)

fifth_element= media.Movie("The Fifth Element", "The only hope for mankind is the Fifth Element, who comes to Earth every five thousand years to protect the humans with four stones of the four elements: fire, water, Earth and air","https://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg", "https://youtu.be/fQ9RqgcR24g")

#print(fifth_element)

swing_kids= media.Movie("Swing Kids", "A close-knit group of young kids in Nazi Germany listen to banned swing music from the US ","https://upload.wikimedia.org/wikipedia/en/f/f8/Swing_kids.jpg", "https://youtu.be/43GN5BAXuHQ")



basketball_diaries= media.Movie("The Basketball Diaries", "As a member of a seemingly unbeatable high school basketball squad, Jim's life centers around the basketball court and the court becomes a metaphor for the world in his mind. ","https://upload.wikimedia.org/wikipedia/en/2/26/The_Basketball_Diaries_Poster.jpg", "https://youtu.be/NyfX9UHyxgY")



edwards_scissorhands= media.Movie("Edward Scissorhands", "A scientist (Vincent Price) builds an animated human being -- the gentle Edward ","https://upload.wikimedia.org/wikipedia/en/3/3b/Edwardscissorhandsposter.JPG", "https://youtu.be/M94yyfWy-KI")



battle_royale= media.Movie("Battle Royale", "A group of ninth-grade students from a Japanese high school have been forced by legislation to compete in a Battle Royale. ","https://upload.wikimedia.org/wikipedia/en/e/eb/Battle_Royale-japanese-film-poster.jpg", "https://youtu.be/N0p1t-dC7Ko")



lo= media.Movie("Lo", "A man uses a demon to save his girlfriend but the demon has a nefarious plan. ","https://upload.wikimedia.org/wikipedia/en/b/b7/Lo_%28film%29.jpg", "https://youtu.be/XhFsK7e8wUo")


movies =[the_matrix, apocalypto,a_i,fifth_element,swing_kids, basketball_diaries, edwards_scissorhands,battle_royale, lo]

fresh_tomatoes.open_movies_page(movies)
