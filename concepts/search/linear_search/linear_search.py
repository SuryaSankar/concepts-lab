def linear_search(input_list: list[int], search_term: int) -> int:
    for i, item in enumerate(input_list):
        if item == search_term:
            return i
    return None

if __name__ == "__main__":
    test_data = [{
        "input_list": [3, 5, 8, 9, 12, 1, 34],
        "search_term": 9,
        "expected_output": 3
    }, {
        "input_list": [3, 5, 8, 9, 12, 1, 34],
        "search_term": 5,
        "expected_output": 1
    }]
    for data in test_data:
        expected = data['expected_output']
        actual = linear_search(data["input_list"], data["search_term"])
        print("Expected: {}, Actual: {}".format(expected, actual))
        assert expected == actual