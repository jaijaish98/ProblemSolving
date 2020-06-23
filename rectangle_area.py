"""
Rectangle Area
https://leetcode.com/problems/rectangle-area/
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45

"""


def compute_area(A, B, C, D, E, F, G, H):
    left_boundary = max(A, E)
    right_boundary = min(C, G)

    top_boundary = min(D, H)
    bottom_bondary = max(B, F)

    area_1 = (C - A) * (D - B)
    area_2 = (G - E) * (H - F)

    if (left_boundary < right_boundary) and (bottom_bondary < top_boundary):
        # area_1 and area_2 has overlapped area
        intersection = (right_boundary - left_boundary) * (top_boundary - bottom_bondary)

    else:
        # area_1 and area_2 has no overlapped area
        intersection = 0

    return area_1 + area_2 - intersection


if __name__ == "__main__":
    area = compute_area(A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2)
    print(area)