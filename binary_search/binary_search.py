# Video Search Application with Binary Search
# Objective: The objective of this assignment is to develop a
# video search application that utilizes the binary search
# algorithm to quickly find specific videos in a sorted list.

# Problem Statement: You are tasked with building a
# video search function that allows users to search
# for videos by their titles using the binary search
# algorithm. This function should provide fast and
# efficient search functionality, enhancing the user experience.

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

# You can use this list video_titles in your Python
# code for further processing or manipulation.

# Task 1:

# Implement the binary search algorithm for searching
# videos by title.



def binary_search(arr, target):
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] ==  target:
            return f"Title found at index {mid}"
        
        else:
            high = mid - 1

    return "Title is not inside data base"

print(binary_search(video_titles, "The Art of Coding"))

# Task 2:

# Develop a REST API endpoint using Flask that
# allows users to search for videos by their titles
# using the binary search developed in Task 1.
# This API should accept a search query as input
# and return the matching videos, if any.



# Task 3:

# Test the video search functionality using Postman 
# r a similar tool. Send requests to the API endpoint
# created in Task 2 with different search queries to
# verify its correctness and efficiency. Ensure that
# the API returns the expected results for both
# existing and non-existing videos.




# Expected Outcomes:

# Successful implementation of the binary search algorithm for efficient searching of videos by title.
# Development of a robust REST API endpoint using Flask, integrating the binary search algorithm from Task 1 to provide fast and accurate video search functionality.
# Verify the correctness and efficiency of the search algorithm, confirming that the API returns the expected results for both existing and non-existing videos.