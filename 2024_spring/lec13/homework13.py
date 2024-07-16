import bs4
import gtts

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.
    
    @params: 
    text (string): the text of a webpage
    
    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    soup = bs4.BeautifulSoup(text, 'html.parser')
    stories = []
    
    for item in soup.find_all('article'):
        title = item.find(['h1', 'h2', 'h3']).get_text(strip=True) if item.find(['h1', 'h2', 'h3']) else ''
        teaser = item.find('p').get_text(strip=True) if item.find('p') else ''
        stories.append((title, teaser))
    
    return stories

def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.
    
    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio

    Output: None
    '''
    if n < 0 or n >= len(stories):
        raise IndexError("Story index out of range")
    
    title, teaser = stories[n]
    text_to_read = f"Title: {title}. Teaser: {teaser}"
    
    tts = gtts.gTTS(text=text_to_read, lang='en')
    tts.save(filename)
