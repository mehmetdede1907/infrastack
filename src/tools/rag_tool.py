from crewai_tools.tools.rag import rag_tool

# Initialize the RagTool with the knowledge base directory
rag_tool = rag_tool().from_directory('data/knowledge_base')

# If you want to add specific files or web pages, you can do so like this:
# rag_tool.add('path/to/specific/file.txt')
# rag_tool.add('https://example.com/sre-best-practices')

# You can also customize the tool name and description if needed
rag_tool.name = "SRE Knowledge Base"
rag_tool.description = "A knowledge base containing SRE best practices, common errors, and troubleshooting guides."