num_arr = [8, 4, 23, 42, 16, 15]


def insertion_sort(num_arr):
  for idx_current in range(len(num_arr)-1):
    # if idx in num_arr
    temp = num_arr[idx_current]
    print(f"***temp's current index value: {idx_current}\n***")
    print(f"***temp's current array value: {temp}\n***")
    # assign temp to idx

    next_idx = idx_current+1
    print(f"Next_idx index value: {next_idx}\n")
    #assign at next index after initial iteration
    while next_idx >= 0 and temp < num_arr[next_idx]:
        # print ("Next_idx index value: {next_idx}")
        num_arr[next_idx+1] = num_arr[next_idx]

        next_idx -= 1
        temp = num_arr[next_idx+1]
        print(f"temp's current value: {temp}\n ****")

  return num_arr

insertion_sort(num_arr)

