def merge_sort(list):
  if len(list) > 1:
    mid = len(list) // 2

    left = list[:mid]
    right = list[mid:]


    merge_sort(left)
    merge_sort(right)

    left_index = 0
    right_index = 0
    merged_list_idx = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            list[merged_list_idx] = left[left_index]
            left_index = left_index + 1
        else:
            list[merged_list_idx] = right[right_index]
            right_index = right_index + 1
        merged_list_idx = merged_list_idx + 1

    while left_index < len(left):
        list[merged_list_idx] = left[left_index]
        left_index += 1
        merged_list_idx += 1

    while right_index < len(right):
        list[merged_list_idx] = right[right_index]
        right_index += 1
        merged_list_idx += 1

  return list
