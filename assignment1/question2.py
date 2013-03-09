def parse_links_regex(filename):
    """question 2a

    Using the re module, write a function that takes a path to an HTML file
    (assuming the HTML is well-formed) as input and returns a dictionary
    whose keys are the text of the links in the file and whose values are
    the URLs to which those links correspond. Be careful about how you handle
    the case in which the same text is used to link to different urls.
    
    For example:

        You can get file 1 <a href="1.file">here</a>.
        You can get file 2 <a href="2.file">here</a>.

    What does it make the most sense to do here? Concatenate them all!
    """
    # no idea why we use re...
    import re
    
    try:
        html = open(filename,"r")
        html_string = html.read()
        data = re.findall('<a.+href=[\'|\"](.+)[\'|\"].*?>(.+)</a>', html_string)

        dictionary = {}
        for (URL,link) in data:
            # handling the case where the link is already there.
            if link in dictionary:
                dictionary[link] += " and " + URL
            else:
                dictionary[link] = URL

        return dictionary
                

    except IOError:
        print ("File {} does not exist".format(filename))

def parse_links_xpath(filename):
    """question 2b

    Do the same using xpath and the lxml library from http://lxml.de rather
    than regular expressions.
    
    Which approach is better? (Hint: http://goo.gl/mzl9t)
    """
    try:
        html = open(filename,"r")
        html_string = html.read()
        data = re.findall('<a.+href=[\'|\"](.+)[\'|\"].*?>(.+)</a>', html_string)

        dictionary = {}
        for (URL,link) in data:
            # handling the case where the link is already there.
            if link in dictionary:
                dictionary[link] += " and " + URL
            else:
                dictionary[link] = URL

        return dictionary
                

    except IOError:
        print ("File {} does not exist".format(filename))
