
import fresh_tomatoes
import media

# toy story movie
toy_story = media.Movie("Toy Story",
						"A story of talking toys....",
						r"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
						r"https://www.youtube.com/watch?v=Bj4gS1JQzjk")

# forrest gump
forrest_gump = media.Movie("Forrest Gump",
							"Forrest Gump is a 1994 American comedy-drama film based on the 1986 novel of the same name by Winston Groom.",
							r"http://t0.gstatic.com/images?q=tbn:ANd9GcSppDgk99BKVA4TJtWc1FN4-HUkdWrFNfMm1-M0nQ01sIOcbTZu",
							r"https://www.youtube.com/watch?v=uPIEn0M8su0")

# 3 idiots
three_idiots = media.Movie("3 Idiots",
							"Three college student's story",
							r"http://www.gstatic.com/tv/thumb/movieposters/7951929/p7951929_p_v8_aa.jpg",
							r"https://www.youtube.com/watch?v=xvszmNXdM4w")

#lagaan
lagaan = media.Movie("Lagaan",
						"Lagaan (English: Taxation) is a 2001 Indian epic sports-drama film written and directed by Ashutosh Gowariker.",
						r"http://www.gstatic.com/tv/thumb/movieposters/27923/p27923_p_v8_aa.jpg",
						r"https://www.youtube.com/watch?v=oSIGQ0YkFxs")

#chak de india
chack_de_india = media.Movie("Chack De India",
								"Indian sports film",
								r"http://www.gstatic.com/tv/thumb/movieposters/168383/p168383_p_v8_ae.jpg",
								r"https://www.youtube.com/watch?v=6a0-dSMWm5g")

#dangal
dangal = media.Movie("Dangal",
						"Indian Hindi-language biographical sports drama film",
						r"http://t3.gstatic.com/images?q=tbn:ANd9GcQIXnFlBKGWT1ByyIu3qfxX6opQX6BmeeU_qsiE3X8rX9ZRr63r",
						r"https://www.youtube.com/watch?v=x_7YlGv9u1g&t=13s")

#airlift
#airlift = media.Movie("Airlift",
#						"Airlift is a 2016 Indian historical drama film directed by Raja Krishna Menon",
#						r"https://en.wikipedia.org/wiki/Airlift_(film)#/media/File:Airlift_poster.jpg",
#						r"https://www.youtube.com/watch?v=vb5xCMbMfZ0")

movie_list = [toy_story, forrest_gump, three_idiots, lagaan, chack_de_india, dangal]

fresh_tomatoes.open_movies_page(movie_list)