const bubbleSort = require('./bubbleSort');

test('sorting [1, 23, 43, 11, 12] to equal [1, 11, 12, 23, 43]', () => {
    const sortedList = bubbleSort([1, 23, 43, 11, 12]);
    expect(sortedList).toEqual([1, 11, 12, 23, 43]);
});