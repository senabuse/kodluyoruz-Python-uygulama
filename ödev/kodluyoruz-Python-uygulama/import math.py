import math
# Noktaların tanımlanması
points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)
# Minimum mesafenin bulunması
min_distance = min(distances)
print("Noktalar arasındaki minimum Öklid mesafesi:", min_distance)