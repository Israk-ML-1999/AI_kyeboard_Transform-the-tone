import requests
import json

def test_generate_text(mood, prompt):
    response = requests.post(
        "http://localhost:8000/api/generate",
        json={
            "mood": mood,
            "prompt": prompt
        }
    )
    return response.json()

# Test examples
test_cases = [
    {
        "mood": "happy",
        "prompt": "Transform this text within 60 words: I went to the store and bought some groceries. The weather was cloudy and it started raining on my way back."
    },
    {
        "mood": "sad",
        "prompt": "Transform this text in 30 words: I got a promotion at work today and my colleagues congratulated me."
    },
    {
        "mood": "roma
        ntic",
        "prompt": "We had dinner at a restaurant and watched a movie together. Word count: 40"
    },
    {
        "mood": "excited",
        "prompt": "I'm going to visit my parents this weekend. We'll probably have a quiet dinner at home. Limit: 25 words"
    },
    {
        "mood": "peaceful",
        "prompt": "The city was busy with traffic and people rushing to work. I had to wait in line for my coffee."
    },
    {
        "mood": "nostalgic",
        "prompt": "Transform this text within 50 words: I'm starting a new job next week in a different city. I've packed all my things and ready to move."
    }
]

# Run all test cases
for i, test in enumerate(test_cases, 1):
    print(f"\nTest Case {i}:")
    print(f"Mood: {test['mood']}")
    print(f"Original Text: {test['prompt']}")
    print("\nResponse:")
    result = test_generate_text(test['mood'], test['prompt'])
    print(json.dumps(result, indent=2))
    print("-" * 80) 