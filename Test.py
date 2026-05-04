import sys
# Import necessary libraries here as your team builds the modules
# import ast
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

def input_module():
    """
    Module 1: Accept multiple source code files from the user.
    """
    print("\n[+] Running Input Module...")
    # TODO: Write logic to read .py files from a specific directory or user input
    print("Files loaded successfully. (Dummy message)")
    return ["student_code_1.py", "student_code_2.py"] # Dummy return

def preprocessing(files):
    """
    Module 2: Remove comments, whitespace, and normalize variable names.
    """
    print("\n[+] Running Preprocessing...")
    # TODO (Rahoul): Implement regex or string manipulation to clean the raw code
    print("Code preprocessed successfully.")
    return "cleaned_code_data"

def tokenization(cleaned_code):
    """
    Module 3: Break code into meaningful tokens.
    """
    print("\n[+] Running Tokenization...")
    # TODO: Implement tokenization logic (can use Python's built-in tokenize module)
    print("Tokenization complete.")
    return "tokens"

def feature_extraction(tokens):
    """
    Module 4: Apply TF-IDF for textual features and AST for structural features.
    """
    print("\n[+] Running Feature Extraction...")
    # TODO (Dua Fatima): Integrate scikit-learn TF-IDF vectorization and Python's AST parsing
    print("Features extracted (TF-IDF & AST).")
    return "features"

def similarity_computation(features):
    """
    Module 5: Use cosine similarity and structural comparison.
    """
    print("\n[+] Running Similarity Computation...")
    # TODO: Calculate cosine similarity score based on extracted features
    print("Similarity scores computed.")
    return 85.5 # Dummy similarity score

def output_generation(score):
    """
    Module 6: Display similarity percentage and highlight matching sections.
    """
    print("\n[+] Running Output Generation...")
    # TODO: Format the final output for the CLI (Later can be shifted to Streamlit/Flask)
    print(f"Final Result: Overall Code Similarity is {score}%")

def main_menu():
    while True:
        print("\n" + "="*55)
        print("    AI-BASED CODE PLAGIARISM DETECTOR - MAIN MENU")
        print("="*55)
        print("1. Run Full Pipeline (End-to-End Test)")
        print("2. Test Input Module")
        print("3. Test Preprocessing Module")
        print("4. Test Tokenization Module")
        print("5. Test Feature Extraction Module")
        print("6. Test Similarity Computation Module")
        print("7. Test Output Generation Module")
        print("8. Exit")
        print("="*55)

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            # End-to-end integration flow
            files = input_module()
            cleaned = preprocessing(files)
            tokens = tokenization(cleaned)
            features = feature_extraction(tokens)
            score = similarity_computation(features)
            output_generation(score)
            
        elif choice == '2':
            input_module()
        elif choice == '3':
            preprocessing("dummy_files")
        elif choice == '4':
            tokenization("dummy_cleaned_code")
        elif choice == '5':
            feature_extraction("dummy_tokens")
        elif choice == '6':
            similarity_computation("dummy_features")
        elif choice == '7':
            output_generation(85.5)
        elif choice == '8':
            print("Exiting system. Allah Hafiz!")
            sys.exit()
        else:
            print("Invalid choice! Please select a valid option (1-8).")

if __name__ == "__main__":
    main_menu()