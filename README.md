# AI agents with python 

lets try python with openai models. 

1. install uv - a rust installer

https://docs.astral.sh/uv/getting-started/installation/#standalone-installer


1.1 and install the requests library

```
% uv add requests
```

1.2 dotenv package

```
% uv add python-dotenv
```

# run the application locally by

```
% uv run main.py
```




Prompt engineering tip:

<em>use XML delimiters</em>
this helps the LLM- model to understand better the difference between prompts and the input

```
    <topic>
    {topic}
    </topic>
```
