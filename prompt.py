"""
Prompt the Claude model and return the results
1. get the long context prompt (parse and collect it in another file)
2. get the question from the user
3. put together the long_context_prompt and the question via a template format
4. call the model and get the results
"""

import os
key = os.environ['CLAUDE_KEY']


import os
import anthropic

client = anthropic.Client(key)


#with open("context_prompt.txt", "r") as f:
#    document = f.read()
#
#question = "what is 123120 times 1203914?"
#
#prompt_str =f"""{anthropic.HUMAN_PROMPT}The follow are the resource about how to use large language model and 
#teach how to prompt the large langauge model (LLM) to get the best results out of it.
#Please learn about LLM and the art of prompting, I'll ask use how to help me prompt after you read the following resource.
#
#
#{document}
#
#Based on the above tutorial, please help me prompt the following question: 
#```
#{question}
#```
#
#Be sure to explain your reason and provide a detail explanation of how you prompt the model to get the answer.
#
#{anthropic.AI_PROMPT}"""
#
#response = client.completion(
#    prompt=prompt_str,
#    stop_sequences = [anthropic.HUMAN_PROMPT],
#    model="claude-instant-v1-100k",
#    max_tokens_to_sample=512,
#)
#
#
#print(response)


# Make the above into a function
def prompt_claude(question):
    with open("context_prompt.txt", "r") as f:
        document = f.read()

    prompt_str =f"""{anthropic.HUMAN_PROMPT}The follow are the resource about how to use large language model and 
    teach how to prompt the large langauge model (LLM) to get the best results out of it.
    Please learn about LLM and the art of prompting, I'll ask use how to help me prompt after you read the following resource.


    {document}

    Based on the above tutorial, please help me make my prompt better:
    ```
    {question}
    ```

    Be sure to explain your reason and provide a detail explanation of how you prompt the model to get the answer.
    The prompting method you describe need to be very good so that the LLM can answer the question correctly and informatively even if consider the shortcoming of LLM.
    

    {anthropic.AI_PROMPT}"""

    response = client.completion(
        prompt=prompt_str,
        stop_sequences = [anthropic.HUMAN_PROMPT],
        model="claude-v1.3-100k",
        max_tokens_to_sample=512,
    )

    return response

if __name__ == "__main__":
    question = "what is 123120 times 1203914?"
    response = prompt_claude(question)
    print(response)