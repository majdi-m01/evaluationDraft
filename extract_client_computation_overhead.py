# Lists to store all mins and maxes across all clients
all_min_trains = []
all_max_trains = []
all_min_encrypt_serialize = []
all_max_encrypt_serialize = []
all_min_decrypt_deserialize = []
all_max_decrypt_deserialize = []

# Loop through clients 1 to 10
for client_num in range(1, 11):
    filename = f'client_{client_num}_log.txt'

    # Initialize lists to store times for each category
    train_times = []
    encrypt_serialize_times = []
    decrypt_deserialize_times = []

    # Open and read the file
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove leading/trailing whitespace
                line = line.strip()
                if line:  # Skip empty lines
                    # Split the line into parts based on ", "
                    parts = line.split(", ")
                    if len(parts) == 4:  # Ensure the line has exactly 4 parts
                        try:
                            # Extract time values by splitting on ": " and removing 's'
                            train_time_str = parts[1].split(": ")[1].replace('s', '')
                            encrypt_serialize_time_str = parts[2].split(": ")[1].replace('s', '')
                            decrypt_deserialize_time_str = parts[3].split(": ")[1].replace('s', '')

                            # Convert strings to floats
                            train_time = float(train_time_str)
                            encrypt_serialize_time = float(encrypt_serialize_time_str)
                            decrypt_deserialize_time = float(decrypt_deserialize_time_str)

                            # Append times to respective lists
                            train_times.append(train_time)
                            encrypt_serialize_times.append(encrypt_serialize_time)
                            decrypt_deserialize_times.append(decrypt_deserialize_time)
                        except (IndexError, ValueError):
                            print(f"Skipping malformed line in {filename}: {line}")
                            continue

        # Print header for current client
        print(f"\nResults for {filename}:")

        # Check if any data was collected
        if train_times:
            # Calculate minimum and maximum times for each category
            min_train = min(train_times)
            max_train = max(train_times)
            min_encrypt_serialize = min(encrypt_serialize_times)
            max_encrypt_serialize = max(encrypt_serialize_times)
            min_decrypt_deserialize = min(decrypt_deserialize_times)
            max_decrypt_deserialize = max(decrypt_deserialize_times)

            # Store mins and maxes for overall calculation
            all_min_trains.append(min_train)
            all_max_trains.append(max_train)
            all_min_encrypt_serialize.append(min_encrypt_serialize)
            all_max_encrypt_serialize.append(max_encrypt_serialize)
            all_min_decrypt_deserialize.append(min_decrypt_deserialize)
            all_max_decrypt_deserialize.append(max_decrypt_deserialize)

            # Print the results with 4 decimal places
            print("Training time:")
            print(f"  Min: {min_train:.4f}s")
            print(f"  Max: {max_train:.4f}s")
            print("Encrypt+Serialize time:")
            print(f"  Min: {min_encrypt_serialize:.4f}s")
            print(f"  Max: {max_encrypt_serialize:.4f}s")
            print("Decrypt+Deserialize time:")
            print(f"  Min: {min_decrypt_deserialize:.4f}s")
            print(f"  Max: {max_decrypt_deserialize:.4f}s")
        else:
            print("No valid data found in the file.")

    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error processing {filename}: {str(e)}")

# Calculate and display overall statistics
if all_min_trains:  # Check if we have any data
    print("\nOverall Statistics Across All Clients:")

    # Training time overall stats
    overall_min_train = min(all_min_trains)
    overall_max_train = max(all_max_trains)
    train_avg = (overall_min_train + overall_max_train) / 2

    print("Training time (Overall):")
    print(f"  Minimum of all minimums: {overall_min_train:.4f}s")
    print(f"  Maximum of all maximums: {overall_max_train:.4f}s")
    print(f"  Average of extremes: {train_avg:.4f}s")

    # Encrypt+Serialize overall stats
    overall_min_encrypt = min(all_min_encrypt_serialize)
    overall_max_encrypt = max(all_max_encrypt_serialize)
    encrypt_avg = (overall_min_encrypt + overall_max_encrypt) / 2

    print("Encrypt+Serialize time (Overall):")
    print(f"  Minimum of all minimums: {overall_min_encrypt:.4f}s")
    print(f"  Maximum of all maximums: {overall_max_encrypt:.4f}s")
    print(f"  Average of extremes: {encrypt_avg:.4f}s")

    # Decrypt+Deserialize overall stats
    overall_min_decrypt = min(all_min_decrypt_deserialize)
    overall_max_decrypt = max(all_max_decrypt_deserialize)
    decrypt_avg = (overall_min_decrypt + overall_max_decrypt) / 2

    print("Decrypt+Deserialize time (Overall):")
    print(f"  Minimum of all minimums: {overall_min_decrypt:.4f}s")
    print(f"  Maximum of all maximums: {overall_max_decrypt:.4f}s")
    print(f"  Average of extremes: {decrypt_avg:.4f}s")
else:
    print("\nNo valid data found across all files.")