from collections import Counter

def calculate_similarity_score(list1, list2):
    # Count the occurrences of each number in list2
    count_list2 = Counter(list2)
    
    # Calculate the similarity score
    similarity_score = 0
    for num in list1:
        similarity_score += num * count_list2[num]
    
    return similarity_score

def read_pairs_from_file(file_path):
    list1 = []
    list2 = []
    
    with open(file_path, 'r') as file:
        for line in file:
            pair = line.strip().split()
            list1.append(int(pair[0]))
            list2.append(int(pair[1]))
    
    return list1, list2

def calculate_sum_of_distances(list1, list2):
    # Sort both lists
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    
    # Calculate distances between pairs
    distances = [abs(a - b) for a, b in zip(sorted_list1, sorted_list2)]
    
    # Calculate the sum of distances
    sum_of_distances = sum(distances)
    
    return sum_of_distances

# Read pairs from the file
file_path = 'input.txt'
list1, list2 = read_pairs_from_file(file_path)

# Calculate the sum of distances
sum_of_distances = calculate_sum_of_distances(list1, list2)

# Print the sum of distances
print(f"The sum of distances between pairs is: {sum_of_distances}")

# Calculate the similarity score
similarity_score = calculate_similarity_score(list1, list2)

# Print the similarity score
print(f"The similarity score of the two lists is: {similarity_score}")