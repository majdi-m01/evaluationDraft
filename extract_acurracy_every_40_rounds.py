def calculate_accuracy_averages(filename):
    try:
        # Lists to store accuracies and averages
        accuracies = []
        averages = []

        # Read the file
        with open(filename, 'r') as file:
            lines = file.readlines()

            # Process each line
            for i, line in enumerate(lines, 1):
                # Extract accuracy value from the line
                try:
                    # Split the line by comma and get the accuracy part
                    accuracy_part = line.strip().split(',')[1]
                    # Extract the number from "Accuracy: XX.XX"
                    accuracy = float(accuracy_part.split(':')[1].strip())
                    accuracies.append(accuracy)
                except (IndexError, ValueError) as e:
                    print(f"Error processing line {i}: {line.strip()}")
                    continue

                # Calculate average every 40 rounds
                if i % 40 == 0:
                    if accuracies:
                        avg = sum(accuracies[-40:]) / 40
                        averages.append(avg)
                        print(f"Average accuracy for rounds {i - 39} to {i}: {avg:.2f}")

            # Handle remaining rounds if total isn't multiple of 40
            remaining = len(accuracies) % 40
            if remaining > 0:
                last_batch = accuracies[-remaining:]
                avg = sum(last_batch) / remaining
                averages.append(avg)
                print(f"Average accuracy for final {remaining} rounds: {avg:.2f}")

        return averages

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []


# Example usage
if __name__ == "__main__":
    filename = "metrics_log.txt"  # Replace with your file name
    averages = calculate_accuracy_averages(filename)

    # Print summary
    if averages:
        print("\nSummary of all averages:")
        for i, avg in enumerate(averages, 1):
            print(f"Batch {i}: {avg:.2f}")