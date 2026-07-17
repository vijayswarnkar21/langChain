from langchain_core.prompts import PromptTemplate

# template
template = PromptTemplate(
    template="""
        Generate summary of "{book_name}" book in "{language}" in "{lines}" lines.
        if the book is banned in India then your output should be
        "This book is banned in India"
    """,
input_variables=['book_name', 'language','lines'],
validate_template=True
)

template.save('template.json')