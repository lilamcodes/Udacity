import urllib.request as request
import urllib.parse as parse


def read_text():

    quotes = open(r"C:\Users\IBM_ADMIN\Desktop\movie_quotes.txt")   
    contents_of_file = quotes.read()
    print(contents_of_file)

    quotes.close()
    check_profanity(contents_of_file)

def check_profanity (text):
    url = 'http://www.wdylike.appspot.com/?q='
    q = parse.quote(text)

    connection = request.urlopen(url+q)
    output = connection.read()
    print(output)
    connection.close()

    if "true" in str(output):
       print("Profanity Alert!!")
    elif "false" in str(output):
         print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")


read_text()
