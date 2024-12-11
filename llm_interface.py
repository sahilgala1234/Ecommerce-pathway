import openai
import env
openai.api_key = env.api_key
def generate_befunge_code(target_output):
    prompt = f"""You are an expert in Befunge programming.
    Generate the shortest possible Befunge code that produces the following output:
    {target_output}
    Ensure the code is functional and optimized."""
    
    response = openai.chat.completions.create(
    model="gpt-4o-mini",  # Replace with the desired model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Generate Befunge code for 'Hello, World!'."}
    ]
      )
    print(response['choices'][0]['message']['content'].strip())  