# Homework 3: What movie to watch tonight?

## Authors
* **Yves Gaetan Nana Teukam**
* **Caterina Alfano**
* **Meher Kavya Koppisetti**

## Objective
The goal of this assignment is to create a search engine for movies.<br/>
To make this possible downloaded 30000 wikipedia paged about movies and then retrieved the most important informations to create an inverted index to 
compute our queries. The query's result are then ordered by similarity to the query (using the Cosine Similarity and the tdidf methods). <br/>
Laslty we also added our own ranking method to order the results of the query.

The Homework also includes an algorithmic question: how to find the length of the longest palindrome substring in a give string

### Repository Structure

Our Repository contains the following files:

* `README.md`: a Markdown file that explains the content of your repository. 
* `collector.py`: a python file that contains the line of code needed to collect data from the `html` page and Wikipedia.
* `collector_utils.py`: a python file that stores the function used in `collector.py`.
* `parser.py`: a python file that contains the line of code needed to parse the entire collection of `html` pages and save those in `tsv` files.
* `parser_utils.py`: a python file that gathers the function used in `parser.py`.
* `index.py`: a python file that once executed generate the indexes of the Search engines.
* `index_utils.py`: a python file that contains the functions used for creating indexes.
* `utils.py`: a python file that gather functions needed in more than one of the previous files.
* `main.py`: a python file that once executed builds up the search engine. 
* `exercise_4.py`: python file that contains the implementation of the algorithm that solves problem 4.
* `main.ipynb`: a Jupyter notebook explaines the strategies you adopted solving the homework and the Bonus point (visualization task). The notebook must be clear, complete and tidy. [Here](https://github.com/dusicastepic/ADMSecondHomework/blob/master/ADM_HW2_Full.ipynb) an example of a nice notebook from last year. **Avoid** pushing on GitHub notebook that contain entire long printed list, otherwise we will not be able to open it.




