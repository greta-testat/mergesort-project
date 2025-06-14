import matplotlib.pyplot as plt

def merge_sort(list_to_sort_by_merge):

    if len(list_to_sort_by_merge) <= 1:
        return

    mid = len(list_to_sort_by_merge) // 2
    left_half = list_to_sort_by_merge[:mid]
    right_half = list_to_sort_by_merge[mid:]

    # Recursively sort both halves
    merge_sort(left_half)
    merge_sort(right_half)

    # Merge the sorted halves
    left_index = right_index = merged_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            list_to_sort_by_merge[merged_index] = left_half[left_index]
            left_index += 1
        else:
            list_to_sort_by_merge[merged_index] = right_half[right_index]
            right_index += 1
        merged_index += 1

    # Copy remaining elements of left_half, if any
    while left_index < len(left_half):
        list_to_sort_by_merge[merged_index] = left_half[left_index]
        left_index += 1
        merged_index += 1

    # Copy remaining elements of right_half, if any
    while right_index < len(right_half):
        list_to_sort_by_merge[merged_index] = right_half[right_index]
        right_index += 1
        merged_index += 1

def plot_list(data, title, color):
    x = range(len(data))
    plt.figure(figsize=(8, 4))
    plt.plot(x, data, marker='o', color=color, label=title)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.legend()
    plt.show()



if __name__ == "__main__":
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    # Before sorting
    plot_list(my_list, "Unsortiert", color="red")

    # Sort the list
    merge_sort(my_list)

    # After sorting
    plot_list(my_list, "Sortiert", color="green")

      