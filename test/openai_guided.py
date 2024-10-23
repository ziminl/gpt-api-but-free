import openai


openai.api_key = 'api_key'

def edit_code(code):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Please edit the following code and return only the edited code:\n\n{code}"}
        ]
    )
    return response.choices[0].message['content'].strip()


code_to_edit = """
print("test code")
"""

edited_code = edit_code(code_to_edit)
print(edited_code)
