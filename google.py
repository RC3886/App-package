from googlesearch import search


class Googling:

    def my_search(self):
        search_mode = True
        while search_mode:
            query = input("Enter your query or press 0 to return back to the menu. ")
            if query == 0:
                search_mode = False
            else:
                for i in search(query, tld="com", num=10, stop=10, pause=1):    # prefer .com,10 results,request rate 1s
                    print(i)



