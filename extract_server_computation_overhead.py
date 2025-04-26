import re


def extract_times(filename):
    # Lists to store the extracted times
    deserialize_times = []
    agg_serialization_times = []

    try:
        # Open and read the file
        with open(filename, 'r') as file:
            # Read all lines
            lines = file.readlines()

            # Regular expressions to match the time values
            deserialize_pattern = r'Deserialize time: (\d+\.\d+)s'
            agg_serialization_pattern = r'Aggregation\+Serialization time: (\d+\.\d+)s'

            # Process each line
            for line in lines:
                # Extract Deserialize time
                deserialize_match = re.search(deserialize_pattern, line)
                if deserialize_match:
                    deserialize_times.append(float(deserialize_match.group(1)))

                # Extract Aggregation+Serialization time
                agg_serialization_match = re.search(agg_serialization_pattern, line)
                if agg_serialization_match:
                    agg_serialization_times.append(float(agg_serialization_match.group(1)))

        return deserialize_times, agg_serialization_times

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return [], []
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return [], []


def analyze_times(times, measurement_name):
    if not times:
        print(f"No {measurement_name} data to analyze.")
        return

    minimum = min(times)
    maximum = max(times)
    avg_min_max = (minimum + maximum) / 2

    print(f"\n{measurement_name} Analysis:")
    print("-" * 50)
    print(f"Minimum: {minimum:.4f}s")
    print(f"Maximum: {maximum:.4f}s")
    print(f"Average of Min and Max: {avg_min_max:.4f}s")
    print(f"Overall Average: {sum(times) / len(times):.4f}s")


def print_times(deserialize_times, agg_serialization_times):
    print("\nExtracted Times:")
    print("-" * 50)
    print(f"Number of entries: {len(deserialize_times)}")
    print("\nDeserialize Times (s):")
    for i, time in enumerate(deserialize_times, 1):
        print(f"Entry {i}: {time}")
    print("\nAggregation+Serialization Times (s):")
    for i, time in enumerate(agg_serialization_times, 1):
        print(f"Entry {i}: {time}")

    # Perform analysis for both measurements
    analyze_times(deserialize_times, "Deserialize")
    analyze_times(agg_serialization_times, "Aggregation+Serialization")


# Example usage
if __name__ == "__main__":
    filename = "server_timing_log.txt"  # Replace with your actual filename

    # Extract the times
    deserialize_times, agg_serialization_times = extract_times(filename)

    # Print the results
    if deserialize_times or agg_serialization_times:
        print_times(deserialize_times, agg_serialization_times)
    else:
        print("No data extracted.")