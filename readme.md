# Solidity Smart Contract Unit Test Generator

This repo contains two programs developed to automatically generate unit tests for Solidity smart contracts. The first program leverages LlamaIndex for Retrieval-Augmented Generation (RAG) to analyze Solidity files and generate the unit tests. The second program directly generates unit tests using predefined prompts along with the Solidity contract code.


## Project Description

This PoC aims to streamline the process of writing unit tests for Solidity smart contracts by automating the generation of these tests. Automation is achieved through two distinct methods:

1. **Retrieval-Augmented Generation (RAG)**: Utilizing LlamaIndex to analyze existing Solidity code and generate relevant unit tests based on the contract's functions and behaviors.
2. **Direct Generation from Prompts**: By integrating predefined prompts with the Solidity contract code, the program can directly generate specific and detailed unit tests.

Both projects use GPT-4o models.

## Prerequisites

- Git
- Node.js and npm
- Python 3.10
- Virtual environment for Python (reccomended)

### Installation

Clone the repository:

```bash
git clone https://github.com/mickymultani/genAI-unitTester.git
cd genAI-unitTester
```
