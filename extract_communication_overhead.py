def calculate_average_size(filename):
    try:
        # Initialize variables
        total_size = 0
        count = 0

        # Open and read the file
        with open(filename, 'r') as file:
            for line in file:
                # Look for lines containing "size" and extract the number
                if "size" in line:
                    # Split the line and get the number after "size"
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if part == "size" and i + 1 < len(parts):
                            size_str = parts[i + 1]
                            # Remove any non-digit characters except the number
                            size = int(''.join(filter(str.isdigit, size_str)))
                            total_size += size
                            count += 1

        # Calculate and return average
        if count > 0:
            average = total_size / count
            return average, count
        else:
            return 0, 0

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return None, None


def main():
    filename = "server_comm_log.txt"
    average, count = calculate_average_size(filename)

    if average is not None and count is not None:
        if count > 0:
            print(f"Processed {count} entries")
            print(f"Total size: {int(average * count)} bytes")
            print(f"Average size: {average:,.2f} bytes")
        else:
            print("No size data found in the file")


if __name__ == "__main__":
    main()