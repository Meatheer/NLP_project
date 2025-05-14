from spellChecker import SpellChecker

test_cases = [
    {"text": "The quick brown fox jumps over the lazy dog.", "expected_errors": []},
    {"text": "Python is an interpreted, high-level language.", "expected_errors": []},
    {"text": "The REST API is NOT working!", "expected_errors": []},  
    {"text": "I'm gonna leave now.", "expected_errors": []},       
    {"text": "It's 42°F outside.", "expected_errors": []},             
    {"text": "I recieved the package yesterday.", "expected_errors": ["recieved"]},
    {"text": "This is an independant study.", "expected_errors": ["independant"]},
    {"text": "She has a seperate room.", "expected_errors": ["seperate"]},
    {"text": "Don't stop believin'.", "expected_errors": ["believin'"]},
    {"text": "The quokka smiled.", "expected_errors": []},
    {"text": "Ths is a obvius error.", "expected_errors": ["ths", "obvius"]},
    {"text": "Teh cat sat on teh mat.", "expected_errors": ["teh", "teh"]},
    {"text": "They're going to it's place.", "expected_errors": ["it's"]},
    {"text": "Many pepole agrees on the concensus of the meeting", "expected_errors": ["pepole","agrees","concensus"]},
    {"text": "The Lab had all the equiptment requird", "expected_errors": ["equiptment", "requird"]},
    {"text": "She is independant woman", "expected_errors": ["independant"]},
    {"text": "The text is not readible", "expected_errors": ["readible"]},
    {"text": "This tool is not  usible", "expected_errors": ["usible"]},
    {"text": "He reciedved the adress yesterday", "expected_errors": ["reciedved", "adress"]},
    {"text": "Their going to the libary now", "expected_errors": ["Their", "libary"]},
]

def evaluate_spell_checker(test_cases):
    checker = SpellChecker()
    results = {
        "true_positives": 0,
        "false_positives": 0,
        "false_negatives": 0,
        "true_negatives": 0,
    }

    for i, case in enumerate(test_cases, 1):
        text = case["text"]
        expected_errors = set(case["expected_errors"])
        predicted_errors = set(checker.check_text(text))

        words = text.split()
        total_words = len(words)

        tp = predicted_errors & expected_errors
        fp = predicted_errors - expected_errors
        fn = expected_errors - predicted_errors

        # TN is what's left after TP, FP, FN
        tn = total_words - (len(tp) + len(fp) + len(fn))

        results["true_positives"] += len(tp)
        results["false_positives"] += len(fp)
        results["false_negatives"] += len(fn)
        results["true_negatives"] += tn

        print(f"Test {i}: \"{text}\"")
        print(f"  Expected Errors: {sorted(expected_errors)}")
        print(f"  Predicted Errors: {sorted(predicted_errors)}")
        print(f"  True Positives: {sorted(tp)}")
        print(f"  False Positives: {sorted(fp)}")
        print(f"  False Negatives: {sorted(fn)}")
        print(f"  True Negatives: {tn}\n")

    tp = results["true_positives"]
    fp = results["false_positives"]
    fn = results["false_negatives"]
    tn = results["true_negatives"]

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    accuracy = (tp + tn) / (tp + fp + fn + tn) if (tp + fp + fn + tn) > 0 else 0

    print(f"---\nOverall Results:")
    print(f"TP = {tp}, FP = {fp}, FN = {fn}, TN = {tn}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-Score: {f1:.2f}")
    print(f"Accuracy: {accuracy:.2f}")

evaluate_spell_checker(test_cases)
