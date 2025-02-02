# Simple Calculation 2.0
def main():
    scores = []  # List to store quiz scores

    while True:
        score = input("Enter a quiz score (or type 'q' to quit):\n")

        if score.lower() == 'q':
            break

        
        if score.isdigit():
            scores.append(float(score))  
        else:
            print("Invalid input! Please enter a valid quiz score!")

        
        another = input("Do you want to enter another quiz score? (y/n): ").strip().lower()
        if another not in ['y', 'yes']:
            break

    
    if scores:
        average_score = sum(scores) / len(scores)
        print(f"The average quiz score is: {average_score:.2f}")
    else:
        print("No scores were entered.")

if __name__ == "__main__":
    main()

    