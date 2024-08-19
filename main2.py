import openai
import PyPDF2

# set your OpenAI API key
client = openai.OpenAI(api_key='add your openai key here')

def extract_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# you can be more prescriptive, I just added what I think is sufficient for a PoC of sorts
def gen_Utests(contract_text):
    prompt = f"""
    I have an Ethereum smart contract written in Solidity. 
    Please generate an extensive set of unit tests for all functions in the contract using Hardhat and ethers.js. 
    These tests should include:

    1. Basic functionality tests for each function.
    2. Edge case handling for inputs and outputs.
    3. Security vulnerability checks, including:
        - Reentrancy attacks
        - Overflows and underflows
        - Access control (e.g., onlyOwner modifiers)
        - Proper handling of external calls
    4. Tests that simulate complex interactions and user scenarios.
    5. Ensure proper event emissions are tested.
    6. Known common issues with Solidity smart contracts.
    
    Please make sure to:
    
    - Use Hardhat as the testing environment.
    - Use ethers.js for interacting with the contract and writing assertions.
    - Write the tests in JavaScript, not TypeScript.
    - Avoid using web3.js or pytest.
    
    Here is the smart contract code:

    {contract_text}
    
    Generate the unit tests in a neatly organized Hardhat-compatible format.
    """

    # new chat compleyion
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user","content": prompt
        }
    ],
    model="gpt-4o",
    )

    # extract content of the message from the response
    response_message = chat_completion.choices[0].message.content
    
    return response_message

def write_tests(test_cases, output_file):
    
    with open(output_file, 'w') as file:
        file.write(test_cases)

def main(pdf_path, output_file):
    # extract text from the PDF, generate unit test and then save to file
    contract_text = extract_text(pdf_path)
    
    test_cases = gen_Utests(contract_text)
   
    write_tests(test_cases, output_file)
    
    print(f"Test cases generated and written to {output_file}")


# usage with usdt contract code
pdf_path = 'contracts/usdt.pdf'  # path to your smart contract, i saved it as a pdf
output_file = 'unitTests.txt'  # test cases file
main(pdf_path, output_file)