import re

# cache messages in variables 

welcome_message = """
  *************************************************
             Welcome to MadLibs Creator!
      Get funny and creative with your answers.
    Don't be afraid to get really silly with it!! 
     Enter 'EXIT' or 'QUIT' to exit application.
  *************************************************
  """

result_message = """
  *************************************************
             Thanks for playing MadLibs!
                Check out your story:
  *************************************************
  """

# Paths 

path_template = "../assets/madlibTemp.txt"
path_output = "../assets/output.txt"

# Functions

def welcome():
  """
  Prints welcome message to user upon application start! 
  """
  print(welcome_message)

def word_or_phrase_prompt(type_of_word: str) -> str:
  """
  Prompts the user for a word or phrase!

  Argument: type_of_word (name, adjective, noun, etc...)

  Output: The user's input (a string) 
  """
  user_prompt = f"Please enter a(n) {type_of_word}: "
  user_input = input(user_prompt)
  return user_input

def read_template(file_path: str) -> str:
  """
  Reads the Madlib template file and returns content as a string.

  Arguments: the file path (file_path)

  Output: Contents of the file as a string
  """
  try:
    with open(file_path, "r") as tempFile:
      return tempFile.read()
  except FileNotFoundError:
    raise 
  
def parse_template(template: str) -> str:
  """ 
  Parses the text in language parts (the brackets) and returns a string with those lanaguage parts removed. Those language parts are then returned as a separate list.

  Argument: the template(template) to be parsed.

  Output: The stripped text (template with language parts in brackets removed) and then a separate list of those language parts. 
  """

  pattern = r"{(['\w\s-]*)}"
  substitution = "{}"
  
  language_parts = list(re.findall(pattern, template))
  template_stripped = re.sub(pattern, substitution, template)

  return template_stripped, language_parts

def merge(template: str, inputs: list) -> str and list: 
  """
  Merges the list of words/phrases into the STRIPPED madlibs template.

  Arguments: template (stripped template as string) and words (words or phrases as list)

  Output: Complete story (merge)
  """
  pattern = r"{}"
  match = re.findall(pattern, template)

  for input in inputs:
    template = re.sub(pattern, input, template, +1)
  
  return template

def write_output(template: str) -> str: 
  """
  Write output text to output.txt file
  
  Argument: The template updated with user data (string)
  """
  with open(path_output, "w") as file:
    file.write(template)

def print_output(user_story: str) -> str:
  """
  Print out result_message and the story for the user after all inputs have been received.

  Arguments: user_story (The story output)

  Output: The printing of result_message and user_story
  """ 
  print(result_message)
  print(user_story)

def start_program(): 
  """
  This function runs this command line application
  """
  welcome()
  template = read_template(path_template)
  template_stripped, language_parts = parse_template(template)
  input_new_list = []

  for part in language_parts:
    input_new = word_or_phrase_prompt(part)
    if input_new.upper() == "EXIT" or input_new.upper() == "QUIT":
      quit()
    else: 
      input_new_list.append(input_new)
  
  final_story = merge(template_stripped, list(input_new_list))
  print_output(final_story)
  write_output(final_story)

# Run the program:
while __name__ == "__main__":
  start_program()
