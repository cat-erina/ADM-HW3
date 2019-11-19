# parser.py

# In other to save the info into tsv files, we've executed the following lines

# The path to my html files
paths = '/Users/yves/Desktop/Data_Science/first_year/first_semester/adm/adm_hw3/html_files/'

    
for filename in os.listdir(paths):
    if filename not in movies_done:
        if filename.endswith(".html"):
            ff = open(paths + filename, 'r') # open the HTML page
            html = ff.read()
            film = BeautifulSoup(html)

            page_name = filename.rstrip('.html') # extract the name of the file without extension and we will use this as the file id            
            movie_number = re.findall('\d+', filename )
            movie_number = movie_number[0]
            
            
            #save the info into tsv files

            # The path to my tsv folder
            with open('/Users/yves/Desktop/Data_Science/first_year/first_semester/adm/adm_hw3/tsv_files/'+page_name+'.tsv', 'wt') as out_file:
                tsv_writer = csv.writer(out_file, delimiter='\t')
                if info_tsv(film,movie_number , filename) is None or len(info_tsv(film, movie_number, filename)) == 0:
                    continue
                else:
                    for col in info_tsv(film, movie_number, filename):
                        tsv_writer.writerow([col[0], col[1]])
            print('tsv created '+ str(len(movies_done)))

            continue

        else:
            continue
    else:
        continue
print('DONE')