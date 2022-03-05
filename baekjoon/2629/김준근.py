weights_count = int(input())
weights = list(map(int, input().split()))

marbles_count = int(input())
marbles = list(map(int, input().split()))

measurable_weights = {weights[0]}

for weight_index in range(1, len(weights)):
    weight = weights[weight_index]
    new_measurable_weights = {weight}
    for measurable_weight in measurable_weights:
        new_measurable_weights.add(measurable_weight + weight)
        new_measurable_weights.add(abs(measurable_weight - weight))
    measurable_weights = measurable_weights.union(new_measurable_weights)

for marble in marbles:
    print("Y" if marble in measurable_weights else "N", end=" ")
