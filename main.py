import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    parser = argparse.ArgumentParser(description="Magic's Chatbot feat. Gemini")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if api_key == None:
        raise RuntimeError("API key did not load <sadface>")
    client = genai.Client(api_key = api_key)
    for _ in range(20):
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
        )
        if response.usage_metadata == None:
            raise RuntimeError("Metadata does not exist <sadface>")
        if args.verbose == True:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)
        if response.function_calls is not None:
            results_list = []
            for function in response.function_calls:
                function_call_result = call_function(function, verbose=args.verbose)
                if function_call_result.parts == []:
                    raise Exception("'Parts' is be empty but should not be")
                if function_call_result.parts[0].function_response == None:
                    raise Exception("'function_response' should not be None but is")
                if function_call_result.parts[0].function_response.response == None:
                    raise Exception("'response' is None but it should not be")
                results_list.append(function_call_result.parts[0])
                if args.verbose == True:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
            messages.append(types.Content(role="user", parts=results_list))
        else:
            print(response.text)
            return
    print("Agent hit the iteration limit without a final response.")
    sys.exit(1)

if __name__ == "__main__":
    main()