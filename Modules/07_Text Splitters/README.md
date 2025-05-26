# ✂️ **Module 07: Text Splitters in LangChain**

Welcome to **Module 07 – Text Splitters**! In this module, we delve into the crucial preprocessing step of breaking down large documents into smaller, manageable chunks. This process enhances the efficiency and effectiveness of downstream tasks like **retrieval**, **summarization**, and **question answering**.

![text_splitters-7961ccc13e05e2fd7f7f58048e082f47](https://github.com/user-attachments/assets/09917717-5610-4ba6-a66f-d33b6a19ea58)

---
## ❓ Why Split Documents?

Splitting documents is essential for several reasons:

- **Handling Non-Uniform Document Lengths**  
  Real-world documents vary in size. Splitting ensures consistent processing across all documents.

- **Overcoming Model Limitations**  
  Many models have maximum input size constraints. Splitting allows processing of larger documents.

- **Improving Representation Quality**  
  Smaller chunks can lead to more focused and accurate representations.

- **Enhancing Retrieval Precision**  
  Fine-grained chunks improve the granularity of search results.

- **Optimizing Computational Resources**  
  Smaller chunks are more memory-efficient and allow better parallelization.

---
## 🔧 Key Concepts

- **Chunk Size:** The maximum number of characters or tokens per chunk.

- **Chunk Overlap:** The amount of content repeated between chunks to preserve context.

- **Separator:** The character(s) used to split the text (e.g., newline, period).

- **Metadata:** Additional information such as page number or source, carried with each chunk.

---
## 🧩 Types of Text Splitters

LangChain offers various text splitters, each suited for different scenarios:

1. **CharacterTextSplitter**  
   **Description:** Splits text based on a specified separator.  
   **Use Case:** Suitable for plain text documents where specific delimiters are present.

2. **RecursiveCharacterTextSplitter**  
   **Description:** Recursively splits text by different characters to find one that works.  
   **Use Case:** Ideal for structured text like articles or documentation.

3. **TokenTextSplitter**  
   **Description:** Splits text based on token count using a tokenizer.  
   **Use Case:** Useful when working with language models that have token limitations.

4. **MarkdownHeaderTextSplitter**  
   **Description:** Splits text based on Markdown header levels.  
   **Use Case:** Ideal for `.md` documents, blogs, and tutorials.

5. **HTMLHeaderTextSplitter**  
   **Description:** Splits text based on HTML header tags.  
   **Use Case:** Suitable for structured web content.
6. **LanguageAwareTextSplitter**  
   **Description:** Splits text based on language-specific rules.  
   **Use Case:** Useful for multilingual content.

7. **SemanticChunker (Experimental)**  
   **Description:** Splits text based on semantic meaning.  
   **Use Case:** Advanced use cases requiring semantic coherence.
---
## Overview of text splitters

| Splitter                         | Description                                    | Use Case                                |
| -------------------------------- | ---------------------------------------------- | --------------------------------------- |
| `CharacterTextSplitter`          | Splits by characters using specified separator | Simple plain text                       |
| `RecursiveCharacterTextSplitter` | Recursively splits by multiple separators      | Articles, documentation with paragraphs |
| `TokenTextSplitter`              | Splits based on token counts (model tokenizer) | Token-limited LLM contexts              |
| `MarkdownHeaderTextSplitter`     | Splits by markdown header levels               | `.md` files, blogs, tutorials           |
| `HTMLHeaderTextSplitter`         | Splits by HTML header tags                     | Structured web content                  |
| `LanguageAwareTextSplitter`      | Splits using language-specific rules           | Multilingual content                    |
| `SemanticChunker` (experimental) | Splits based on semantic coherence             | Advanced semantic chunking              |

---
##  Evaluating Text Splitters

To evaluate and visualize how different text splitters work, you can use the **Chunkviz** utility created by Greg Kamradt. This tool helps in tuning up the splitting parameters by showing how your text is being split.

##  Combining Splitters

You can combine multiple splitters to achieve the desired chunking strategy. For instance, you might first split by paragraphs and then by sentences within each paragraph.

---

##  Best Practices

- **Choose the Right Splitter:** Select a splitter that aligns with your document's structure and your application's requirements.

- **Adjust Parameters:** Fine-tune `chunk_size` and `chunk_overlap` to balance between context preservation and chunk size.

- **Evaluate Splitter Performance:** Use tools like Chunkviz to assess the effectiveness of your chosen splitter.

---
## 📌 Additional Notes on Text Splitters

- **Context Preservation vs. Chunk Size:**  
  Finding the right balance between chunk size and overlap is key. Too small chunks may lose context, while too large chunks might exceed model limits.

- **Handling Different File Types:**  
  Depending on the input format (PDF, HTML, Markdown, plain text), choose splitters designed to handle those structures for better results.

- **Custom Splitters:**  
  You can implement custom text splitters tailored to your specific document structure or domain to improve chunking quality.

- **Performance Considerations:**  
  Chunking large datasets can be computationally intensive; consider batch processing or parallelization.

- **Impact on Downstream Tasks:**  
  The choice and configuration of text splitters directly affect retrieval accuracy, summarization coherence, and QA performance.

- **Integration with LangChain Pipelines:**  
  Text splitters are typically the first step in a LangChain pipeline, so properly tuning them sets a strong foundation for all subsequent tasks.

- **Logging and Debugging:**  
  Always log chunk sizes and overlaps during preprocessing to debug issues related to model input size errors or poor retrieval performance.

- **Multilingual and Domain-Specific Splitting:**  
  When working with multilingual data or specialized domains (legal, medical), prefer splitters that can respect language or domain-specific syntax and semantics.

---
## Practice
- [`Lengh Based`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/07_Text%20Splitters/length_based.py)
- [`Markdown Splitter`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/07_Text%20Splitters/markdown_splitting.py)
- [`Code Splitting`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/07_Text%20Splitters/python_code_splitting.py)
- [`Semantic Based`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/07_Text%20Splitters/semantic_meaning_based.py)
- [`Text Based`](https://github.com/Adity-star/LangChainMastery/blob/main/Modules/07_Text%20Splitters/text_structure_based.py)


---
## Further reading
- [Langchain Text Splitters Documentation](https://python.langchain.com/docs/concepts/text_splitters/)
- [How to split codes](https://python.langchain.com/docs/how_to/code_splitter/)

---

## Next Step
You have completed 70% of LangChain Mastery! Ready to tackle the remaining 30%?
After mastering Text Splitters, proceed to:
👉 [Module 08: Vector Store](https://github.com/Adity-star/LangChainMastery/tree/main/Modules/08_Vector%20Store)
