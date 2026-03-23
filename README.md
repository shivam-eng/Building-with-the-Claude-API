# BUILDING WITH CLAUDE API

## OVERVIEW

This Repository is based on the [Building with the Claude API Course](https://anthropic.skilljar.com/claude-with-the-anthropic-api) provided on [Anthropic Academy](https://www.anthropic.com/learn). This consists of Hands-on Exercise which can be performed in order to learn Claude API. The course covers Integrating Claude AI into applications using the Anthropic API. Course is covered on API Operations, advanced prompting techniques, tool integration. Through hands-on exercises and practical examples, we will to implement conversational AI, retrieval-augmented generation, automated workflows, and leverage Claude's multimodal capabilities for processing text, images, and documents.

## TOOLS USED

- Python 3.12.10
- Anthropic Claude Model
- Jupyter Notebook

## PREREQUISITES

- Install Python Version 3.x
- Jupyter Notebook installed in VSCode / Launch Jupyter Lab through Anaconda Navigator
- Sign up for an API key from Anthropic (https://www.anthropic.com/) [Store the key in .env file as "ANTHROPIC_API_KEY=your_key_here"]

## GETTING STARTED

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies using pip:
   ```
   %pip install anthropic python-dotenv
   ```
3. Launch Jupyter Notebook in your preferred Editor / App.
4. The Exercises are designed chapter-wise.
   For eg., Chapter 1: Accessing Claude with API [Follow the sequence of exercises as per the folder structure in Readme.md]
   Chapter 2: Prompt Evaludation

## ENVIRONMENT VARIABLES

- "ANTHROPIC_API_KEY=your_key_here" - API Key is mandatory and should be placed in the folder.

## NOTEBOOK DESCRIPTION

### - Chapter 1 : Accessing Claude with API

- Making_A_Request.ipynb: Introduction to making API requests to Claude.
- Multi_Turn_Conversation.ipynb: Implementing multi-turn conversations with Claude.
- Chat_Exercise.ipynb: Hands-on exercise to practice chat interactions with Claude.
- System_prompts.ipynb: Understanding and using system prompts to control Claude's behavior.
- System_Prompts_Exercise.ipynb: Exercise to practice creating effective system prompts.
- Temperature.ipynb: Exploring the temperature parameter to control response creativity.
- Response_Streaming.ipynb: Implementing response streaming for real-time interactions.
- Controlling_Model_Output.ipynb: Techniques to control and refine Claude's output.
- Structured_Data.ipynb: Working with structured data inputs and outputs in Claude.

## FOLDER STRUCTURE

```
BUILDING WITH CLAUDE API/
├──Accessing Claude with API/
│ ├── Making_A_Request.ipynb
│ ├── Multi_Turn_Conversation.ipynb
│ ├── Chat_Exercise.ipynb
│ ├── System_prompts.ipynb
│ ├── System_Prompts_Exercise.ipynb
│ ├── Temperature.ipynb
│ ├── Response_Streaming.ipynb
│ ├── Controlling_Model_Output.ipynb
│ └── Structured_Data.ipynb
├──Prompt Evaluation/
│ ├── dataset.json
│ ├── Generating_Datasets_Evaluation_Grade.ipynb
│ ├── README.md
│ ├── Test_API.ipynb
├──Prompt Engineering Techniques/
│ ├── dataset.json
│ ├── output.html
│ ├── output.json
│ ├── prompting.ipynb
│ └── README.md
├──Tool Use with Claude/
│ ├── Text Editor Tool/
│ │  ├── main.py   <-File modified by model
│ │  ├── test.py   <-File created by model
│ │  └── text_editor_tool.ipynb
│ ├── Multi-Turn Conversation.ipynb
│ ├── Tool_Streaming.ipynb
│ ├── Tools.ipynb
│ ├── web_search_tool.ipynb
│ └── README.md
├──RAG and agentic Search/
│ ├── bm25.ipynb
│ ├── chunking.ipynb
│ ├── embeddings.ipynb
│ ├── hybrid.ipynb
│ ├── vectordb.ipynb
│ ├── report.md
│ └── README.md
├──Features Of Claude/
│ ├── images/
│ │  ├── prop1.png
│ │  ├── prop2.png
│ │  ├── prop3.png
│ │  ├── prop4.png
│ │  ├── prop5.png
│ │  ├── prop6.png
│ │  └── prop7.png
│ ├── earth.pdf
│ ├── images.ipynb
│ ├── thinking.ipynb
│ └── README.md
└── README.md
```
