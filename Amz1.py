import math

def calculate_sum_of_qualities(packets, channels):
    packets.sort(reverse=True)  # Sort packets in descending order

    if len(packets) < channels:
        return 0

    channel_packets = [[] for _ in range(channels)]
    for packet in packets:
        min_channel = min(channel_packets, key=lambda x: sum(x))
        min_channel.append(packet)

    sum_of_qualities = 0
    for channel in channel_packets:
        median = sorted(channel)[len(channel) // 2]  # Median calculation
        sum_of_qualities += median

    return math.ceil(sum_of_qualities)  # Round up to the next higher integer

# Example usage
packets = [89, 48, 14]
channels = 2
result = calculate_sum_of_qualities(packets, channels)
print(result)
