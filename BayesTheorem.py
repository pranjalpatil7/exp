def bayes_theorem(p_a, p_b_given_a, p_b):
    # Compute posterior probability P(A|B) using Bayes' Theorem.
    return (p_b_given_a * p_a) / p_b

def main():
    print("Bayes Theorem Formula: P(A|B) = [P(B|A) * P(A)] / P(B)\n")

    try:
        # Taking user inputs
        p_a = float(input("Enter prior probability P(A): "))
        p_b_given_a = float(input("Enter conditional probability P(B|A): "))
        p_b = float(input("Enter total probability P(B): "))

        # Validating inputs
        if not (0 <= p_a <= 1 and 0 <= p_b_given_a <= 1 and 0 <= p_b <= 1):
            print("\nError: Probabilities must be between 0 and 1.")
            return

        if p_b == 0:
            print("\nError: P(B) cannot be zero.")
            return

        # Calculating posterior probability
        p_a_given_b = bayes_theorem(p_a, p_b_given_a, p_b)

        # Displaying results
        print("\nUsing Bayes' Theorem:")
        print(f"P(A|B) = ({p_b_given_a} × {p_a}) / {p_b}")
        print(f"\nPosterior Probability P(A|B) = {p_a_given_b:.4f}")
        print(f"That means there's a {p_a_given_b * 100:.2f}% probability of A given B.\n")

    except ValueError:
        print("\nInvalid input! Please enter numeric values between 0 and 1.")

if __name__ == "__main__":
    main()

# Bayes Theorem Formula: P(A|B) = [P(B|A) * P(A)] / P(B)

# Enter prior probability P(A): 0.2
# Enter conditional probability P(B|A): 0.4
# Enter total probability P(B): 0.6

# Using Bayes' Theorem:
# P(A|B) = (0.4 × 0.2) / 0.6

# Posterior Probability P(A|B) = 0.1333
# That means there's a 13.33% probability of A given B.