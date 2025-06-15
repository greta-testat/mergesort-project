import matplotlib.pyplot as plt

def merge_sort(list_to_sort_by_merge):
    # abbrechen, wenn die liste 0/1 elemente hat
    if len(list_to_sort_by_merge) <= 1:
        return

    # mitte berechnen, für 2 hälften 
    mid = len(list_to_sort_by_merge) // 2
    # linke hälfte
    left_half = list_to_sort_by_merge[:mid]
    # rechte hälfte
    right_half = list_to_sort_by_merge[mid:]

    # linke hälfte wird sortiert (rekursiv)
    merge_sort(left_half)
    # rechte hälfte wird sortiert (rekursiv)
    merge_sort(right_half)

    # index initialieren für links, rechts und gemergte liste
    left_index = right_index = merged_index = 0

    # listen vergöeichen (und haben beide listen überhaupt elemente?)
    # das kleinste element kommt zurück in die originalliste
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            list_to_sort_by_merge[merged_index] = left_half[left_index]
            left_index += 1
        else:
            list_to_sort_by_merge[merged_index] = right_half[right_index]
            right_index += 1
        merged_index += 1

    # sind elemente über (links), kommen sie auch in die originalliste 
    while left_index < len(left_half):
        list_to_sort_by_merge[merged_index] = left_half[left_index]
        left_index += 1
        merged_index += 1

    # sind elemente über (rechts), kommen sie auch in die originalliste 
    while right_index < len(right_half):
        list_to_sort_by_merge[merged_index] = right_half[right_index]
        right_index += 1
        merged_index += 1


def plot_list(data, title, color):
    # x-achse erstelllen (indexe der daten)
    x = range(len(data))
    plt.figure(figsize=(6, 4))
    # plot erstellen 
    plt.plot(x, data, marker='o', color=color, label=title)
    plt.title(title)            
    plt.xlabel("Index")    
    plt.ylabel("Value")        
    plt.grid(True)
    plt.legend()
    plt.show()

# wird ausgeführt, wenn das skript gestartet wird 
if __name__ == "__main__":
    # beispiel
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    # plot unsortierte liste
    plot_list(my_list, "Unsortiert", color="red")

    # mit merge sort sortieren
    merge_sort(my_list)

    # plot sortierte liste
    plot_list(my_list, "Sortiert", color="green")
