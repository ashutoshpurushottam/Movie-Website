import media
import fresh_tomatoes


# Create instance of six favorite movies

toy_story = media.Movie("Toy Story",
    "A story of a boy and his toys that come to life",
    "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

interstellar = media.Movie("Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival",
    "http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar3.jpg",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

gone_girl = media.Movie("Gone Girl",
    "With his wife's disappearance having become the focus of an intense media circus,"
    "a man sees the spotlight turned on him when it's suspected that he may not be innocent",
    "http://sheilas.org.au/wp-content/uploads/2014/10/Gone-Girl-poster-31.jpg",
    "https://www.youtube.com/watch?v=Ym3LB0lOJ0o")

her = media.Movie("Her",
    "A lonely writer develops an unlikely relationship with his newly purchased operating system"
    "that's designed to meet his every need",
    "https://shyfyy.files.wordpress.com/2013/08/her1.jpg",
    "https://www.youtube.com/watch?v=WzV6mXIOVl4")


creed = media.Movie("Creed",
    "The former World Heavyweight Champion Rocky Balboa serves as a trainer and"
    "mentor to Adonis Johnson, the son of his late friend and former rival Apollo Creed",
    "http://cdn2-www.comingsoon.net/assets/uploads/gallery/creed/creedpostersmall.jpg",
    "https://www.youtube.com/watch?v=Uv554B7YHk4")


movies = [toy_story, avatar, interstellar, gone_girl, her, creed]
fresh_tomatoes.open_movies_page(movies)
