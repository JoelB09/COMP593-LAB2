def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name': 'Joel Bahati',
        'student_id': 10276278,
        'pizza_toppings': ['BBQ CHICKEN', 'ITALIAN SAUSAGE', 'RED PEPPERS' ],
         'movies': [
            {
                'wall street': 'crime/fiction'
            },
            {
                'ready player one': 'scifi' 
            }

         ]

    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {
        '21 jump street': 'action/comedy'
    }
    about_me['movies'].insert(2, new_movie)
    
    
    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me, ('bacon', 'olives', 'ham'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me) 
    print_movie_titles(about_me)


# TODO: Step 4 - Function that prints student name and ID	   
def print_student_name_and_id(about_me):
    first_name = about_me['full_name'].split()[0] 
    print(f"my name is {about_me['full_name']} but you can call me Lord {first_name}.")  
    print(f"My student ID is {about_me['student_id']}")
    return 
    
       
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'] = sorted(about_me['pizza_toppings'], key=lambda x: x.lower()) 
    about_me['pizza_toppings'] = [topping.lower() for topping in about_me['pizza_toppings']]

        

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for topping in about_me['pizza_toppings']:
        print(f"- {topping}")
             
           

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [value for movie in about_me['movies'] for value in movie.values()]
    n = len(genres)
    if n > 1:
        genres[-1] = "and " + genres[-1]
    print("I like to watch", ", ".join(genres),"movies")




# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(about_me):
    movie_list = [list(movie.keys())[0] for movie in about_me['movies']]
    n = len(movie_list)
    if n > 1:
        movie_list[-1] = "and " + movie_list[-1]
    print("Some of my favourite movies are", ", ".join(movie_list)+".", "😊")
        
if __name__ == '__main__':
  main()
  main()

