"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        
    {
        "input": [[1, 2, 3, 4, 5]],
        "answer": True
    },
    {
        "input": [[5, 4, 3, 2, 1]],
        "answer": False
    },
    {
        "input": [[]],
        "answer": True
    },
    {
        "input": [[1]],
        "answer": True
    }

    ]
}
