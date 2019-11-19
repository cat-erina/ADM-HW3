# collector_utils.py

# In order to extract the info from infobox of the html pages we created a function called 'info_tsv'
# We've also created a function to clean the rows of the infobox called 'clean_col'

# The following function is to clean the rows of the intobox
def clean_col(string):
    clean1 = string.strip('\n') # remove all escape characters
    pattern = r'\[.*?\]'  # remove all square brakets and content
    clean2 = re.sub(pattern, '', clean1)
    return(clean2)

# The following function is to extract info from the intobox

# This function takes three inputs:
# The first input is the html page - from which the info is going to be extracted.
# The second input is a number associated to the page (This number is an identificator number, 
# thanks to which we will be able to retrieve the url of the html page).
# The third input is the name given to the html page.

def info_tsv(film_soup, movie_number, filename):  
    
    # This is the list of the info we want to take from the infobox
    infb = ['Directed by', 'Produced by', 'Written by', 'Screenplay by',
           'Story by', 'Based on', 'Starring', 'Narrated by', 'Music by',
           'Cinematography', 'Edited by', 'Production company', 
            'Distributed by', 'Release date', 'Running time', 'Country',
           'Language', 'Budget'] 
    
    # remove all square brakets and content
    pattern = r'\[.*?\]' 
    
    # This list will be a list of list, and each list inside will contain the infobox related to each row, the Into and Plot
    L = []  
        
    # Retrieve the Title   
        
    Initial_Title = film_soup.select("#firstHeading")[0].text
    L.append(['Title', str(Initial_Title)])
    
    # Retrieve the Intro
     
    contents = film_soup.findAll('div', attrs={'id': 'toc'}) 
    if len(contents) > 0:
        Intr = contents[0].fetchPreviousSiblings('p') # give us all the paragraphs from the end of the first section
        # These paragraphs correspond to the Intro
        Intro = []
        if len(Intr) > 0:
            for p in reversed(Intr):  # we order the paragraphs as they should be (same order as in the original html page)
                if len(p.text) > 5:  # If a paragraph has less than five strings we do not consider it to be a paragraph
                    Intro.append(p.text)  # The treshold len(p.text) > 5 help us to remove all empty and meaningless paragraphs
                else:
                    continue
            Intro = ''.join(Intro)
            Final_intro = re.sub(pattern, '', Intro)  # remove all the square brakets and what it contains, because  
                                                      # These brakets are Wikipedia notes/citations
            if len(Final_intro)>20: # If a section, in this case the Intro, has less than 20 strings, we do consider it to be meaningless
                L.append(['Intro', Final_intro.strip()])  # we save the info we've got from the intro
            else:
                L.append(['Intro', 'NA'])  # in case we don't have any info, we put an 'NA'
    
    
    # Retrieve the Plot
    
    plot = []
    
    # Before starting looking for the info in the plot, we created a list of the most used names to indicate the section Plot
    possibles = ['Plot','Synopsis','Plot synopsis','Plot summary', 'Plot_summary', 'Plot_synopsis'
                 'Story','Plotline','The Beginning','Summary',
                'Content','Premise', 'Intro', 'Intro']
    for i in possibles:
        items = film_soup.find(id=i) # se find the section with name == ith element in possibles
        if items is None or len(items) == 0:
            continue
        else:
            # walk through the siblings of the parent (H2) node 
            # until we reach the next H2 node
            for element in items.parent.nextSiblingGenerator():  # we basically take all the paragraphs till the end of the section
                if element.name == "h2":
                    break
                if hasattr(element, "text"):
                    plot.append(element.text)
    plot = "".join(plot)
    # remove all square brakets and content
    Final_plot = re.sub(pattern, '', plot)
    if len(Final_plot) > 20:  # same as before (for the Intro), in case the whole section has less than 20 string, we considered it meaningless
        L.append(['Plot', Final_plot.strip()])  # we save the info found in the Plot
    else:
        L.append(['Plot', 'NA']) # in case we don't have any info, we put an 'NA'
    
    # Retrieve info in the infobox
    
    # we have found the infobox by not only looking for the tables in the page but by section the table with class = 'infobox vevent'  
    if len(film_soup.findAll('table', {'class': 'infobox vevent'}))>0:  
        
        # If the box is not empty we go through it
        if len(film_soup.findAll('table', {'class': 'infobox vevent'})[0].tbody.findAll('tr'))>0:
            
            # from the infobox the firt row correspond to the Name of the Film
            Title = film_soup.findAll('table', {'class': 'infobox vevent'})[0].tbody.findAll('tr')[0].text
            
            # If a title contains more than 75 strings we do not consider it to a title, because it could be some additional 
            # messages inserted in the pages
            if len(Title)>75:
                
                L.append(['Name', 'NA']) # in case we don't have any info, we put an 'NA'
            else:
                L.append(['Name', Title]) # we save the Name of the film
            
        else:
            L.append(['Name', 'NA']) # in case we don't have any info, we put an 'NA'
    
    
    # In the following table we will put all the info that we've retreived from the infobox - except the name.
    # The the idea, is to do an intersection between the elements found and the elements we wanted to found
    # for all the missing elements we will put 'NA'
    
    in_table = [] # This list will contain all the info found in the infobox
    
    # check if the table is not empty
    if len(film_soup.findAll('table', {'class': 'infobox vevent'}))>0: 
        
        # check if the row is not empty
        if len(film_soup.findAll('table', {'class': 'infobox vevent'})[0].tbody.findAll('tr'))>0:
            
            #go through the columns of each row
            for row in film_soup.findAll('table', {'class': 'infobox vevent'})[0].tbody.findAll('tr')[1:]:
                
                # check that the first column is not empty
                first_col = row.findAll('th') 
                if len(first_col)>0:
                    
                    # extract and check the second column
                    second_col = row.findAll('td')
                    if len(second_col)>0:
                        
                        # external rows can contain internal rows. 
                        # extract elements in each row 
                        second_col = []
                        for element in row.findAll('td')[0]:
                            # check if the element in the row has a child
                            if isinstance(element, Tag):
                                second_col.append(element.text) # collect all the info found in this row
                            else:
                                second_col.append(element)
                        second_col = ' '.join(second_col)
                        
                        new_second_col = clean_col(second_col) # clean the output -calling the initial function

                        in_table.append(first_col[0].text) # save the feature of the row ex. 'Directed by'
                        in_table.append(new_second_col)  # save the info corresponding to this feature
                        

            # put 'NA' to all missing values
            for i in infb:
                if i in in_table:
                    index = in_table.index(i)
                    L.append([i, in_table[index +1]])
                else:
                    L.append([i, 'NA']) # in case we don't have any info, we put an 'NA'
    L.append(['Url', List_url[int(movie_number) -1]])  # from the list of the urls we take url of this html page
    return(L) # we return all the info we need to save in the tsv files.