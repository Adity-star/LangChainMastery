from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path=r'C:\Users\Administrator\OneDrive\Desktop\LangChainMastery\Books\Telco-Customer-Churn.csv')

docs = loader.load()

print(len(docs))

print(docs[1])