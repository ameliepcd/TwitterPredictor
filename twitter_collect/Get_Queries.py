
def get_candidate_queries(file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    mon_fichier = open(file_path,'r')
    queries=[]
    for line in mon_fichier:
        a=line.replace('\n','')
        queries.append(a)
    return(queries)

#print(get_candidate_queries('hashtag_candidate_2.txt'))


