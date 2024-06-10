from openai import OpenAI
from arsewards import arsewards_dict
key = arsewards_dict["oai2"]
import tiktoken


client = OpenAI(api_key=key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {"role": "system", "content": "You are an assistant."},
    {"role": "user", "content": "Explain recursion in programming in a short, simple way."}
  ]
)

print(completion.choices[0].message['content'])
print(completion.choices[0].message)
'''
encoding = tiktoken.get_encoding("cl100k_base")

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
print(num_tokens_from_string(arsewards_dict["resumeShort"], "cl100k_base"))

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  #header = {"Authorization": "Bearer " + key},
  messages=[
    {"role": "system", "content": "You are applying for a role as a python developer. You have three years of experience"},
    #{"role": "assistant", "content": arsewards_dict["resumeShort"]},
    {"role": "user", "content": "How many years of experience in python do you have?"}
  ]
)
print(response)'''