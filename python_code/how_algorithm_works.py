'''
The ‘data’ are presented as matrix with 4 columns. Each row of the matrix represents a participant, to refer to the particular participant index numbers are used. Each column of the matrix is an indicator that corresponds to one of the scores of the tests on the basis of which the participants have been allocated to the different groups. The results of four tests have been taken into account. There are emotion detection-, mental verb comprehension-, theory of mind- and pragmatic tests.

The distance between two students was calculated. In order to do so, the cosine between four-dimentional vectors was measured. Then, by using the function scipy.spatial.distance.cosine which returns the value «1–cosine» was obtained the distance matrix of all children of the class (‘dist_matrix’) . Thus, the closer vectors are, the less number in ‘dist_matrix’ is.

Then, with the function ‘np.argmin’ was calculated a minimum of all distances and its location (a vector) – (min_index=np.unravel_index(np.argmin(dist_matrix, axis=None), dist_matrix.shape)). This way the pares of close vectors in min_index were found.  
'''

#In cycle
while len(group1) < int(rows/2) and len(group2) < int(rows/2):
    min_index = np.unravel_index(np.argmin(dist_matrix, axis=None), dist_matrix.shape)#find next two closest vectors
    #
    if (np.sum(min_index[0] == group1) > 0 or np.sum(min_index[0] == group2) > 0) and (np.sum(min_index[1] == group1) > 0 or np.sum(min_index[1] == group2) > 0):
        dist_matrix[min_index] = 2 # if they both are already in group1 or group2 - skip these two vectors
        continue
    elif np.sum(min_index[0] == group1) > 0 or np.sum(min_index[0] == group2) > 0:
        if np.sum(min_index[0] == group1) > 0: # if first of them is in group1, then we put the  second one uin group2
            group2 = np.append(group2, min_index[1])
        else:
            group1 = np.append(group1, min_index[1]) # if first of them is in group2, then we put the  second one uin group1
    elif np.sum(min_index[1] == group1) > 0 or np.sum(min_index[1] == group2) > 0: #symmetrically if second one is in group1 or group2
        if np.sum(min_index[1] == group1) > 0:
            group2 = np.append(group2, min_index[0])
        else:
            group1 = np.append(group1, min_index[0])
    else: # if no were in some group - then just put in different groups
        group1 = np.append(group1, min_index[0])
        group2 = np.append(group2, min_index[1])
    dist_matrix[min_index] = 2
	
'''
The algorithm stops when one of the groups contains half of the students. The remaining participants are assigned to the other group.
'''
used = np.append(group1, group2)
all = set(np.arange(rows))
found = set(used)
other = np.array(list(all.difference(found)))
if len(group1) < len(group2):
    group1 = np.append(group1, other)
else:
    group2 = np.append(group2, other)


