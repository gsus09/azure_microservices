
clients = [("Alice", 25, 5), ("Bob", 35, 12), ("Catherine", 30, 15), ("David", 45, 8)]

# Lambda function to filter clients based on age and interaction count
filter_clients = lambda client: client[1] > 30 and client[2] > 10

# Lambda function to transform the filtered data
transform_data = lambda client: (client[0], 'high engagement')

filtered_clients = list(filter(filter_clients, clients))
print(list(map(transform_data, filtered_clients)))  # Expected output: [('Bob', 'high engagement')]