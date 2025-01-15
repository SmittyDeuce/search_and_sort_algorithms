from flask import Flask, request, jsonify
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
    "Artificial Intelligence Revolution",]

# Sorted list of video titles for binary search
sorted_video = sorted(video_titles)

# You can use this list video_titles in your Python
# code for further processing or manipulation.

# Task 1:

# Implement the binary search algorithm for searching
# videos by title.



# Task 1: Binary search implementation
def binary_search(arr, target):
    """
    Perform binary search on a sorted list.

    Parameters:
    - arr (list): Sorted list to search in.
    - target (str): Title to search for.

    Returns:
    - int: Index of the found title, or -1 if not found.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid].lower() == target.lower():
            return mid
        elif arr[mid].lower() < target.lower():
            low = mid + 1
        else:
            high = mid - 1
    return -1


# print(binary_search(sorted_video, "The Art of Coding"))

# Task 2:

# Develop a REST API endpoint using Flask that
# allows users to search for videos by their titles
# using the binary search developed in Task 1.
# This API should accept a search query as input
# and return the matching videos, if any.


# Task 2: Flask REST API
app = Flask(__name__)

@app.route("/titles", methods=["POST"])
def add_titles():
    """
    Add new titles to the video list.
    Expects a JSON payload with a "video_titles" key containing a list of titles.
    """
    global video_titles, sorted_video
    data = request.json
    if not data or "video_titles" not in data or not isinstance(data["video_titles"], list):
        return jsonify({"error": "Invalid data format"}), 400

    video_titles += data["video_titles"]
    sorted_video = sorted(video_titles)
    return jsonify({"message": "Titles added successfully!"}), 201

@app.route("/titles/search", methods=["GET"])
def search_title():
    """
    Search for a video title using binary search.
    Accepts a "query" parameter in the request URL.
    """
    query = request.args.get("query", "").strip()
    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Perform binary search
    index = binary_search(sorted_video, query)
    if index != -1:
        return jsonify({"found": True, "index": index, "title": sorted_video[index]}), 200
    return jsonify({"found": False, "message": "Title not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

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