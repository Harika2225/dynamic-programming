def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Step 1: Sort intervals based on the start time
    # The lambda x: x[0] part just says: "Use the first element (x[0]) of each interval as the sorting key."
    intervals.sort(key=lambda x: x[0]) #
    
    # Step 2: Initialize merged list with the first interval
    merged = [intervals[0]]
    
    # Step 3: Iterate through the rest
    for current in intervals[1:]:
        # Gets the last interval from the merged list.
        last = merged[-1]
        
        # If they overlap, merge them
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    
    return merged

intervals = [[8, 10], [1, 3], [2, 6], [15, 18]]
print(merge_intervals(intervals))