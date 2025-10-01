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

1.3 openapi package for python

```
% uv add openapi
```


### run the application locally by

```
% uv run main.py
```




## Prompt engineering tip:

1. <em>use XML delimiters</em>
this helps the LLM- model to understand better the difference between prompts and the input

```
    <topic>
    {topic}
    </topic>
```

2. <em>Few shot prompting</em>
- provide some samples of topic and result so the quality increases
- use xml'-ish structure for this. 
- Here are some examples of good X posts:
```
    <example-1>
        <topic>Product Launch new website</topic>
        <generated-post>
            Just launched our new product! Check it out on our website. 🚀 #NewProduct #LaunchDay
            Thank you for your support! 🙌
            We're excited to hear your feedback. 😊
        </generated-post>
    </example-1>
```


## Troubleshooting with python:
- pip3 is with python3 connected. had to sym-linking to `pip`  in z-shell profile with alias.
- upgrade pip3 to latest with: `pip3 install --upgrade pip`
- `uv sync` after pip install sometimes helps
- un-install and re-install libraries helps.
- de-activate all python extensions in vscode
- clean uv cache with: `uv cache prune` && `uv cache clean`.
- re-install python with uv: `uv python install --reinstall`
