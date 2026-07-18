# CHANGES FROM ORIGINAL VERSION (and why):
#
# 1. Removed `from langchain.output_parsers import StructuredOutputParser, ResponseSchema`
#    (and the later attempt `from langchain_core.output_parsers import ...` of the same names).
#    Neither exists in the installed langchain/langchain-core (1.x) - StructuredOutputParser
#    and ResponseSchema were part of the legacy 0.x API and have been removed.
#
# 2. Replaced the ResponseSchema list + StructuredOutputParser.from_response_schemas(...)
#    with a Pydantic `Facts` model + PydanticOutputParser. This is the current, supported
#    way to describe a structured schema in langchain 1.x.
#
# 3. First tried `model.with_structured_output(Facts, method="json_schema")` instead of a
#    manual parser. That ran, but langchain_huggingface's implementation just wraps a plain
#    JsonOutputParser under the hood - it never actually validates the JSON against `Facts`,
#    so the model could return a totally different shape (e.g. {'facts': [...]}) with no error.
#    (Its default method, "function_calling", is worse: it unconditionally raises
#    NotImplementedError for any Pydantic schema - a limitation in that library.)
#
# 4. Switched to `parser = PydanticOutputParser(pydantic_object=Facts)` used directly in the
#    chain (`template | model | parser`). This actually enforces the schema: format
#    instructions describing the exact fields are injected into the prompt via
#    `partial_variables`, and `parser.parse()` raises OutputParserException if the model's
#    output doesn't validate against `Facts`, instead of silently passing bad data through.
#
# 5. Added `provider="featherless-ai"` to HuggingFaceEndpoint. Without it, HF's inference
#    router returned `model_not_supported` for google/gemma-2-2b-it under this account -
#    matches the working provider already used in jsonoutputparser_withoutcahin_3.py.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    provider="featherless-ai"
)

model = ChatHuggingFace(llm=llm)


class Facts(BaseModel):
    fact_1: str = Field(description='Fact 1 about the topic')
    fact_2: str = Field(description='Fact 2 about the topic')
    fact_3: str = Field(description='Fact 3 about the topic')


parser = PydanticOutputParser(pydantic_object=Facts)

template = PromptTemplate(
    template='Give 3 facts about {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)