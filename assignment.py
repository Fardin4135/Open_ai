import openai

API_KEY = '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'

def filter_content(response):
    """Basic filtering mechanism to detect inappropriate content."""
    blocked_words = ["violence", "hate", "illegal", "explicit"]
    for word in blocked_words:
        if word in response.lower():
            return "[Content Blocked: Inappropriate Response]"
    return response

def generate_response(prompt):
    """Calls OpenAI's API to generate a response."""
    
    try:
         client = openai.OpenAI(api_key=API_KEY)
         response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
         return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main function to take user input and generate AI response."""
    user_input = input("Enter your query: ")
    response = generate_response(user_input)
    print("\nAI Response:", response)

if __name__ == "__main__":
    main()
