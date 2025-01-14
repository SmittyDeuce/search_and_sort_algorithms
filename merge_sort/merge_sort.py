# from flask import Flask, request, jsonify


# Video Sorting with Merge Sort
# Objective: The objective of this assignment is to implement the merge sort algorithm to sort a list of videos based on their titles.

# Problem Statement: You are tasked with developing a
# video sorting function that sorts a list of videos
# alphabetically by their titles using the merge sort
# algorithm. This application will help users organize
# their video collections more efficiently. You should
# use the previous assignment project.



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


# Task 1:
# Implement the merge sort algorithm in Python to sort videos
# by their titles..

def merge_sort(arr):
    if len(arr) >1: #base case: stop if the array has 1 or no elements
        mid = len(arr) // 2 # find the midpoint to split the array
        left_half = arr[:mid] #slice from idx 0 to mid -1
        right_half = arr[mid:] #slice from arr idx mid to end

        merge_sort(left_half) 
        merge_sort(right_half) 

        '''
        ^^^^^^^
        merge_sort(lft_half/right) constantly calls func on array
        to split array until its only 1 and 1 on each side first it
        does to left half then to right 
        '''




        i = j = k = 0

        #Merge sorted halves, arr[0] will be smallest number before
        #incrementing up
        while i < len(left_half) and j < len(right_half):  # Continue until one of the halves is exhausted
            if left_half[i] < right_half[j]:  # Compare elements from left and right halves
                arr[k] = left_half[i]  # If left element is smaller, place it in the merged array
                i += 1  # Move pointer in left_half to the next element
            else:
                arr[k] = right_half[j]  # Otherwise, place the right element in the merged array
                j += 1  # Move pointer in right_half to the next element
            k += 1  # Move the pointer in the merged array to the next position


        '''
        ^^^^^^^
        After the main while loop, we've merged as many elements as possible from both halves.
        But there may be remaining elements in either the left_half or right_half.
        Now, we handle those leftovers separately using two additional loops.
        '''

        # Copy remaining elements from left_half (if any)
        while i < len(left_half):  
            arr[k] = left_half[i]  # Place the remaining element from left_half into arr
            i += 1  # Move pointer in left_half to the next element
            k += 1  # Move pointer in merged array

        # Copy remaining elements from right_half (if any)
        while j < len(right_half):  
            arr[k] = right_half[j]  # Place the remaining element from right_half into arr
            j += 1  # Move pointer in right_half to the next element
            k += 1  # Move pointer in merged array


        '''
        ^^^^^^^
        After these two loops, all remaining elements from either half will be copied into arr.
        The result will be a fully sorted array.
        '''

        
# Task 2:
# Develop another REST API endpoint using Flask that allows
# users to fetch a list of videos sorting alphabetically by
# their titles using the merge sort developed in Task 1.





# Task 3:
# Test the video sorting functionality using Postman or a similar tool. Send requests to the API endpoint created in Task 2 and verify its correctness and efficiency. Ensure that the API returns the expected results.





# Expected Outcomes:

# Successful implementation of the merge sort algorithm for sorting
# videos alphabetically by title.

# Correct sorting of video titles, enhancing the
# organization of video collections.

# NOTE: Ensure that all code in your file is ready to run.
# This means that if someone opens your file and clicks the
# run button at the top, all code executes as intended.

# For example, if there are if statements, print statements,
# or for loops, they should function correctly and display
# output in the console as expected. If you have a function,
# make sure the function is called and runs. If there are
# classes/objects, make sure they are instantiated and the
# methods are called.